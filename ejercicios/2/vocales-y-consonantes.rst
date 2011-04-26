Vocales y consonantes
---------------------

Escriba una función que determine si una letra
es vocal o consonante.
Decida usted qué es lo que retornará la función.
Por ejemplo, podría ser así::

    >>> es_vocal('a')
    True
    >>> es_vocal('b')
    False

O así::

    >>> es_consonante('a')
    False
    >>> es_consonante('b')
    True

O incluso así::

    >>> tipo_de_letra('a')
    'vocal'
    >>> tipo_de_letra('b')
    'consonante'

A continuación,
escriba la función ``contar_vocales_y_consonantes(palabra)``
que retorne las cantidades de vocales y consonantes
de la palabra.
Esta función debe llamar a la función que usted escribió antes.

::

    >>> v, c = contar_vocales_y_consonantes('edificio')
    >>> v
    5
    >>> c
    3

Finalmente,
escriba un programa que pida al usuario ingresar una palabra
y le muestre cuántas vocales y consonantes tiene:

.. testcase::

    Ingrese palabra: `edificio`
    Tiene 5 vocales y 3 consonantes
