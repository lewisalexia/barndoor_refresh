# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import pandas as pd
import os
import env

class DuplicatesPipeline:
    def open_spider(self, spider):
        self.csv_path = env.csv_path
        
        # Load existing data if CSV exists, else prepare an empty DataFrame
        if os.path.isfile(self.csv_path):
            self.existing_data = pd.read_csv(self.csv_path, usecols=['us_news']).drop_duplicates('us_news')
        else:
            self.existing_data = pd.DataFrame(columns=['us_news'])
        
        # Initialize a list to store new items
        self.new_items = []

    def process_item(self, item, spider):
        # Convert item to DataFrame for easy comparison
        item_df = pd.DataFrame([item])
        
        # Check if the item's title is already in the loaded DataFrame
        if not item_df['us_news'].isin(self.existing_data['us_news']).any():
            self.new_items.append(item)
        
        return item

    def close_spider(self, spider):
        # If there are new items, process them
        if self.new_items:
            # Convert list of items to DataFrame
            new_items_df = pd.DataFrame(self.new_items)
            
            # Concatenate new items with existing data and remove any duplicates
            updated_data = pd.concat([self.existing_data, new_items_df], ignore_index=True).drop_duplicates('us_news')
            
            # Write the updated DataFrame to CSV
            updated_data.to_csv(self.csv_path, index=False)