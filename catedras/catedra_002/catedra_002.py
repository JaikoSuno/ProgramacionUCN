total_vacunados = 0
cant_primera = 0
cant_segunda = 0

cant_sinovac = 0
cant_pfizer = 0

nombre = input('Ingrese el nombre del usuario: ')
while nombre != '-1':

    dosis = input('Ingrese si es primera o segunda dosis (1 o 2): ').lower()
    while dosis != '1' and dosis != '2':
        dosis = input('Ingrese si es primera o segunda dosis (1 o 2): ').lower()

    tipo_vacuna = input('Ingrese tipo de vacuna (pfizer o sinovac): ').lower()
    while tipo_vacuna != 'pfizer' and tipo_vacuna != 'sinovac':
        tipo_vacuna = input('Ingrese tipo de vacuna (pfizer o sinovac): ').lower()

    alergia = input('¿Posee alguna alergia? (si o no): ').lower()
    while alergia != 'si' and alergia != 'no':
        alergia = input('¿Posee alguna alergia? (si o no): ').lower()

    total_vacunados += 1

    if dosis == '1':
        cant_primera += 1
    else:
        cant_segunda += 1

    if tipo_vacuna == 'sinovac':
        cant_sinovac += 1
    else:
        cant_pfizer += 1

    nombre = input('Ingrese el nombre del usuario: ')

print('Cantidad total de vacunados:', total_vacunados)

try:
    print('Porcentaje de personas con primera dosis:', (cant_primera / total_vacunados) * 100, '%')
    print('Porcentaje de personas con segunda dosis:', (cant_segunda / total_vacunados) * 100, '%')
except ZeroDivisionError:
    print('Porcentaje de personas con primera dosis: 0 %')
    print('Porcentaje de personas con segunda dosis: 0 %')

if cant_pfizer > cant_sinovac:
    print('Pfizer es la vacuna mas suministrada con', cant_pfizer)
elif cant_pfizer < cant_sinovac:
    print('Sinovac es la vacuna mas suministrada con', cant_pfizer)
else:
    print('Ambas vacunas tienen la misma cantidad de vacunaciones suministradas')