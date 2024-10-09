"""
TÍTULO DEL PROGRAMA: Ejercicio de excepciones
"""

# Creación de clase personalizada para lanzar una excepción específica cuando se detecta un tipo de dato incorrecto
class StrTypeError(Exception):
    pass

# Función para procesar una lista de parámetros y realizar operaciones
def process_params(parameters: list):

    if len(parameters) < 3:
        # Se lanza una excepción de tipo IndexError si la lista tiene menos de 3 elementos
        raise IndexError()
    elif parameters[1] == 0:
        # Se lanza una excepción de tipo ZeroDivisionError si el segundo elemento es 0 (para evitar la división entre cero)
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        # Se lanza la excepción personalizada StrTypeError si el tercer elemento es una cadena de texto
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto")

    # Imprime el tercer elemento de la lista
    print(parameters[2])
    # Imprime el resultado de la división del primer elemento por el segundo
    print(parameters[0] / parameters[1])
    # Intenta sumar 5 al tercer elemento, esto solo funcionará si es un número
    print(parameters[2] + 5)

# Bloque try para capturar y manejar posibles excepciones durante la ejecución de process_params
try:
    process_params([23, 2, 2, 45]) # Ejemplo de lista de parámetros con la que se llama a la función
except IndexError as e:
    # Captura la excepción IndexError si la lista tiene menos de 3 elementos
    print("La lista debe tener más de 2 elementos")
except ZeroDivisionError as e:
    # Captura la excepción ZeroDivisionError si el segundo elemento de la lista es 0
    print("El segundo elemento de la lista no puede ser cero")
except StrTypeError as e:
    # Captura la excepción personalizada StrTypeError si el tercer elemento es una cadena de texto
    print(f"{e}")
except Exception as e:
    # Captura cualquier otra excepción no anticipada
    print(f"Se ha producido un error inesperado: {e}")
else:
    # Se ejecuta si no se lanza ninguna excepción
    print("No se ha producido ningún error")
finally:
    # Este bloque se ejecuta siempre, independientemente de si ocurrió o no una excepción
    print("El programa finaliza sin detenerse")

# Indica el final del programa
print("Fin del programa")
