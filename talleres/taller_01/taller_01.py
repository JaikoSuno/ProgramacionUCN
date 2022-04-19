monto_total = 0
cant_prod_5 = 0

cliente_total_mayor = ''
total_mayor = -1

cant_preferencial = 0
venta_minima = 9999999

cliente_productos_mayor = ''
mayor_productos = -1

print('Bienvenido a la librería DISC')

cliente = input('Ingrese nombre del cliente: ').capitalize()
while cliente == '':
    cliente = input('Ingrese nombre del cliente: ').capitalize()

while cliente != 'Fin':
    total_productos = 0
    tipo_cliente = -1
    while True:
        try:
            print("""
            [1] Standard
            [2] VIP
            [3] Premium
            [4] Preferencial
            [5] Magnum
            """)
            tipo_cliente = int(input('Ingrese tipo de cliente: '))
            if not 1 <= tipo_cliente <= 5:
                print('[!] Error: producto u opcion no valida')
        except ValueError:
            print('[!] Error: producto u opcion no valida')
            continue

    if tipo_cliente == 4:
        cant_preferencial += 1

    subtotal = 0
    producto = -1
    while producto != 6:
        try:
            print("""
                [1] Lapiz - $ 500
                [2] Goma - $ 300
                [3] Papel Lustre - $ 1200
                [4] Carton - $ 2100
                [5] Plumon - $ 2200
                [6] Salir
                """)

            producto = int(input('Ingrese producto: '))
            if not 1 <= producto <= 6:
                print('[!] Error: producto u opcion no valida')
                continue
            
        except ValueError:
            print('[!] Error: producto u opcion no valida')
            continue

        while True:
            try:
                cantidad = int(input('Ingrese la cantidad: '))
                if cantidad <= 0:
                    print('[!] Error: valor no valido')
                    continue
                else:
                    total_productos += cantidad
            except ValueError:
                print('[!] Error: valor no valido')
                cantidad = 0
                continue

        if cantidad > 5:
            cant_prod_5 += 1

        if producto == 1:
            subtotal += 500 * cantidad
        elif producto == 2:
            subtotal += 300 * cantidad
        elif subtotal == 3:
            subtotal += 1200 * cantidad
        elif subtotal == 4:
            subtotal += 2100 * cantidad
        else:
            subtotal += 2200 * cantidad

    if total_productos > mayor_productos:
        mayor_productos = total_productos
        cliente_productos_mayor = cliente

    if subtotal > total_mayor:
        total_mayor = subtotal
        cliente_total_mayor = cliente

    iva = round(subtotal * 0.19)
    total = subtotal + iva

    while True:
        try:
            propina = int(input('Ingrese monto de la propina si lo desea: '))
            if propina < 0:
                print('[!] Error: la propina no puede ser negativa')
        except ValueError:
            print('[!] Error: Monto no valido')
            continue

    if tipo_cliente == 2:
        descuento = 0.1  # 10%
    elif tipo_cliente == 3:
        descuento = 0.15  # 15%
    elif tipo_cliente == 5:
        descuento = 0.2  # 20%
    else:
        descuento = 0

    total = total - round(total * descuento)

    if total < venta_minima:
        venta_minima = total

    monto_total += total

    cliente = input('Ingrese nombre del cliente: ').capitalize()
    while cliente == '':
        cliente = input('Ingrese nombre del cliente: ').capitalize()

print('Estadisticas Generales:')
print('Monto total vendido: $', monto_total)
print('Cantidad de productos vendidos con un precio mayor al precio promedio: No se entiende')
print('Cantidad de pedidos realizados con más de 5 productos:', cant_prod_5)
print('Cliente que realizo la mayor compra: ', cliente_total_mayor)
print('Estadisticas Personalizadas:')
print('Cantidad de clientes preferenciales:', cant_preferencial)
print('Venta minima realizada: $', venta_minima)
print('Cliente que más productos compro:', cliente_productos_mayor)
