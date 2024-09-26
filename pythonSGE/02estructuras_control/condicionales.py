a = 3
b = 1

# IF
if a < b:
    print("a es menor que b")
elif a > b:
    print("a es mayor que b")
else:
    print("deben ser iguales porque no se cumple ninguna condicion...")

# CASE
error = input('Introduzca un código de error:\n')

match error:
    case "200":
        print('Todo ok.')
    case "301":
        print('Movimiento permanente de la página.')
    case "302":
        print('Movimiento temporal de la página.')
    case "404":
        print('Página no encontrada.')
    case "500":
        print('Error interno del servidor.')
    case "503":
        print('Servicio no disponible.')
    case _:
        print('Error no disponible.')

