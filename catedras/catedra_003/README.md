# Ejercicio 003 - Biblioteca DISC

#### Contenido: Archivos
#### Dificultad: Difícil

Una biblioteca tiene problemas para administrar sus libros debido a la gran cantidad de préstamos efectuados durante la
semana pasada. Este aumento peculiar debe ser estudiado y esto requiere la obtención de ciertos estadísticos. Para ello
se tiene un registro de los últimos préstamos y devoluciones efectuados durante la semana pasada que aún no se han
registrado en el sistema y el inventario de la biblioteca previo a esta semana ajetreada.
En el archivo “libros.txt” se almacenan todos los prestamos y devoluciones efectuados por los clientes durante la semana
a tratar, mientras que dentro del archivo “inventario.txt” se almacena el inventario anterior a la semana considerada. El
formato de esta información es, para cada archivo respectivamente: 

<center>(código ISBN;titulo;tipo;copias)</center>
<center>(código ISBN,titulo,copias,valor)</center>

Donde “código ISBN” corresponde al código identificador del libro, “título” es literalmente el título del libro, “tipo”
corresponde textualmente a “PRE” o “DEV” en caso de un préstamo o una devolución respectivamente, “copias” en el
archivo “libros.txt” corresponde a la cantidad de copias que fueron prestadas o devueltas del libro en específico, mientras
que en el archivo “inventario.txt” representa la cantidad de ejemplares disponibles en bodega (registrados en el inventario)
y, “valor” corresponde al precio de venta de cada ejemplar de este libro. 

**Nota: Las ventas de libros son realizadas en otro sistema el cual es completamente aparte del sistema de
préstamos y devoluciones.**

Lo que se requiere que haga el sistema es:

1. Indicar el total de préstamos y devoluciones registrados durante la semana pasada.
2. Determinar el total de libros pendientes por devolver considerando que a inicios de la semana pasada (antes de
registrar lo del archivo “libros.txt”) habían 10 libros pendientes por devolver.
3. Para el inventario del archivo “inventario.txt” determinar el valor promedio de un libro dentro del inventario (Ej: si
se cuenta con una copia de un libro de valor 70 y dos copias de un libro de valor 10, entonces el valor promedio
por libro dentro del inventario es de 30)
4. Para únicamente el libro de mayor valor y el libro de menor valor dentro del inventario determinar el porcentaje
de préstamos efectuados respecto del total que había disponible dentro del inventario, es decir, el porcentaje en
el cual fue reducida la cantidad de ejemplares de estos libros dentro del inventario.
5. Se desea señalar todos los cambios a realizar en el inventario para el libro “Fundamentos de la Computación”,
indicando la disponibilidad previa en el inventario, la cantidad total de préstamos y devoluciones para este libro,
el valor previo y actual del inventario.