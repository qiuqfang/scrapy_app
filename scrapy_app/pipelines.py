# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy_app.utils import mkdir


class ScrapyAppPipeline:
    def open_spider(self, spider):
        print("ScrapyAppPipeline 开始")

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        print("ScrapyAppPipeline 结束")


class DangDangSavePipeline:
    def open_spider(self, spider):
        mkdir('./books')
        self.fp = open("./books/book.json", 'w', encoding='utf-8')
        self.fp.write('[')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        self.fp.write(',')
        return item

    def close_spider(self, spider):
        self.fp.write(']')
        self.fp.close()


import urllib.request


# 多条管道开启
class DangDangDownloadPipeline:
    def open_spider(self, spider):
        print("开始下载")

    def process_item(self, item, spider):
        url = "http:" + item.get('src')
        filename = "./books/" + item.get("name") + '.jpg'

        urllib.request.urlretrieve(url, filename)
        return item

    def close_spider(self, spider):
        print("结束下载")
