Resolución de sistemas lineales
===============================

Repasemos el producto matriz-vector:

.. image:: ../diagramas/dieta-1.png
   :align: center

Esta operación tiene dos operandos:
una matriz y un vector.
El resultado es un vector.
A los operandos los denominaremos respectivamente ``A`` y ``x``,
y al resultado, ``b``.

Un problema recurrente en Ingeniería
consiste en obtener cuál es el vector ``x``
cuando ``A`` y ``b`` son dados:

.. image:: ../diagramas/dieta-2.png
   :align: center

La ecuación matricial `Ax = b` es una manera abreviada
de expresar un `sistema de ecuaciones lineales`_.
Por ejemplo,
la ecuación del diagrama
es equivalente al siguiente sistema de tres ecuaciones
que tiene las tres incógnitas `w`, `y` y `z`:

.. math::

    \begin{align}
      36w + 51y + 13z &= 3 \\
      52w + 34y + 74z &= 45 \\
             7y + 1.1z &= 33 \\
    \end{align}

.. _sistema de ecuaciones lineales: http://es.wikipedia.org/wiki/Sistema_de_ecuaciones_lineales

En matemáticas,
este sistema se representa matricialmente así:

.. math::

    \begin{bmatrix}
      36 & 51 & 13 \\
      52 & 34 & 74 \\
         &  7 & 1.1 \\
    \end{bmatrix}
    \begin{bmatrix}
       w \\ y \\ z \\
    \end{bmatrix}
    =
    \begin{bmatrix}
       3 \\ 45 \\ 33 \\
    \end{bmatrix}

La teoría detrás de la resolución de problemas de este tipo
usted la aprenderá en sus ramos de matemáticas.
Sin embargo,
como este tipo de problemas aparece a menudo en la práctica,
aprenderemos cómo obtener rápidamente la solución
usando Python.

Dentro de los varios módulos incluídos en NumPy
(por ejemplo, ya vimos ``numpy.random``),
está el módulo ``numpy.linalg``,
que provee algunas funciones que implementan algoritmos de álgebra lineal,
que es la rama de las matemáticas que estudia los problemas de este tipo.
En este módulo está la función ``solve``,
que entrega la solución ``x`` de un sistema
a partir de la matriz ``A`` y el vector ``b``::

    >>> a = array([[ 36. ,  51. ,  13. ],
    ...            [ 52. ,  34. ,  74. ],
    ...            [  0. ,   7. ,   1.1]])
    >>> b = array([  3.,  45.,  33.])
    >>> x = solve(a, b)
    >>> x
    array([-7.10829222,  4.13213834,  3.70457422])

Podemos ver que el vector ``x`` en efecto
satisface la ecuación ``Ax = b``::

    >>> dot(a, x)
    array([  3.,  45.,  33.])
    >>> b
    array([  3.,  45.,  33.])

Sin embargo, es importante tener en cuenta que
los valores de tipo real
casi nunca están representados de manera exacta en el computador,
y que el resultado de un algoritmo que involucra muchas operaciones
puede sufrir de algunos errores de redondeo.
Por esto mismo,
puede ocurrir que aunque los resultados se vean iguales en la consola,
los datos obtenidos son sólo aproximaciones
y no exactamente los mismos valores::

    >>> (dot(a, x) == b).all()
    False


