import scrapy
import pandas as pd
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
        print(f'US News Titles Found {len(titles)}')