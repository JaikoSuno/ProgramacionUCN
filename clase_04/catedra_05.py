arch = open('text.txt', 'r')
lineas = arch.read()
arch.close()

word = input('Ingrese una palabra a buscar (ENTER para finalizar): ')
while word != '':
    if word in lineas:
        print('Logrado')
    else:
        print('No se encuentra la palabra ingresada')

    word = input('Ingrese una palabra a buscar (ENTER para finalizar): ')
