total_infractores = 0
sum_edad_infractores = 0
sum_mascotas_no_inscritas = 0

nombre_mayor_no_inscrito = ''
mayor_no_inscrito = -1

nombre_menor_no_inscrito = ''
menor_no_inscrito = 999999

nombre_mayor_edad = ''
mayor_edad = -1

recaudacion_total = 0

arch = open('datos.txt', 'r')
linea = arch.readline().strip()

while linea != '':
    items = linea.split(',')
    nombre = items[0]
    edad = int(items[1])
    cant_mascotas = int(items[2])
    cant_mascotas_reales = int(items[3])

    # Es infractor
    if cant_mascotas < cant_mascotas_reales:
        total_infractores += 1
        sum_edad_infractores += edad
        cant_no_inscritos = cant_mascotas_reales - cant_mascotas
        sum_mascotas_no_inscritas += cant_no_inscritos
        recaudacion_total += cant_no_inscritos * 30000

        if cant_no_inscritos > mayor_no_inscrito:
            mayor_no_inscrito = cant_no_inscritos
            nombre_mayor_no_inscrito = nombre

        if cant_no_inscritos < menor_no_inscrito:
            menor_no_inscrito = cant_no_inscritos
            nombre_menor_no_inscrito = nombre
    else:
        # No es infractor
        if edad > mayor_edad:
            mayor_edad = edad
            nombre_mayor_edad = nombre

    linea = arch.readline().strip()

print('Cantidad total de infractores a la ley:', total_infractores)

try:
    print('Promedio de edad de los infractores:', sum_edad_infractores / total_infractores)
except ZeroDivisionError:
    print('Promedio de edad de los infractores: 0')

try:
    prom_mascotas_no_inscritas = sum_mascotas_no_inscritas / total_infractores
    print('Promedio de mascotas no inscritas entre todos los infractores:', prom_mascotas_no_inscritas)
except ZeroDivisionError:
    print('Promedio de mascotas no inscritas entre todos los infractores: 0')

print('Nombre del dueño con el mayor numero de mascotas no inscritas:', nombre_mayor_no_inscrito)
print('Nombre del dueño con el menor numero de mascotas no inscritas:', nombre_menor_no_inscrito)
print('Nombre de la persona con mas edad entre los dueños no infractores:', nombre_mayor_edad)
print('Recaudacion total en multas: $', recaudacion_total)
