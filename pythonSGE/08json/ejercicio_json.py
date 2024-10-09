"""
Información sobre ficheros JSON:
- Definición: JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero y fácil de leer/escribir para humanos y máquinas. Se utiliza comúnmente para enviar datos entre un servidor y una aplicación web.
- Elementos: Los elementos en un fichero JSON incluyen objetos (con llaves `{}`) que contienen pares de clave-valor y listas (con corchetes `[]`) que pueden contener múltiples valores.
- Características: Es un formato textual, independiente del lenguaje, y soporta estructuras de datos como objetos y arrays.
- Usos principales: Se utiliza en APIs, almacenamiento de datos, configuración de aplicaciones, y en la transmisión de información entre cliente y servidor.
"""

import json
import os

# Datos a guardar en el fichero JSON
data = {
    "Nombre": "Juan Pérez",
    "Edad": 30,
    "Fecha_nacimiento": "1994-05-10",
    "Módulos": ["Programación", "Base de Datos", "Sistemas"]
}

# Crear un fichero JSON y guardar los datos
with open('datos.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  # Usar indentación para mejorar la legibilidad

# Mostrar el contenido del fichero JSON
with open('datos.json', 'r') as json_file:
    content = json_file.read()
    print("Contenido del fichero JSON:")
    print(content)

# Borrar el fichero JSON
os.remove('datos.json')
print("Fichero JSON borrado.")
