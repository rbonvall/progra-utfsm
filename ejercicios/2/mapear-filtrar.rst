Mapear y filtrar
----------------

Escriba la función ``mapear(f, valores)``
cuyos parámetros sean una función ``f`` y una lista ``valores``,
y que retorne una nueva lista que tenga los elementos obtenidos
al aplicar la función a los elementos de la lista::

    >>> def cuadrado(x):
    ...     return x ** 2
    ...
    >>> mapear(cuadrado, [5, 2, 9])
    [25, 4, 81]

Escriba la función ``filtrar(f, valores)``
cuyos parametros sean una función ``f`` que retorne un valor booleano
y una lista ``valores``,
y que retorne una nueva lista que tenga todos los elementos de ``valores``
para los que la función ``f`` retorne ``True``::

    >>> def es_larga(palabra):
    ...     return len(palabra) > 4
    ...
    >>> p = ['arroz', 'leon', 'oso', 'mochila']
    >>> filtrar(es_larga, p)
    ['arroz', 'mochila']

Las funciones no deben modificar la lista original,
sino retornar una nueva::

    >>> filtrar(es_larga, p)
    ['arroz', 'mochila']
    >>> p
    ['arroz', 'leon', 'oso', 'mochila']

(En Python, estas funciones ya existen, y se llaman ``map`` y ``filter``.
Ignore esta información y escriba las funciones por su cuenta).
