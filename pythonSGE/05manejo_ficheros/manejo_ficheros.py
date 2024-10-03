import os

# Crear un archivo de texto y escribir datos usando 'with' para el manejo seguro
with open("datos.txt", "w") as archivo:
    archivo.write("Nombre: Juan\n")
    archivo.write("Edad: 30\n")
    archivo.write("Lenguaje de programación: Python\n")

# Leer el contenido del archivo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# Eliminar el archivo al final
if os.path.exists("datos.txt"):
    os.remove("datos.txt")
    print("Archivo eliminado.")
else:
    print("El archivo no existe.")
