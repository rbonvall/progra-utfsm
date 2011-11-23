Promoción con descuento
=======================

*Este problema apareció en el certamen 1 del segundo semestre de 2011 en el campus Vitacura.*

El supermercado Pitón Market ha lanzado una promoción
para todos sus clientes que posean la tarjeta Raw Input.
La promoción consiste en aplicar un descuento
por cada *n* productos que pasan por caja.

El primer descuento es de 20%,
y se aplica sobre los primeros *n* productos ingresados.
Luego,
cada descuento es la mitad del anterior,
y es aplicado sobre los siguientes *n* productos.

Por ejemplo,
si *n* = 3 y la compra es de 11 productos,
entonces los tres primeros tienen 20% de descuento,
los tres siguientes 10%,
los tres siguientes 5%,
y los dos últimos no tienen descuento.

Escriba un programa que pida al usuario ingresar *n*
y la cantidad de productos,
y luego los precios de cada producto.
Al final,
el programa debe entregar el precio total,
el descuento total
y el precio final después de aplicar el descuento.

Si al aplicar el descuento el precio queda con decimales,
redondee el valor hacia abajo.

.. testcase::

    n: `3`
    Cantidad productos: `8`
    Precio producto 1: `400`
    Precio producto 2: `800`
    Precio producto 3: `500`
    Precio producto 4: `100`
    Precio producto 5: `400`
    Precio producto 6: `300`
    Precio producto 7: `200`
    Precio producto 8: `500`
    Total: 3200
    Descuento: 420
    Por pagar: 2780

