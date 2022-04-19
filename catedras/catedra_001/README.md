# Ejercicio 001

#### Contenido: Ruteo

Rutee manualmente el siguiente código e indique el valor que van tomando las variables. Para ello considere que:
* Debe identificar todas las variables en el código para las diversas preguntas solicitadas.
* Para cada variable identificada, anote el nombre de la variable y los valores que va tomando la variable a lo largo
del código.
* Solo anote los valores que toma la variable al cambiar.
* Si la variable no cambia su valor no es necesario repetir el valor a cada momento.
* Escriba hacia abajo los valores que van tomando las variables a medida que cambian en el tiempo.

Ejemplo.

<center>X</center>
<center>2</center>
<center>4</center>
<center>6</center>
<center>12</center>

Nota: Debe rutear el código SIN USAR SPYDER O CUALQUIER OTRO PROGRAMA. Si es sorprendido usando un programa
para responder este ejercicio será sancionado.

a) Que valores toman las variables si x=2 y n=7

b) Que valores toman las variables si x=23 y n=9

c) Que valores toman las variables si x=3 y n=2
d) Responda: ¿Exista lineas de código que no se ejecutan? Si su respuesta es si, identifique las lineas ejemplo
10,11,12, etc. Si su respuesta es no, explique el porque ejemplificando con los valores de x y n.

Código:
`````python
x = int(input("Ingrese en valor de x: "))
n = int(input("Ingrese el valor de n: "))
p = n
while p > 0:
    p = p - 7
j = 2
c = 1
if p > 0:
    for i in range(n):
        j = j * i
    print(j)
else:
    if p == 0 and n < 10:
        p = True
        while j > 0:
            j = j - c
            if p:
                c = c + 1
            p = not p
        print(p)
    else:
        z = int(n/2)
        if z > 3:
            c *= x
            for i in range(n):
                c += 1
                print(c)
        else:
            c *= x
            for i in range(n,1,-1):
                c += 1
                print(c)
`````

NOTA: Para ver las lineas de código o el codigo como tal, [ver aquí](catedra_001.py)

# Solución

a) Que valores toman las variables si x=2 y n=7

|  x  |  y  |  p  |  j  |  c  |  z  |
|:---:|:---:|:---:|:---:|:---:|:---:|
|  1  |  2  |  1  |     |     |     |
|  2  |  3  | 22  |     |     |     |
|  3  |  4  |  3  |     |     |     |

b) Que valores toman las variables si x=23 y n=9

|  x  |  y  |  p  |  j  |  c  |  z  |
|:---:|:---:|:---:|:---:|:---:|:---:|
|  1  |  2  |  1  |     |     |     |
|  2  |  3  | 22  |     |     |     |
|  3  |  4  |  3  |     |     |     |
c) Que valores toman las variables si x=3 y n=2

|  x  |  y  |  p  |  j  |  c  |  z  |
|:---:|:---:|:---:|:---:|:---:|:---:|
|  1  |  2  |  1  |     |     |     |
|  2  |  3  | 22  |     |     |     |
|  3  |  4  |  3  |     |     |     |

d) Responda: ¿Exista lineas de código que no se ejecutan? Si su respuesta es si, identifique las lineas ejemplo
10,11,12, etc. Si su respuesta es no, explique el porque ejemplificando con los valores de x y n.
