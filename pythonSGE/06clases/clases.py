# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        # Atributos
        self.nombre = nombre
        self.edad = edad

    # Método para mostrar la información de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 30)
persona1.mostrar_informacion()  # Salida: Nombre: Juan, Edad: 30
