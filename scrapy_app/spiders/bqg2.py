import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_app.items import Bqg2Item


class Bqg2Spider(CrawlSpider):
    name = "bqg2"
    allowed_domains = ["www.bqg2.org"]
    start_urls = ["https://www.bqg2.org/212/212267/2603.html"]

    rules = (Rule(LinkExtractor(allow=r"2603_\d+\.html"), callback="parse_item", follow=True),)

    def parse_start_url(self, response, **kwargs):
        content_list = response.xpath("//p[@class='articlecontent']/text()").extract()

        page_content = ""
        length = len(content_list) - 2
        for content in content_list[0:length]:
            page_content += str.strip(content) + "<br>"

        bqg2 = Bqg2Item(content=page_content)
        yield bqg2

    def parse_item(self, response):
        content_list = response.xpath("//p[@class='articlecontent']/text()").extract()

        page_content = ""
        length = len(content_list) - 2
        for content in content_list[0:length]:
            page_content += str.strip(content) + "<br>"

        bqg2 = Bqg2Item(content=page_content)
        yield bqg2
