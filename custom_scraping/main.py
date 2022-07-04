import scrapy

import os
from dotenv import load_dotenv

load_dotenv('.env')
URL = eval(os.getenv('URL'))
URL_DOMAIN = eval(os.getenv('URL_DOMAIN'))

class CustomSpider(scrapy.Spider):
    name = "spider_2"

    # Dominios permitidos
    allowed_domains = URL_DOMAIN

    # URLs para comenzar a rastrear
    start_urls = URL

    '''def parse(self, response):
        menus = response.css('article h2 a::attr(href)').getall()

        for menu in menus:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_article
            )
'''
    def parse(self, response):
        links = response.css('article h2 a::attr(href)').getall()

        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_article
            )

    def parse_article(self, response):
        title = response.css('article h2.entry-title::text').get()
        description = response.css('article p::text').getall()
        description = [i for i in description if not (i == "\n")]#Eliminando \n
        description = ' '.join(description)#Juntando todos los parrafos

        '''yield {
            'title': title,
            'description': description,
            'url': response.url
        }
        '''
        print('----------------------------------------------------')
        print('title: ',title)
        print('description: ',description)
        print('----------------------------------------------------')

