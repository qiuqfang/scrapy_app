import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_app.items import Bqg2Item


class Bqg2_1Spider(scrapy.Spider):
    name = "bqg2_1"
    allowed_domains = ["www.bqg2.org"]
    start_urls = ["https://www.bqg2.org/212/212267/"]

    base_url = "https://www.bqg2.org"

    base_href = ""
    page = 1
    a_list = None
    a_list_len = 0
    current_a = 2579
    fp = None

    def parse(self, response):
        self.a_list = response.xpath("//div[@class='ml_list']//li/a")
        self.a_list_len = len(self.a_list)
        print(self.a_list_len)

        href = self.a_list[self.current_a].xpath("./@href").extract_first()
        self.base_href = href[0:len(href) - 5]
        self.page = 1
        url = self.base_url + self.base_href + "_" + str(self.page) + ".html"
        self.fp = open("./bqg2/book.csv", 'w', encoding='utf-8')
        self.fp.write(str(self.current_a + 1) + ",")
        yield scrapy.Request(url, callback=self.other_parse)
        pass

    def other_parse(self, response):
        content_list = response.xpath("//p[@class='articlecontent']/text()").extract()

        page_content = ""
        length = len(content_list) - 2
        for content in content_list[0:length]:
            page_content += str.strip(content) + "<br>"

        bqg2 = Bqg2Item(content=page_content, fp=self.fp)
        yield bqg2

        if self.page < 3:
            self.page += 1
            url = self.base_url + self.base_href + "_" + str(self.page) + '.html'
            yield scrapy.Request(url, callback=self.other_parse)
        else:
            self.fp.write("\n")
            self.fp.close()
            if self.current_a < self.a_list_len - 1:
                self.current_a += 1
                self.fp = open("./bqg2/book.csv", "a", encoding="utf-8")
                self.fp.write(str(self.current_a + 1) + ",")
                href = self.a_list[self.current_a].xpath("./@href").extract_first()
                self.base_href = href[0:len(href) - 5]
                self.page = 1
                url = self.base_url + self.base_href + "_" + str(self.page) + ".html"
                yield scrapy.Request(url, callback=self.other_parse)
