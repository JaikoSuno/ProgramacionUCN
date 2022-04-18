nombre_1 = input('Ingrese nombre (1era persona): ')
mes_1 = int(input('Ingrese mes (numero) de nacimiento: '))
anio_1 = int(input('Ingrese año de nacimiento: '))

nombre_2 = input('Ingrese nombre (2da persona): ')
mes_2 = int(input('Ingrese mes (numero) de nacimiento: '))
anio_2 = int(input('Ingrese año de nacimiento: '))

if mes_1 == mes_2 and anio_1 == anio_2:
    print('Wow,', nombre_1, 'y', nombre_2, 'cumplen el mismo mes y año')
elif mes_1 == mes_2:
    if anio_1 > anio_2:
        print('Cumplen el mismo mes, pero', nombre_2, 'es mas experimentado que', nombre_1)
    else:
        print('Cumplen el mismo mes, pero', nombre_1, 'es mas experimentado que', nombre_2)
elif anio_1 == anio_2:
    mes_cnt = abs(mes_2 - mes_1)
    print(nombre_1, 'y', nombre_2, 'tiene edades muy similares, pero con', mes_cnt, 'meses de diferencia')
else:
    print('Sus fechas de nacimiento no estan muy relacionadas')
