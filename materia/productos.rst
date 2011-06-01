Productos entre arreglos
========================

Recordemos que **vector** es sinónimo de arreglo de una dimensión,
y **matriz** es sinónimo de arreglo de dos dimensiones.


Producto interno (vector-vector)
--------------------------------
El **producto interno** entre dos vectores
es la suma de los productos entre elementos correspondientes:

.. image:: ../diagramas/producto-interno.png
   :align: center

El producto interno entre dos vectores
se obtiene usando la función ``dot``
provista por NumPy::

    >>> a = array([-2.8 , -0.88,  2.76,  1.3 ,  4.43])
    >>> b = array([ 0.25, -1.58,  1.32, -0.34, -4.22])
    >>> dot(a, b)
    -14.803

El producto interno es una operación muy común.
Por ejemplo, suele usarse para calcular totales::

    >>> precios = array([200, 100, 500, 400, 400, 150])
    >>> cantidades = array([1, 0, 0, 2, 1, 0])
    >>> total_a_pagar = dot(precios, cantidades)
    >>> total_a_pagar
    1400

También se usa para calcular promedios ponderados::

    >>> notas = array([45, 98, 32])
    >>> ponderaciones = array([30, 30, 40]) / 100.
    >>> nota_final = dot(notas, ponderaciones)
    >>> nota_final
    55.7

Producto matriz-vector
----------------------
El **producto matriz-vector**
es el vector de los productos internos
El producto matriz-vector puede ser visto
simplemente como varios productos internos
calculados de una sola vez.

Esta operación también es obtenida
usando la función ``dot``
entre las filas de la matriz y el vector:

.. image:: ../diagramas/matriz-vector.png
   :align: center

El producto matriz-vector puede ser visto
simplemente como varios productos internos
calculados de una sola vez.

Esta operación también es obtenida
usando la función ``dot``::

    >>> a = array([[-0.6,  4.8, -1.2],
                   [-2. , -3.6, -2.1],
                   [ 1.7,  4.9,  0. ]])
    >>> x = array([-0.6, -2. ,  1.7])
    >>> dot(a, x)
    array([-11.28,   4.83, -10.82])

Producto matriz-matriz
----------------------
El **producto matriz-matriz**
es la matriz de los productos internos
entre las filas de la primera matriz
y las columnas de la segunda:

.. image:: ../diagramas/matriz-matriz.png
   :align: center

Esta operación también es obtenida
usando la función ``dot``::

    >>> a = array([[ 2,  8],
                   [-3,  7],
                   [-8, -5]])
    >>> b array([[-3, -5, -6, -3],
                 [-9, -2,  3, -3]])
    >>> dot(a, b)
    array([[-78, -26,  12, -30],
           [-54,   1,  39, -12],
           [ 69,  50,  33,  39]])

La multiplicación de matrices
puede ser vista como varios productos matriz-vector
(usando como vectores todas las filas de la segunda matriz),
calculados de una sola vez.

En resumen,
al usar la función ``dot``,
la estructura del resultado
depende de cuáles son los parámetros pasados::

    dot(vector, vector) → número
    dot(matriz, vector) → vector
    dot(matriz, matriz) → matriz

