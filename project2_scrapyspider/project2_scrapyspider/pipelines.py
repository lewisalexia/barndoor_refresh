# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import json
import env

class JsonLinesPipeline:
    def open_spider(self, spider):
        self.file_path = env.jsonl_path
        self.file = open(self.file_path, 'a')

    def process_item(self, item, spider):
        item_dict = ItemAdapter(item).asdict()
        line = json.dumps(item_dict) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()