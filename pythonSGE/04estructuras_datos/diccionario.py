d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)

# Acceder
print(d1['Nombre'])
print(d1.get('Nombre'))

# Modificar
d1['Nombre'] = "Pedro"
print(d1)

# Eliminar
del d1['Nombre']
print(d1)