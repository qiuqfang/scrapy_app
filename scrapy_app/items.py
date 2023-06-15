# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAppItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()


class Bqg2Item(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    fp = scrapy.Field()


class DangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    src = scrapy.Field()  # 图片
    name = scrapy.Field()  # 名字
    price = scrapy.Field()  # 价格


class ReadItem(scrapy.Item):
    src = scrapy.Field()  # 图片
    name = scrapy.Field()  # 名字
