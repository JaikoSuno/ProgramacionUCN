# Taller 02 - Conversor de Unidades
#### Ano: 2021

Desarrolle un programa de conversor de unidades, que permita pasar distintos tipos de unidades de
distintos tipos de mediciones.

Por ejemplo, si a usted le toca convertir unidades de temperatura, masa y energía, su programa debe ser
capaz de recibir como parámetro una temperatura dada en un tipo de unidad (por ejemplo Kelvin) y convertirla
a otra unidad (por ejemplo °Fahrenheit).

El programa debe leer un archivo que tiene un formato como el siguiente:

<center>Medida, unidad_origen, unidad_destino, valor_a_convertir</center>

Un ejemplo (sólo un ejemplo) sería lo siguiente:

<center>Temperatura,Celsius,Kelvin,-25</center>
<center>Temperatura,Fahrenheit,Celsius,50</center>
<center>Masa,kg,gr,2000</center>
<center>Energia,Julio;BTU,30000</center>

El archivo de texto debe ser elaborado por usted y su compañero, debe tener al menos 20 conversiones
por realizar.

El programa primero debe leer el archivo y procesar cada conversión, entregando por pantalla el detalle
completo de cada una (medida, unidades y valores) en un formato adecuado. Luego de lo anterior debe
preguntarle al usuario si desea hacer alguna(s) conversión(es) adicional(es), y desplegarle un menú para ello.

Cada conversión para una medida distinta debe estar contenida en su propia función. Es una y sólo una
función por medida. Cada medida se debe poder convertir al menos entre 4 unidades.

Al finalizar se le debe entregar al usuario una serie de estadísticas personalizadas.

Es importante destacar que el código debe usar listas y funciones. No debe usar matrices u otras
estructuras de datos que aún no hemos visto.

Finalmente se debe escribir un archivo donde se guarde cada uno de los valores finales de las conversiones
realizadas en el siguiente formato. Debe tener todas las conversiones (del archivo y manuales):

<center>Medida,unidad_origen,unidad_destino,valor_origen,valor_destino</center>

### Condiciones de entrega
* Debe enviar el archivo en formato Python (.py) o Jupyter Notebook (.ipynb)
* Junto con la entrega debe enviar un video de máximo de 3 minutos explicando el código realizado en que ambos alumnos
hablen. Puede enviar el link del video en Google Drive u otro medio, como usted guste, pero debe ser accesible.
* Debe adjuntar una captura de pantalla con los parámetros personalizados a la entrega.

### Resultado requerido para el avance:
* Conversión de unidades. Lectura del archivo. No es necesario aún la entrada de valores.
* Envío del archivo txt con los ejemplos de conversión.

### Resultado requerido para la entrega final:
* Trabajo completo. Incluye la inclusión de valores por el usuario, estadísticas y escritura del archivo
* Video explicando el código.

### Parámetros personalizados:
En el siguiente enlace podrá encontrar los requerimientos específicos que usted y su pareja deben cumplir.
Estos requerimientos son distintos para cada pareja:

[Obtener parámetros personalizados](https://taller-personalizado.web.app/)

Fecha de publicación: 09-10-2021

Fecha de entrega de avance: 23-10-2021

Fecha de entrega final: 06-11-2021

Desarrollo en parejas.
