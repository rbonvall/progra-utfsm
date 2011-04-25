Tabla de verdad
===============

Un **predicado lógico** es una función cuyos parámetros son booleanos
y su resultado también es booleano.

Escriba la función ``tabla_de_verdad(predicado)``
que reciba como parámetro un predicado lógico de tres parámetros
e imprima la tabla de verdad del predicado.::

    >>> def predicado(p, q, r):
    ...    return (not p) and (q or r)
    ...
    >>> tabla_verdad(predicado)
    p     q     r     predicado
    ===== ===== ===== =========
    True  True  True  False
    True  True  False False
    True  False True  False
    True  False False False
    False True  True  True
    False True  False True
    False False True  True
    False False False False

Note que la función ``tabla_verdad``
no retorna nada, sólo imprime la tabla.

