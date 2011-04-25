Iguales o distintos
-------------------

Escriba la función ``todos_iguales(lista)``
que indique si todos los elementos de una lista son iguales::

    >>> todos_iguales([6, 6, 6])
    True
    >>> todos_iguales([6, 6, 1])
    False
    >>> todos_iguales([0, 90, 1])
    False

A continuación, escriba una función ``todos_distintos(lista)``
que indique si todos los elementos de una lista son distintos::

    >>> todos_distintos([6, 6, 6])
    False
    >>> todos_distintos([6, 6, 1])
    False
    >>> todos_distintos([0, 90, 1])
    True

Sus funciones deben ser capaces de aceptar listas de cualquier tamaño
y con cualquier tipo de datos::

    >>> todos_iguales([7, 7, 7, 7, 7, 7, 7, 7, 7])
    True
    >>> todos_distintos(list(range(1000)))
    True
    >>> todos_iguales([12])
    True
    >>> todos_distintos(list('hiperblanduzcos'))
    True

