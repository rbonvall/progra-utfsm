Sumas por fila y columna
------------------------

El archivo ``datos1.txt``
tiene tres números enteros en cada línea:

.. code-block:: none

    45 12 98
    1 12 65
    7 15 76
    54 23 1
    65 2 84

1. Escriba la función ``suma_lineas(nombre_archivo)``
   que entregue una lista con las sumas
   de todas las líneas del archivo::

    >>> suma_lineas('datos1.txt')
    [155, 78, 98, 78, 151]

2. Escriba la función ``suma_columnas(nombre_archivo)``
   que entregue una lista con las sumas
   de las tres columnas del archivo::

    >>> suma_columnas('datos1.txt')
    [172, 64, 324]

