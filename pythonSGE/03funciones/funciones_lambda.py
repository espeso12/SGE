"""
Las funciones lambda o anónimas son un tipo de funciones en Python
que típicamente se definen en una línea y cuyo código a ejecutar suele ser pequeño.

Normal:
def suma(a, b):
    return a+b

"""
# Definición y almacenamiento en variable
suma = lambda a, b : a + b
print(suma(5, 6))

# Declarar y llamar en la misma línea
print((lambda a, b: a + b)(2, 4))

