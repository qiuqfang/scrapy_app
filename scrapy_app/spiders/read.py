import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_app.items import ReadItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1078_1.html"]

    rules = (Rule(LinkExtractor(allow=r"/book/1078_\d+\.html"), follow=True),)

    def parse(self, response, **kwargs):
        img_list = response.xpath("//div[@class='bookslist']//img")
        for img in img_list:
            src = img.xpath("./@data-original").extract_first()
            name = img.xpath("./@alt").extract_first()

            if src:
                src = src
            else:
                src = img.xpath("./@src").extract_first()

            book = ReadItem(src=src, name=name)
            yield book
