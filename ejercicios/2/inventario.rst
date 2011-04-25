Inventario
----------
Una tienda tiene la información de sus productos
en un archivo llamado ``productos.txt``.
Cada línea del archivo tiene tres datos:

* el código del producto (un número entero),
* el nombre del producto, y
* la cantidad de unidades del producto
  que quedan en bodega.

Los datos están separados por un símbolo ``/``.
Por ejemplo,
el siguiente puede ser el contenido del archivo:

.. code-block:: none

    1265/Reloj/26
    613/Cuaderno/87
    9801/Vuvuzela/3
    321/Lápiz/12
    5413/Tomate/5

1. Escriba la función ``existe_producto(codigo)``
   que indique si existe el producto
   con el código dado::

    >>> existe_producto(1784)
    False
    >>> existe_producto(321)
    True
    >>> existe_producto(613)
    True
    >>> existe_producto(0)
    False

2. Escriba la función ``por_reabastecer()``
   que cree un nuevo archivo llamado ``por_reabastecer.txt``
   que contenga los datos de todos los productos
   de los que queden menos de 10 unidades.

   En este caso,
   el archivo ``por_reabastecer.txt``
   debe quedar así:

.. code-block:: none

    9801/Vuvuzela/3
    5413/Tomate/5


