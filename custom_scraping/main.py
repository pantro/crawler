import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyScraping(scrapy.Spider):
    name = 'myscraping'
    allowed_domains = ['aosfatos.org']
    start_urls = ['https://aosfatos.org/']
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
        links = response.xpath('//nav//ul//li/a[re:test(@href, "checamos")]/@href').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_category
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
        title = response.css('article h1::text').get()
        date = ' '.join(response.css('div.publish-date::text').get().split())

        quotes = response.css('article blockquote p')
        for quote in quotes:
            quote_text = quote.css('::text').get()
            status = quote.xpath(
                './parent::blockquote/preceding-sibling::figure//figcaption/text()'
            ).get()
            yield {
                'title': title,
                'date': date,
                'quote_text': quote_text,
                'status': status,
                'url': response.url
            }
