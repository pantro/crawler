import threading

#import logging

#Log para hilos
#logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s) %(message)s')

class ThreadCustom(threading.Thread):
    # select elements in the table
    selector_general = 'html'
    selector_head_title = 'head title'
    selector_header_nav = 'header nav li > a '
    selector_links = 'a'

    def __init__(self, path, website, num_page, corpus):
        threading.Thread.__init__(self, target=ThreadCustom.scraping, args=(self, corpus))

        self.path = path
        self.website = website
        self.driver = ''
        self.num_page = num_page
        self.url = self.build_url(self.website, self.num_page)
        self.element_general = ""
        self.element_authors = ""

    def build_url(self, website, num_page):
        return website+'/page/'+str(num_page)

    def open_web(self):
        print("Verificando URL: " + self.url)
        self.driver = webdriver.Chrome(self.path)
        # Abrir web
        self.driver.get(self.url)
        # Esperar un tiempo hasta que todo cargue
        self.driver.implicitly_wait(0.5)
        return

    def close_web(self):
        # quit drive we opened in the beginning
        self.driver.quit()
        return

    def scraping(self, corpus):
        self.open_web()
        #logging.info("Guardando para el id " + str(id_persona) + " la data " + data)

        self.element_general = self.driver.find_element(by=By.CSS_SELECTOR, value=ThreadCustom.selector_general)
        self.get_links()
        return
    def get_title_web(self):
        self.element_authors = self.element_general.find_elements(by=By.CSS_SELECTOR, value=ThreadCustom.selector_header_nav)
        return

    def get_links(self):
        element_links = self.element_general.find_elements(by=By.CSS_SELECTOR, value=ThreadCustom.selector_links)
        element_authors = [e.get_attribute("href") for e in self.element_links]
        print(self.element_authors)
        return

    def get_html(self):
        html = self.driver.page_source
        return html
