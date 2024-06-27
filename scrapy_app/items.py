# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# 定义项目（items），也就是你从网站上爬取的数据的结构。通过定义一个或多个类，这些类表示你希望从网站上提取的数据的模型，每个类包含的字段（Field）对应你爬取的数据的不同属性。

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
