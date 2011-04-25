Producto interno
----------------

El **producto interno** de dos listas de números
es la suma de los productos de los términos correspondientes de ambas.

Por ejemplo, si::

    a = [5, 1, 6]
    b = [1, -2, 8]

entonces el producto interno entre ``a`` y ``b`` es::

    (5 * 1) + (1 * -2) + (6 * 8)

1. Escriba la función ``producto_interno(a, b)``
   que entregue el producto interno de ``a`` y ``b``::

      >>> a = [7, 1, 4, 9, 8]
      >>> b = range(5)
      >>> producto_interno(a, b)
      68

2. Dos listas de números son **ortogonales**
   si su producto interno es cero.
   Escriba la función ``son_ortogonales(a, b)``
   que indique si ``a`` y ``b`` son ortogonales::

     >>> son_ortogonales([2, 1], [-3, 6])
     True

