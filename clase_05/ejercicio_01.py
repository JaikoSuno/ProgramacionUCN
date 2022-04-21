lista_ciudades = []
lista_milimetros = []

ciudad = input('Ingrese nombre de la ciudad: ').capitalize()
while ciudad != 'Fin':
    milimetros = float(input('Ingrese los milimetros caidos: '))

    if ciudad not in lista_ciudades:
        lista_ciudades.append(ciudad)
        lista_milimetros.append(milimetros)
    else:
        pos = lista_ciudades.index(ciudad)
        lista_milimetros[pos] += milimetros

    ciudad = input('Ingrese nombre de la ciudad: ').capitalize()

# Ciudad que tiene mas milimetros de lluvia caidos
ciudad_mayor = ''
mayor_mili = -1

for i in range(len(lista_ciudades)):
    if lista_milimetros[i] > mayor_mili:
        mayor_mili = lista_milimetros[i]
        ciudad_mayor = lista_ciudades[i]
print('La ciudad que tiene mas milimetros de lluvia caidos es:', ciudad_mayor)

# Cantidad de ciudades con mas de 10mm.
cant_ciudades_10mm = 0
for i in range(len(lista_ciudades)):
    if lista_milimetros[i] > 10:
        cant_ciudades_10mm += 1
print('Cantidad de ciudades con mas de 10 mm:', cant_ciudades_10mm)

# Cantidad de agua caida en Antofagasta
pos_antofagasta = lista_ciudades.index('Antofagasta')
print('Cantidad de agua caida en Antofagasta:', lista_milimetros[pos_antofagasta])