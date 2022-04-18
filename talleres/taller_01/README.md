# Taller 01 - Sistema de ventas
#### Año: 2021

Considere que usted debe hacer un sistema de ventas para una empresa. El sistema debe poder procesar
distintos pedidos de distintos clientes, y cada cliente compra diversos productos. Para simplificar
asuma que solo hay una lista pequeña de productos.

Por cada nuevo pedido se le debe desplegar al cliente la lista de productos disponibles y él tiene la
posibilidad de elegir el que desea. Cada producto tiene un precio distinto.

El sistema debe ejecutarse hasya que ya no haya nuevos pedidos que procesar y al finalizar debe entregar una
serie de estadísticas estándar:

1. Monto total vendido durante el día
2. Cantidad de productos vendidos con un precio mayor al precio promedio
3. Cantidad de pedidos realizados con más de 5 productos
4. Cliente que realizó la mayor compra

Considere que al cliente se le aplica un descuento, el cual se le indicará con los parámetros personalizados
(ver al final).

También considere que podría tener que aplicar IVA al total de la compra (también dependerá de los parámetros
personalizados).

Su sistema debe considerar la existencia de "tipos de clientes": VIP, Premium, Standard, Magnum, Preferencial,
o como usted decida nombrarlos. Al comenzar cada nueva venta debe preguntarse por pantalla el tipo de cliente,
y si es que el cliente es de una categoría superior se le deberá aplicar el tipo de descuento especificado en
sus parámetros personalizados.

En los parámetros personalizados también se le indicará el tipo de tienda (deportes, abarrotes, ferretería, etc)
y por lo tanto todo el contexto del programa deberá estar de acuerdo a eso (mensaje de bienvenida, productos, etc).

La compra puede ser online o presencial (se le indicará en los parámetros). En caso de ser online se debe incluir
costo de envío (usted determine como calcularlo). En caso de ser presencial se le debe preguntar si incluye propina.
Ninguno de los dos casos (propina y envío) se deben considerar como un monto de venta para la tienda 
(estadística 1 arriba).

Finalmente se debe entregar 4 estadísticas personalizadas que también le serán indicadas.

Es importante destacar que el código no debe usar listas, matrices u otras estructuras de datos que
aún no hemos visto. El programa no debe hacer uso de archivos ni hacer uso de funciones. Sin embargo, sí podrá usar
librerías externas si así lo necesita.

### Condiciones de entrega:
* Debe enviar el archivo en formato Python (.py) o Jupyter Notebook (.ipynb)
* Junto con la entrega debe enviar un video de máximo de 3 minutos explicando el código realizado en que ambos alumnos
hablen. Puede enviar el link del video en Google Drive u otro medio, como usted guste, pero debe ser accesible.
* Debe adjuntar una captura de pantalla con los parámetros personalizados a la entrega.

### Resultado requerido para el avance:

* Todo, sin las estadísticas y los descuentos
* Captura de pantalla con los parámetros personalizados

### Resultado requerido para la entrega final:

* Se incluye las estadísticas y los descuentos a las ventas
* Video explicando el código

### Parámetros personalizados:
En el siguiente enlace podrá encontrar los requerimientos específicos que usted y su pareja deben cumplir.
Estos requerimientos son distintos para cada pareja:

[Obtener parámetros personalizados](https://taller-personalizado.web.app/)

Fecha de publicación: 04-09-2021

Fecha de entrega de avance: 25-09-2021

Fecha de entrega final: 09-10-2021

Desarrollo en parejas.