# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy_app.utils import mkdir
import urllib.request


class ScrapyAppPipeline:
    def open_spider(self, spider):
        print("ScrapyAppPipeline 开始")

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        print("ScrapyAppPipeline 结束")


class ReadSavePipeline:
    def open_spider(self, spider):
        mkdir('./read')
        self.fp = open("./read/book.csv", 'w', encoding='utf-8')

    def process_item(self, item, spider):
        txt = str.format("{},{}\n", item['name'], item['src'])
        self.fp.write(txt)
        return item

    def close_spider(self, spider):
        self.fp.close()


class ReadDownloadPipeline:
    def open_spider(self, spider):
        mkdir('./read/img')
        print("开始下载")

    def process_item(self, item, spider):
        url = item.get('src')
        filename = "./read/img/" + item.get("name") + '.jpg'

        urllib.request.urlretrieve(url, filename)
        return item

    def close_spider(self, spider):
        print("结束下载")


class DangDangSavePipeline:
    def open_spider(self, spider):
        mkdir('./dang')
        self.fp = open("./dang/book.csv", 'w', encoding='utf-8')

    def process_item(self, item, spider):
        txt = str.format("{},{},{}\n", item['name'], item['src'], item["price"])
        self.fp.write(txt)
        return item

    def close_spider(self, spider):
        self.fp.close()


class DangDangDownloadPipeline:
    def open_spider(self, spider):
        mkdir('./dang/img')
        print("开始下载")

    def process_item(self, item, spider):
        url = "http:" + item.get('src')
        filename = "./dang/img/" + item.get("name") + '.jpg'

        urllib.request.urlretrieve(url, filename)
        return item

    def close_spider(self, spider):
        print("结束下载")
