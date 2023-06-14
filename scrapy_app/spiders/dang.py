import scrapy

from scrapy_app.items import ScrapyAppItem


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.49.05.11.00.00.html"]

    base_url = "https://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构

        # src = //ul[@id='component_59']/li//img/@src
        # name = //ul[@id='component_59']/li//img/@alt
        # price = //ul[@id='component_59']/li//p[@class='price']/span[1]/text()

        li_list = response.xpath("//ul[@id='component_59']/li")
        for li in li_list:
            src = li.xpath(".//img/@data-original").extract_first()
            if src:
                src = src
            else:
                src = li.xpath(".//img/@src").extract_first()

            name = li.xpath(".//img/@alt").extract_first()
            price = li.xpath(".//p[@class='price']/span[1]/text()").extract_first()
            print(src, name, price)
            book = ScrapyAppItem(src=src, name=name, price=price)

            # 获取一个book就将book交给pipelines
            yield book

        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + "-cp01.49.05.11.00.00.html"

            # 调用get方法
            yield scrapy.Request(url, callback=self.parse)

        pass
