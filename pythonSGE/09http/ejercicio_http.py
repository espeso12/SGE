"""
Conceptos importantes:

- Servicio web: Un servicio web es un sistema que permite la comunicación entre dispositivos a
través de la red utilizando protocolos estándar, como HTTP. Permiten el intercambio de datos entre
aplicaciones.

- RESTful API: Una API REST (Representational State Transfer) es un conjunto de funciones que
permite a los desarrolladores realizar peticiones y recibir respuestas a través de HTTP. Las API
RESTful son aquellas que cumplen con las restricciones y principios REST.

- Protocolo HTTP: El Protocolo de Transferencia de Hipertexto (HTTP) es un protocolo de red que se
utiliza para la transmisión de información en la web. Es el protocolo principal que rige la
comunicación entre un cliente (navegador) y un servidor web.

- Peticiones HTTP: Son solicitudes enviadas desde un cliente a un servidor para obtener o enviar
datos. Pueden ser de varios tipos: GET (obtener datos), POST (enviar datos), PUT (actualizar datos)
y DELETE (eliminar datos).

- Respuestas HTTP:
  - 200: OK. La petición fue exitosa y el servidor devolvió la respuesta solicitada.
  - 404: Not Found. El servidor no pudo encontrar la página solicitada.
  - 500: Internal Server Error. Se produjo un error en el servidor que impidió procesar la petición.
"""

import requests

# Realizar una petición HTTP para obtener una página web
response = requests.get("https://example.com")

# Verificar si la petición fue exitosa
if response.status_code == 200:
    print("La petición fue exitosa.")
    print("Contenido de la página:")
    print(response.text)  # Imprimir el contenido de la web
else:
    print(f"Error al realizar la petición. Código de estado: {response.status_code}")
