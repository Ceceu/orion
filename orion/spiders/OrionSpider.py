import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class OrionSpider(CrawlSpider):
    name = "orion"
    start_urls = ["https://www.uol.com.br/"]

    rules = [
        Rule(LinkExtractor(allow=("\.br")), callback="parse_items", follow=True)
    ]

    def parse_items(self, response):
        yield {
            "url": response.request.url,
            "html_content": response.text  # .body
        }
