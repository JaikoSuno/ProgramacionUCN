# Ejercicio 001

#### Contenido: Ruteo

#### Dificultad: Media

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

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=x%20%3D%20int%28input%28%22Ingrese%20en%20valor%20de%20x%3A%20%22%29%29%0An%20%3D%20int%28input%28%22Ingrese%20el%20valor%20de%20n%3A%20%22%29%29%0Ap%20%3D%20n%0Awhile%20p%20%3E%200%3A%0A%20%20%20%20p%20%3D%20p%20-%207%0Aj%20%3D%202%0Ac%20%3D%201%0Aif%20p%20%3E%200%3A%0A%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20j%20%3D%20j%20*%20i%0A%20%20%20%20print%28j%29%0Aelse%3A%0A%20%20%20%20if%20p%20%3D%3D%200%20and%20n%20%3C%2010%3A%0A%20%20%20%20%20%20%20%20p%20%3D%20True%0A%20%20%20%20%20%20%20%20while%20j%20%3E%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20j%20-%20c%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20p%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20c%20%3D%20c%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20p%20%3D%20not%20p%0A%20%20%20%20%20%20%20%20print%28p%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20z%20%3D%20int%28n/2%29%0A%20%20%20%20%20%20%20%20if%20z%20%3E%203%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20c%20*%3D%20x%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20c%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28c%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20c%20*%3D%20x%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20i%20in%20range%28n,1,-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20c%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28c%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=22&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%222%22,%227%22%5D&textReferences=true"> </iframe>
d) Responda: ¿Exista lineas de código que no se ejecutan? Si su respuesta es si, identifique las lineas ejemplo
10,11,12, etc. Si su respuesta es no, explique el porque ejemplificando con los valores de x y n.
