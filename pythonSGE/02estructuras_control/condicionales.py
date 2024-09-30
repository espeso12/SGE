# Estructura if
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Estructura case (Python usa match-case desde la versión 3.10)
dia = input("Introduce un día de la semana: ").lower()

match dia:
    case "lunes":
        print("Inicio de la semana")
    case "viernes":
        print("Fin de la semana")
    case _:
        print("Día común")
