import json
import os

# Función para crear un fichero JSON
def create_json_file():
    data = {
        "Nombre": "Juan Pérez",
        "Edad": 30,
        "Fecha_nacimiento": "1994-05-10",
        "Módulos": ["Programación", "Base de Datos", "Sistemas"]
    }
    with open('datos.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Clase que representa a una persona
class Person:
    def __init__(self, nombre, edad, fecha_nacimiento, modulos):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.modulos = modulos

# Función principal para ejecutar la lógica
def main():
    create_json_file()  # Crear el fichero JSON

    # Leer los datos del fichero JSON y crear un objeto Person
    with open('datos.json', 'r') as json_file:
        data = json.load(json_file)
        person = Person(data['Nombre'], data['Edad'], data['Fecha_nacimiento'], data['Módulos'])

    # Mostrar los atributos de la instancia de la clase
    print(f"Nombre: {person.nombre}")
    print(f"Edad: {person.edad}")
    print(f"Fecha de Nacimiento: {person.fecha_nacimiento}")
    print(f"Módulos: {', '.join(person.modulos)}")

    # Borrar el fichero JSON
    os.remove('datos.json')
    print("Fichero JSON borrado.")

if __name__ == "__main__":
    main()
