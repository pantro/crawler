import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyScraping(CrawlSpider):
    name = 'myscraping'
    allowed_domains = ['aosfatos.org']
    start_urls = ['https://aosfatos.org/']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths='//li[contains(text(), "Checamos")]//ul/li'
            )
        ),
        Rule(
            LinkExtractor(
                restrict_css=('a.card')
            ),
            callback='parse_new'
        )
    )

    def paser_new(self, response):
        import ipdb; ipdb.set_trace()
        #title = response.css('article h1::text')