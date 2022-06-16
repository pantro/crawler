from selenium import webdriver
from selenium.webdriver.common.by import By

path = 'C:/Users/crist/Downloads/chromedriver_win32/chromedriver.exe'  # write the path here of chromediver
select_general = 'html'


class Selenium:
    def __init__(self, url):
        self.url = url
        self.driver = ''
        self.element_general = ''
        # Metodo por default
        self.start()

    def start(self):
        self.open_web()
        self.element_general = self.driver.find_element(by=By.CSS_SELECTOR, value=select_general)
        return

    def get_links(self, selector):
        copy_element_general = self.element_general
        var_local = copy_element_general.find_elements(by=By.CSS_SELECTOR, value=selector)
        var_local = [e.get_attribute("href") for e in var_local]
        return var_local

    def get_text(self, selector):
        copy_element_general = self.element_general
        var_local = copy_element_general.find_elements(by=By.CSS_SELECTOR, value=selector)
        var_local = [e.text for e in var_local]
        return var_local

    def open_web(self):
        self.driver = webdriver.Chrome(path)
        # Abrir web
        self.driver.get(self.url)
        # Esperar un tiempo hasta que todo cargue
        self.driver.implicitly_wait(1)
        return

    def close_web(self):
        # quit drive we opened in the beginning
        self.driver.quit()
        return
