
arch = open('vuelos.txt', 'r')
linea = arch.readline().strip()

total_vuelos = 0
total_pasajeros = 0

cant_vuelos_santiago = 0
pasajeros_antof_sant = 0
cant_vuelos_antof_sant = 0

destino_mayor = ''
mayor_cant_pasajeros = -1

origen_menor = ''
menor_cant_pasajeros = 999999

cant_menor_100 = 0

while linea != '':
    items = linea.split(',')
    origen = items[0]
    destino = items[1]
    cant_pasajeros = int(items[2])

    total_vuelos += 1
    total_pasajeros += cant_pasajeros

    if destino == 'Santiago':
        cant_vuelos_santiago += 1
    if origen == 'Antofagasta' or origen == 'Santiago':
        pasajeros_antof_sant += cant_pasajeros
        cant_vuelos_antof_sant += 1
    if cant_pasajeros > mayor_cant_pasajeros:
        mayor_cant_pasajeros = cant_pasajeros
        destino_mayor = destino
    if cant_pasajeros < menor_cant_pasajeros:
        menor_cant_pasajeros = cant_pasajeros
        origen_menor = origen
    if cant_pasajeros < 100:
        cant_menor_100 += 1
    linea = arch.readline().strip()

print('Cantidad total de vuelos realizados:', total_vuelos)
print('Cantidad de vuelos realizados hacia la ciudad de Santiago:', cant_vuelos_santiago)
promedio = pasajeros_antof_sant/cant_vuelos_antof_sant
print('Promedio de pasajeros transportados en los vuelos cuyo origen fue Antofagasta o Santiago:', promedio)
print('Ciudad de destino en la que se transportaron más pasajeros:', destino_mayor)
print('Ciudad de origen en la que se transportaron menos pasajeros:', origen_menor)
porcentaje = cant_menor_100/total_vuelos
print('Porcentaje de vuelos que transportaron menos de 100 personas con respecto al total de vuelos:', porcentaje)
