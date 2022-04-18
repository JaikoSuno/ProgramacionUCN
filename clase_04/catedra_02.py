cliente_mayor = ''
mayor_kilos = -1
mayor_tipo_alimento = ''

cliente_menor = ''
menor_kilos = 999999
menor_tipo_alimento = ''

cant_purina = 0
kilos_purina = 0

cant_otro_alimento = 0
total_alimentos = 0

# Validar que el nombre no sea un texto vacio
nombre = input('Ingrese nombre del cliente: ').lower()
while nombre == '':
    nombre = input('Ingrese nombre del cliente: ').lower()

while nombre != 'fin':
    # Validar que el tipo de alimento solo sea gato, perro u otro.
    tipo_alimento = input('Ingrese tipo de alimento (perro, gato, otro): ').lower()
    while tipo_alimento != 'perro' and tipo_alimento != 'gato' and tipo_alimento != 'otro':
        tipo_alimento = input('Ingrese tipo de alimento (perro, gato, otro): ').lower()

    if tipo_alimento == 'otro':
        cant_otro_alimento += 1

    # Validar la marca para el tipo de alimento de gatos
    if tipo_alimento == 'gato':
        marca = input('Ingrese la marca de alimentos a llevar (Purina o MasterCat): ').lower()
        while marca != 'purina' and marca != 'mastercat':
            marca = input('Ingrese la marca de alimentos a llevar (Purina o MasterCat): ').lower()
    else:
        marca = input('Ingrese la marca de alimentos a llevar: ').lower()
        while marca == '':
            marca = input('Ingrese la marca de alimentos a llevar: ').lower()

    # Validar que la cantidad de kilos sea correcta
    while True:
        try:
            cant_kilos = float(input('Ingrese la cantidad de kilos a llevar: '))
            break
        except ValueError:
            print('Error: Ingrese nuevamente la cantidad de kilos')

    if cant_kilos > mayor_kilos:
        mayor_kilos = cant_kilos
        cliente_mayor = nombre
        mayor_tipo_alimento = tipo_alimento

    if cant_kilos < menor_kilos:
        menor_kilos = cant_kilos
        cliente_menor = nombre
        menor_tipo_alimento = tipo_alimento

    if tipo_alimento == 'gato' and marca == 'purina':
        cant_purina += 1
        kilos_purina += cant_kilos

    total_alimentos += 1

    # Validar que el nombre no sea un texto vacio
    nombre = input('Ingrese nombre del cliente: ').lower()
    while nombre == '':
        nombre = input('Ingrese nombre del cliente: ').lower()

print(cliente_mayor, 'compro mas kilos para', mayor_tipo_alimento, 'con', mayor_kilos, 'kg')
print(cliente_menor, 'compro menos kilos para', menor_tipo_alimento, 'con', menor_kilos, 'kg')
promedio = kilos_purina / cant_purina
print('El promedio de kilos de alimento para gatos de la marca purina comprados:', promedio)
porcentaje = cant_otro_alimento / total_alimentos
print('Porcentaje de la cantidad de veces que se compro otro tipo de alimento, respecto al total:', porcentaje, '%')


