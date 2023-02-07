import scrapy


class AlispiderSpider(scrapy.Spider):
    name = "AliSpider"
    allowed_domains = ["www.aliexpress.com"]
    start_urls = ["http://www.aliexpress.com/"]

    def parse(self, response):
        pass
