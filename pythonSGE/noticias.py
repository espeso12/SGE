from types import new_class

import requests


class Fuente:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Nombre: " + self.name


class Noticia:
    def __init__(self, author, title, description, content, published_at, source):
        self.author = author
        self.title = title
        self.description = description
        self.content = content
        self.published_at = published_at
        self.source = Fuente(source)

    def __str__(self):
        return (
            print(f"Titular: {self.title}"
                  f"Description: {self.description}"
                  f"Published at: {self.published_at}"
                  f"Contenido: {self.content}"
                  f"Autor: {self.author}"
                  f"Fuente: {self.source.name}")
        )


def recuperar_noticias():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=a5c14900304d4028b0adf48c9aa9d72c"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        articulos = []
        for articulo in data['articles']:
            n = Noticia(
                articulo['author'],
                articulo['title'],
                articulo['description'],
                articulo['content'],
                articulo['publishedAt'],
                Fuente(articulo['source']['name'])
            )
            print(n)
            articulos.append(n)

        print(articulos)


def main():
    recuperar_noticias()


main()
