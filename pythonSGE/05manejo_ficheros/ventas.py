import os

# Función para mostrar el menú
def mostrar_menu():
    print("\nGestión de Ventas")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar todos los productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")
    return input("Elige una opción: ")

# Función para añadir un producto al archivo
def añadir_producto():
    with open("ventas.txt", "a") as archivo:
        nombre = input("Introduce el nombre del producto: ")
        cantidad = input("Introduce la cantidad: ")
        precio = input("Introduce el precio: ")
        archivo.write(f"{nombre},{cantidad},{precio}\n")
    print("Producto añadido.")

# Función para consultar un producto
def consultar_producto():
    nombre_buscado = input("Introduce el nombre del producto a consultar: ")
    with open("ventas.txt", "r") as archivo:
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(",")
            if nombre == nombre_buscado:
                print(f"Producto: {nombre}, Cantidad: {cantidad}, Precio: {precio}")
                return
    print("Producto no encontrado.")

# Función para actualizar un producto
def actualizar_producto():
    nombre_buscado = input("Introduce el nombre del producto a actualizar: ")
    productos = []
    encontrado = False
    with open("ventas.txt", "r") as archivo:
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(",")
            if nombre == nombre_buscado:
                cantidad = input("Introduce la nueva cantidad: ")
                precio = input("Introduce el nuevo precio: ")
                encontrado = True
            productos.append(f"{nombre},{cantidad},{precio}\n")

    if encontrado:
        with open("ventas.txt", "w") as archivo:
            archivo.writelines(productos)
        print("Producto actualizado.")
    else:
        print("Producto no encontrado.")

# Función para borrar un producto
def borrar_producto():
    nombre_buscado = input("Introduce el nombre del producto a borrar: ")
    productos = []
    encontrado = False
    with open("ventas.txt", "r") as archivo:
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(",")
            if nombre != nombre_buscado:
                productos.append(f"{nombre},{cantidad},{precio}\n")
            else:
                encontrado = True

    if encontrado:
        with open("ventas.txt", "w") as archivo:
            archivo.writelines(productos)
        print("Producto borrado.")
    else:
        print("Producto no encontrado.")

# Función para mostrar todos los productos
def mostrar_todos():
    with open("ventas.txt", "r") as archivo:
        print("Productos:")
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(",")
            print(f"{nombre}: Cantidad: {cantidad}, Precio: {precio}")

# Función para calcular la venta total
def calcular_venta_total():
    total = 0
    with open("ventas.txt", "r") as archivo:
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(",")
            total += int(cantidad) * float(precio)
    print(f"Venta total: {total}")

# Función para calcular venta por producto
def calcular_venta_producto():
    nombre_buscado = input("Introduce el nombre del producto para calcular la venta: ")
    with open("ventas.txt", "r") as archivo:
        for linea in archivo:
            nombre, cantidad, precio = linea.strip().split(",")
            if nombre == nombre_buscado:
                venta = int(cantidad) * float(precio)
                print(f"Venta total para {nombre}: {venta}")
                return
    print("Producto no encontrado.")

# Programa principal
def main():
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            añadir_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            borrar_producto()
        elif opcion == "5":
            mostrar_todos()
        elif opcion == "6":
            calcular_venta_total()
        elif opcion == "7":
            calcular_venta_producto()
        elif opcion == "8":
            print("Saliendo del programa y eliminando el archivo ventas.txt...")
            if os.path.exists("ventas.txt"):
                os.remove("ventas.txt")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
