valor = float(input('Ingrese un valor: '))

unidad = input('Ingrese la unidad: ')
while unidad != "km" and unidad != "m" and unidad != "cm":
    print('[!] Error: unidad no valida, ingrese nuevamente')
    unidad = input('Ingrese la unidad: ')

unidad_convertir = input('Ingrese la unidad a convertir: ')
while unidad_convertir != "km" and unidad_convertir != "m" and unidad_convertir != "cm":
    print('[!] Error: unidad no valida, ingrese nuevamente')
    unidad_convertir = input('Ingrese la unidad a convertir: ')

if unidad == 'cm':
    if unidad_convertir == 'm':
        resultado = valor / 100
    elif unidad_convertir == 'km':
        resultado = valor / 100000
    else:
        resultado = valor
elif unidad == 'm':
    if unidad_convertir == 'cm':
        resultado = valor * 100
    elif unidad_convertir == 'km':
        resultado = valor / 1000
    else:
        resultado = valor
else:
    if unidad_convertir == 'cm':
        resultado = valor * 100000
    elif unidad_convertir == 'm':
        resultado = valor * 1000
    else:
        resultado = valor

print(valor, unidad, 'equivalen a ', resultado, unidad_convertir)
