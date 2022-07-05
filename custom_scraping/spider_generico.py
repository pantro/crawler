import scrapy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv('.env')
URL_GENERICOS = eval(os.getenv('URL_GENERICOS'))
URL_DOMAIN_GENERICOS = eval(os.getenv('URL_DOMAIN_GENERICOS'))

class CustomSpiderGenerico(scrapy.Spider):
    name = "spider_generico"

    # Dominios permitidos
    allowed_domains = URL_DOMAIN_GENERICOS

    # URLs para comenzar a rastrear
    start_urls = URL_GENERICOS

    def parse(self, response):
        menus = response.css('nav ul > li > a::attr(href)').getall()

        for menu in menus:
            yield scrapy.Request(
                response.urljoin(menu),
                callback=self.parse_page
            )
        result = self.get_data(response)
        yield result

    def parse_page(self, response):
        result = self.get_data(response)
        yield result

    def get_data(self, response):
        title = response.css('h1::text').get()

        # DEscripcion obtendida de la etiqueta "p"
        description_p = set(response.css('p::text').getall())
        description_p = [i for i in description_p if not (i == "\n")]  # Eliminando \n
        description_p = {' '.join(description_p)}  # Juntando todos los parrafos
        # DEscripcion obtendida de la etiqueta "span"
        description_span = set(response.css('p span::text').getall())
        description_span = [i for i in description_span if not (i == "\n")]  # Eliminando \n
        description_span = {' '.join(
            description_span)}  # Juntando todos los parrafos, continua siendo SET para que al juntarse no se agreguen duplicados
        # Juntando descripciones
        description = description_p | description_span
        description = ' '.join(description)

        url = response.url

        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        return {
            'title': title,
            'description': description,
            'url': url,
            'date': date
        }
