import scrapy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv('.env')
URL = eval(os.getenv('URL_2'))
URL_DOMAIN = eval(os.getenv('URL_DOMAIN_2'))

class CustomSpider_2(scrapy.Spider):
    name = "spider_2"

    # Dominios permitidos
    allowed_domains = URL_DOMAIN

    # URLs para comenzar a rastrear
    start_urls = URL

    def parse(self, response):
        categories = response.css('.menu-item-has-children:first-child > ul > li > a::attr(href)').getall()

        for category in categories:
            yield scrapy.Request(
                response.urljoin(category),
                callback=self.parse_link
            )

    def parse_link(self, response):
        links = response.css('article h2 a::attr(href)').getall()

        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_article
            )

        #Activar el paginador
        pages = response.css('.posts-navigation .nav-previous > a::attr(href)').getall()
        for page in pages:
            yield scrapy.Request(
                response.urljoin(page),
                callback=self.parse_link
            )

    def parse_article(self, response):
        title = response.css('article h1.entry-title::text').get()
        description = response.css('article .entry-content p::text').getall()
        description = [i for i in description if not (i == "\n")]#Eliminando \n
        description = ' '.join(description)#Juntando todos los parrafos
        url = response.url
        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        result = {
            'title': title,
            'description': description,
            'url': url,
            'date': date
        }
        yield result

