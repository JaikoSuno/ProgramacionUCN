arch_inventario = open('inventario.txt', 'r')
linea = arch_inventario.readline().strip()
while linea != '':
    items = linea.split(';')
    isbn = items[0]
    titulo = items[1]
    copias = int(items[2])
    valor = int(items[3])
    linea = arch_inventario.readline().strip()
arch_inventario.close()

arch_libros = open('libros.txt', 'r')
linea = arch_libros.readline().strip()
while linea != '':
    items = linea.split(';')
    isbn = items[0]
    titulo = items[1]
    tipo = items[2]
    copias = int(items[3])

    linea = arch_libros.readline().strip()
arch_libros.close()
