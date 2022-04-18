nota1 = float(input('Ingrese nota 1: '))
nota2 = float(input('Ingrese nota 2: '))
nota3 = float(input('Ingrese nota 3: '))

sum_notas = nota1 + nota2 + nota3
promedio = sum_notas/3

if promedio <= 3.9:
    print('reprobado')
else:
    print('aprobado')
