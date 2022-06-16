class Node:
    def __init__(self, url):
        self.url = url
        self.properties = {
            'header_links': list(),
            'content_links': list(),
            'content': list(),
            'teste_links': list(),
            'teste_content': list(),
        }

    def __str__(self):
        print(self.url)

    # Agregar un elemento
    def add_header_link(self, link):
        self.properties['header_links'].append(Node(link))
        return

    def add_content_link(self, link):
        self.properties['content_links'].append(Node(link))
        return

    def add_content(self, text):
        self.properties['content'].append(text)
        return

    def add_teste_link(self, link):
        self.properties['teste_links'].append(Node(link))
        return

    def add_teste_content(self, text):
        self.properties['teste_content'].append(text)
        return
