import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_app.items import Bqg2Item


class Bqg2Spider(scrapy.Spider):
    name = "bqg2"
    allowed_domains = ["www.bqg2.org"]
    start_urls = ["https://www.bqg2.org/212/212267/"]

    base_url = "https://www.bqg2.org"

    base_href = ""
    page = 1
    a_list = None
    a_list_len = 0
    current_a = 20
    fp = None
    all_page = None

    def parse(self, response, **kwargs):
        self.a_list = response.xpath("//div[@class='ml_list']//li/a")
        self.a_list_len = len(self.a_list)
        print(self.a_list_len)
        url = self.common_fn("w")
        yield scrapy.Request(url, callback=self.other_parse)

    def other_parse(self, response):
        if self.all_page is None:
            title = str.strip(response.xpath("//div[@class='nr_title']//h3/text()").extract_first())
            self.all_page = int(title[len(title) - 2])

        content_list = response.xpath("//p[@class='articlecontent']/text()").extract()

        page_content = ""
        length = len(content_list) - 2
        for content in content_list[0:length]:
            page_content += str.strip(content) + "<br>"

        bqg2 = Bqg2Item(content=page_content, fp=self.fp)
        yield bqg2

        if self.page < self.all_page:
            self.page += 1
            url = self.base_url + self.base_href + "_" + str(self.page) + '.html'
            yield scrapy.Request(url, callback=self.other_parse)
        else:
            self.fp.write("\n")
            self.fp.close()
            if self.current_a < self.a_list_len - 1:
                self.all_page = None
                self.current_a += 1
                url = self.common_fn("a")
                yield scrapy.Request(url, callback=self.other_parse)

    def common_fn(self, fp_type):

        self.fp = open("./bqg2/book.csv", fp_type, encoding="utf-8")
        if fp_type == 'w':
            self.fp.write("章节,内容\n")
            
        self.fp.write(str(self.current_a + 1) + ",")
        href = self.a_list[self.current_a].xpath("./@href").extract_first()
        self.base_href = href[0:len(href) - 5]
        self.page = 1
        url = self.base_url + self.base_href + "_" + str(self.page) + ".html"
        return url
