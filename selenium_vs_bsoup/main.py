import sys

from collections import Counter

from BS import BS
from Node import Node
from Selenium import Selenium

cant_threads = 2

MAX_LINKS = 1

URL_MAIN = ''#Pagina web

select_header_links = 'nav li > a'
select_content_links = 'body a'
select_text = 'p'

#URL VISITADAS
url_total = {URL_MAIN}# tipo de dato SET

corpus = list()
visited = list()  # List to keep track of visited nodes.
queue = list()  # Initialize a queue
def main():
    corpus = Node(URL_MAIN)
    ############################################
    add_node(corpus, 'header_links')
    print("hola")

def add_node(node, childrens):
    if len(visited) < MAX_LINKS:
        start_scraping(node)
        visited.append(node.url)
        if node.properties[childrens]:
            queue.extend(node.properties[childrens])
        while queue:
            current = queue.pop(0)
            add_node(current, childrens)
    return

def start_scraping(obj_local):
    #-- Objeto selenium
    selenium = Selenium(obj_local.url)
    #---------------
    # -- Objeto selenium
    bs = BS(obj_local.url)
    # ---------------

    # HEADER_LINKS
    header_links = array_links(selenium.get_links(select_header_links))
    teste_link = array_links(bs.get_link(select_header_links))
    for link in header_links:
        obj_local.add_header_link(link)
    for link in teste_link:
        obj_local.add_teste_link(link)

    # CONTENT_LINKS
    content_links = array_links(selenium.get_links(select_content_links))
    content_links = list((Counter(content_links) - Counter(header_links)).elements())  # Obtener solo los link unicos para content
    for link in content_links:
        obj_local.add_content_link(link)

    # CONTENT_TEXT
    content_text = selenium.get_text(select_text)
    teste_text = bs.get_text(select_text)
    content_text = clean_none(content_text)
    teste_text = clean_none(teste_text)
    for text in content_text:
        obj_local.add_content(text)
    for text in teste_text:
        obj_local.add_teste_content(text)
    #--Objeto selenium
    selenium.close_web()
    del selenium
    #-------------
    return obj_local

def array_links(list_links):
    links = clean_none(list_links)
    links = drop_link_visit(links)
    return links

def clean_none(var_list):
    #Eliminar None
    var_local = [i for i in var_list if i] #Elimina vacios
    var_local = list(dict.fromkeys(var_local)) #Elimina duplicados
    return var_local

def remove_slash(url_local):
    letter_end = url_local[len(url_local) - 1]
    if letter_end == '/':
        return url_local[0:len(url_local) - 1]
    else:
        return url_local

def drop_link_visit(var_list):
    new_list = list()
    for i in range(len(var_list)):
        #Revisamos que no contenga '#' y que pertenesca al mismo dominio
        if not ('#' in var_list[i]) and (URL_MAIN in var_list[i]):
            new_url = remove_slash(var_list[i])
            #Revisa que no lo tenga agregado ese url
            if not new_url in url_total:
                url_total.add(new_url)# tipo de dato SET
                new_list.append(new_url)
    return new_list

if __name__ == "__main__":
    sys.exit(main())

'''
scraping = Scraping(website, num_page, corpus)
scraping.start()
print('hola')

corpus_current = corpus.properties['header_links']
for i in range(cant_levels):
    if len(corpus_current) > 0:
        for j in range(0,len(corpus_current)-1):
            aux = Scraping(path, corpus_current[j],num_page, corpus_current[j])
            aux.start()
            print("esta en el for")
'''

'''
    t = ThreadCustom(path,  website, i+1, corpus)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
    result.extend(t.element_authors)
print(len(result))
#Buscando solo unicos
new_result = list(set(result))
print(len(new_result))

print("fffffffffffffffiiiiiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnn")
'''
'''
aux = new_result[0]#"https://www.profissionaisti.com.br/author/lqgusso/"
driver = webdriver.Chrome(path)
# Abrir web
driver.get(aux)
# Esperar un tiempo hasta que todo cargue
driver.implicitly_wait(0.5)
aux_selector = '.author-description p'
aux2 = driver.find_element(by=By.CSS_SELECTOR, value=aux_selector)
print('DESCRIPCION:')
print(aux2.text)
print("-----------------")
driver.quit()
'''
'''
# Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'goals': all_matches})
print(df)
df.to_csv('tutorial.csv', index=False)
'''