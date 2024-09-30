try:
    num = int(input("Introduce un número: "))
    print(f"Has introducido el número {num}")
except ValueError:
    print("Eso no es un número válido")
