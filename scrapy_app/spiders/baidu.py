import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字，用于运行爬虫的时候 使用的值
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始的url地址
    start_urls = ["https://www.baidu.com"]

    def parse(self, response, **kwargs):
        names = response.xpath("//div[@id='s-top-left']/a/text()")
        print(names.extract_first())
        for name in names:
            print(name.extract())

        pass