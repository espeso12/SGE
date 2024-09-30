"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocando a la función tantas veces como sea necesario.

Hacen el código más legible....

Sintaxis:

def nombre_funcion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombre_funcion(mi_parametro)
"""

"""
*********Funciones básicas: definidas por el usuario******
"""


# Funciones simples: ejecutar todo el código dentro de la propia función

# Definir función
def greet():
    print("Hola!!!, bienvenidos al curso 24/25")


# Invocar función
greet()


# Funciones con retorno:

# Definir función
def return_greet():
    return "Hola!!!, bienvenidos de nuevo al curso 24/25"


# Invocar función
"""Se puede capturar el return en una variable para después imprimirlo:
greet_func = return_greet()
print(greet_func)

Otra opción sería imprimir directamente, sin guardar el return en una variable"""

print(return_greet())


# Función con un argumento: se puede pasar un parámetro a la función para operar con él:
def arg_greet(name):
    print(f"Hola, {name}")


arg_greet("pepito")


# Función con varios argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}")


args_greet("Hi", "pepito")


# Valores por defecto en los parámetros: ejemplo con un argumento predeterminado:
def default_arg_greet(name="Python"):
    print(f"Hola, {name}")


default_arg_greet()  # se puede llamar a la función sin argumentos
default_arg_greet("Pedro")


# Función con varios argumentos posicionales
def args_greet(greet, name):
    print(f"{greet}, {name}")


args_greet(name="Pepito", greet="Hi")


# Función con retorno de varios valores
def multiple_return_greet():
    return "Bienvenidos", "chicos"  # retorna 2 cadenas de texto


greet, name = multiple_return_greet()
print(greet)
print(name)


# Funciones con un número variable de argumentos
def variable_arg_greet(*names):  # significa que podemos pasar más de un nombre, separado por comas
    for name in names:
        print(f"Buenos días, {name}")


variable_arg_greet("Uno", "Dos", "Tres")


# Funciones con un número variable de argumentos con palabra clave
# Los ** significan que cada argumento está formado por una clave y un valor

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Datos: {value} ({key})")


variable_key_arg_greet(
    language="Python",
    year=2024,
    center="Ribera",
    subject="SGE"

)

"""
Funciones dentro de funciones
"""


def outer_function():
    def inner_function():
        print("Hola desde la función interna!!!")

    inner_function()  # es necesario poner esta llamada para ejecutar la función inner_function()


outer_function()

"""
**********Funciones del lenguaje (built-in)***************
"""
# self es una palabra reservada en Python; hace referencia a la propia instancia donde se está ejecutando
print(len("cuentanumeroletras"))
print(type(23))  # muestra el tipo de dato que se le pasa
print("hola".upper())  # upper es una función asociada a la cadena de texto

"""
***********Variables locales y globales*****************
"""

# Ámbito o scope:

# Variable global:

global_example = "Ejemplo de variable global"

print(global_example)


def greet_global():
    print(f"Esto es un: {global_example}")


greet_global()

# Variable local: funciona sólo dentro del ámbito de la función

global_example = "Ejemplo de variable global"

print(global_example)


def greet_local():
    local_example = "Ejemplo de variable local"
    print(f"{local_example}; {global_example}")


greet_local()
# print(local_example); esto daría un error

# Recomendable: restringir al máximo el ámbito del código


