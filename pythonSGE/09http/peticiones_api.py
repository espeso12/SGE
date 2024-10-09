"""
Definiciones importantes:

- API: Es un conjunto de reglas y herramientas que permiten a las aplicaciones interactuar entre sí.
Una API define cómo los diferentes componentes de software deben interactuar y compartir datos.

- API RESTful: Es una API que sigue los principios de REST, donde los recursos están definidos a
través de URLs, y se puede interactuar con ellos usando los métodos HTTP: GET, POST, PUT, DELETE.

- Endpoint: Es la URL que permite acceder a un recurso específico de la API. Cada endpoint
representa una dirección a la que se puede hacer una petición para obtener o manipular datos. En el
caso de PokeAPI, los endpoints permiten acceder a información sobre los diferentes Pokémon.
"""

import requests

# Función para obtener información de un Pokémon por su nombre o número
def obtener_info_pokemon(pokemon):
    # Asegurarse de que el nombre esté en minúsculas
    pokemon = pokemon.lower()

    # URL del endpoint de la API para obtener la información del Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"

    # Realizar la petición HTTP GET
    response = requests.get(url)

    # Verificar si la petición fue exitosa
    if response.status_code == 200:
        data = response.json()  # Convertir la respuesta a formato JSON

        # Mostrar los datos del Pokémon
        print(f"Nombre: {data['name']}")
        print(f"ID: {data['id']}")
        print(f"Peso: {data['weight']}")
        print(f"Altura: {data['height']}")

        # Mostrar los tipos de Pokémon
        tipos = [tipo['type']['name'] for tipo in data['types']]
        print(f"Tipos: {', '.join(tipos)}")

    elif response.status_code == 404:
        print(f"El Pokémon '{pokemon}' no fue encontrado. Verifica el nombre o número.")
    else:
        print(f"Error al realizar la petición. Código de estado: {response.status_code}")


# Solicitar al usuario el nombre o número del Pokémon
nombre = input("Introduce el nombre o número del Pokémon: ")
obtener_info_pokemon(nombre)
