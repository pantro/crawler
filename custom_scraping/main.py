import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyScraping(scrapy.Spider):
    name = 'myscraping'
    allowed_domains = ['']
    start_urls = ['']

    '''
    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths='//li[contains(text(), "Checamos")]//ul/li'
            ),
            callback='parse_new'
        ),
        Rule(
            LinkExtractor(
                restrict_css=('a.card')
            ),
            callback='parse_new'
        )
    )
    '''

    def parse(self, response):
        links = response.css('article header a::attr(href)').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_new
            )

    def parse_category(self, response):
        news = response.css('.entry-item-card::attr(href)').getall()
        for new_url in news:
            yield scrapy.Request(
                response.urljoin(new_url),
                callback=self.parse_new
            )
        pages_url = response.css('.pagination a::attr(href)').getall()
        for page in pages_url:
            yield scrapy.Request(
                response.urljoin(page),
                callback=self.parse_category
            )

    def parse_new(self, response):
        #import ipdb; ipdb.set_trace()
        title = response.css('article header h2::text').get()

        quotes = response.css('article .entry-content p')
        for quote in quotes:
            quote_text = quote.css('::text').get()
            yield {
                'title': title,
                'quote_text': quote_text,
                'url': response.url
            }
