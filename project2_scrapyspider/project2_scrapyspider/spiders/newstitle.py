import scrapy
import os
import pandas as pd
import env

if not os.path.isfile(env.csv_path):
    df = pd.DataFrame(columns=['us_news'])
    df.to_csv(env.csv_path, index=False)

from project2_scrapyspider.items import Project2ScrapyspiderItem

class NewstitleSpider(scrapy.Spider):
    name = "newstitle"
    allowed_domains = [
                    "www.realnewsnotbs.com"
                      ]
    start_urls = [
        "https://www.realnewsnotbs.com/us-news"
                ]

    def parse(self, response):
        titles = response.xpath('//a[@class="bg-wrap-link"]/@aria-label').getall()
        for title in titles:
            item = Project2ScrapyspiderItem()
            item['us_news'] = title
            yield item