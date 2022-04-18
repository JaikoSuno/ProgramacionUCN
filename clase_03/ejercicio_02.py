ciudad_mas_empleados = ''  # Nombre de la ciudad con más empleados
mayor_cant_empleados = 0  # El mayor número de empleados encontrado

nombre_empleado_mayor_edad = ''  # Nombre del empleado de mayor edad entre todas las sucursales
mayor_edad_empleado = 0  # Edad más alta encontrada

cant_emp_25_30 = 0  # Cantidad de empleados entre 25 y 30 años de edad
total_emp = 0  # total de empleados (todas las sucursales)

nombre_empleado_33 = ''  # Nombre del empleado que tiene 33 años
sucursal_empleado_33 = ''  # Sucursal del empleado que tiene 33 años

ciudad_min_ponderacion = ''  # Ciudad con menor ponderacion
min_ponderacion = 999999  # Ponderacion minima calculada hasta ahora

arch = open('sucursales.txt', 'r')
line = arch.readline().strip()
while line != '':
    items = line.split(',')
    ciudad = items[0]
    cant_empleados = int(items[1])

    total_emp += cant_empleados

    if cant_empleados > mayor_cant_empleados:
        mayor_cant_empleados = cant_empleados
        ciudad_mas_empleados = ciudad

    sum_edad = 0
    for emp in range(cant_empleados):
        line = arch.readline().strip()
        items2 = line.split(',')
        nombre = items2[0]
        edad = int(items2[1])
        sum_edad += edad
        if edad > mayor_edad_empleado:
            nombre_empleado_mayor_edad = nombre
            mayor_edad_empleado = edad

        if 25 <= edad <= 30:
            cant_emp_25_30 += 1

        if edad == 33:
            nombre_empleado_33 = nombre
            sucursal_empleado_33 = ciudad
    promedio_edad = sum_edad / cant_empleados
    ponderacion = cant_empleados * 10 + promedio_edad * 0.5

    if ponderacion < min_ponderacion:
        min_ponderacion = ponderacion
        ciudad_min_ponderacion = ciudad

    print('El promedio de edad de la sucursal', ciudad, 'es:', promedio_edad)

    line = arch.readline().strip()

print('Nombre de la sucursal que tiene la mayor cantidad de empleados:', ciudad_mas_empleados)
print('Nombre del empleado con la edad mayor entre todas las sucursales', nombre_empleado_mayor_edad)
print('Porcentaje de empleados cuya edad se encuentra entre 25 y 30 años (ambos inclusive):', cant_emp_25_30/total_emp)
print('El nombre del empleado que tiene 33 años es', nombre_empleado_33, 'de la sucursal de', sucursal_empleado_33)
print('Sucursal con la menor ponderacion:', ciudad_min_ponderacion)
