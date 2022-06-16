import requests
from bs4 import BeautifulSoup


class BS:
    def __init__(self, url):
        self.url = url
        self.soup = ''
        self.start()

    def start(self):
        html_text = requests.get(self.url).text
        self.soup = BeautifulSoup(html_text, 'html.parser')
        return

    def get_link(self, selector):
        copy_soup = self.soup
        array_temp = list()
        for link in copy_soup.select(selector):
            array_temp.append(link.get('href'))
        return array_temp

    def get_text(self, selector):
        copy_soup = self.soup
        array_temp = list()
        for link in copy_soup.select(selector):
            array_temp.append(link.text)
        return array_temp
