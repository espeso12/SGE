import requests
import json

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/'

    def get_top_headlines(self, country='us'):
        """Obtiene los titulares de noticias de un país específico."""
        url = f'{self.base_url}top-headlines?country={country}&apiKey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('articles', [])
        else:
            print("Error recuperando noticias")

    def search_news(self, query):
        """Busca noticias relacionadas con una consulta específica."""
        url = f'{self.base_url}everything?q={query}&apiKey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('articles', [])
        else:
            print("Error recuperando noticias")

def save_news_to_json(news_articles, filename='news.json'):
    """Guarda los artículos de noticias en un archivo JSON."""
    with open(filename, 'w') as f:
        json.dump(news_articles, f, indent=4)

def validate_country_code(country_code):
    """Valida el código del país ingresado por el usuario."""
    valid_codes = ['us', 'es', 'fr', 'de', 'it', 'gb']
    return country_code in valid_codes

def main():
    api_key = 'a5c14900304d4028b0adf48c9aa9d72c'
    news_api = NewsAPI(api_key)

    while True:
        print("\nMenu:")
        print("1. Obtener titulares")
        print("2. Buscar noticias")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            country = input("Ingrese el código de país (ej. us, es): ").strip().lower()
            if not validate_country_code(country):
                print("Código de país no válido. Intente de nuevo.")
                continue
            try:
                articles = news_api.get_top_headlines(country)
                for article in articles:
                    print(f'Title: {article["title"]}')
                save_news_to_json(articles)
                print(f'Se han guardado {len(articles)} artículos en news.json')
            except Exception as e:
                print(e)

        elif choice == '2':
            query = input("Ingrese la búsqueda: ")
            try:
                articles = news_api.search_news(query)
                filtered_articles = list(filter(lambda x: query.lower() in x['title'].lower(), articles))
                for article in filtered_articles:
                    print(f'Title: {article["title"]}')
                save_news_to_json(filtered_articles)
                print(f'Se han guardado {len(filtered_articles)} artículos en news.json')
            except Exception as e:
                print(e)

        elif choice == '3':
            print("Cerrando aplicación")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
