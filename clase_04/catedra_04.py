total_albumes = 0
total_canciones = 0
sum_canciones = 0
album_menor_15 = ''

menor_total_canciones = 99999

arch = open('albumes.txt', 'r')
linea = arch.readline().strip()

while linea != '':
    items = linea.split(',')
    nombre = items[0]
    cant_canciones = int(items[1])
    precio = int(items[2])
    total_albumes += 1
    sum_canciones += cant_canciones

    if cant_canciones < 15 and precio <= 10000:
        album_menor_15 = nombre

    if cant_canciones < menor_total_canciones:
        menor_total_canciones = cant_canciones

    linea = arch.readline().strip()
arch.close()

if total_albumes != 0:
    print('Hay', total_albumes, 'albumes en total')
    print('Cantidad de promedio de canciones:', sum_canciones / total_albumes)
    if album_menor_15 != '':
        print(album_menor_15, 'posee menos de 15 canciones y su precio es inferior o igual a $10000')
    else:
        print('No existe ningun album que posee menos de 15 canciones y su precio es inferior o igual a $10000')
    porcentaje = menor_total_canciones / sum_canciones
    print('Canciones del album con el menor precio respecto al total de canciones en total', porcentaje, '%')
    print('Canciones del album con el menor precio respecto al total de canciones en total: 0 %')
else:
    print('No hay registros')
