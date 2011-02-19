Cumpleaños
----------
Las fechas pueden ser representadas
como tuplas ``(año, mes, dia)``.

Para asociar a cada persona su fecha de nacimiento,
se puede usar un diccionario::

    >>> n = {
    ...     'Pepito': (1990, 10, 20),
    ...     'Yayita': (1992, 3, 3),
    ...     'Panchito': (1989, 10, 20),
    ...     'Perica': (1989, 12, 8),
    ...     'Fulanita': (1991, 2, 14),
    ... }

**Ejercicio 1:**
escriba una función ``mismo_dia(fecha1, fecha2)``
que indique si las dos fechas ocurren el mismo día del año
(aunque sea en años diferentes)::

    >>> mismo_dia((2010, 6, 11), (1990, 6, 11))
    True
    >>> mismo_dia((1981, 8, 12), (1981, 5, 12))
    False

**Ejercicio 2:**
escriba una función ``mas_viejo(n)``
que indique quién es la persona más vieja
según las fechas de nacimiento del diccionario ``n``::

    >>> mas_viejo(n)
    'Panchito'

**Ejercicio 3:**
escriba una función ``primer_cumple(n)``
que indique quién es la persona
que tiene el primer cumpleaños del año::

    >>> primer_cumple(n)
    'Fulanita'
