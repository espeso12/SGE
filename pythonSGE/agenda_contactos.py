# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nAgenda de Contactos")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")
    return input("Elige una opción: ")


# Función para buscar un contacto por nombre
def buscar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a buscar: ").lower()
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print("Contacto no encontrado")


# Función para insertar un nuevo contacto
def insertar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto: ").lower()
    if nombre in agenda:
        print("El contacto ya existe.")
    else:
        telefono = input("Introduce el número de teléfono (9 dígitos): ")
        if telefono.isdigit() and len(telefono) == 9:
            agenda[nombre] = telefono
            print("Contacto añadido correctamente.")
        else:
            print("Número de teléfono no válido. Debe tener 9 dígitos y ser numérico.")


# Función para actualizar un contacto existente
def actualizar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a actualizar: ").lower()
    if nombre in agenda:
        telefono = input("Introduce el nuevo número de teléfono (9 dígitos): ")
        if telefono.isdigit() and len(telefono) == 9:
            agenda[nombre] = telefono
            print("Contacto actualizado correctamente.")
        else:
            print("Número de teléfono no válido.")
    else:
        print("Contacto no encontrado.")


# Función para eliminar un contacto
def eliminar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a eliminar: ").lower()
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado.")
    else:
        print("Contacto no encontrado.")


# Función para mostrar todos los contactos en orden ascendente
def mostrar_todos(agenda):
    if agenda:
        print("\nContactos en la agenda:")
        for nombre in sorted(agenda):
            print(f"{nombre}: {agenda[nombre]}")
    else:
        print("La agenda está vacía.")


# Programa principal
def main():
    agenda = {}  # Diccionario vacío para guardar los contactos

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            buscar_contacto(agenda)
        elif opcion == "2":
            insertar_contacto(agenda)
        elif opcion == "3":
            actualizar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            mostrar_todos(agenda)
        elif opcion == "6":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
