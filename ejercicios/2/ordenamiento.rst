Ordenamiento
============

El método ``sort`` de las listas
ordena sus elementos de menor a mayor::

    >>> a.sort()
    >>> a
    [0, 1, 4, 6, 9]

A veces necesitamos ordenar los elementos
de acuerdo a otro criterio.
Para esto,
el método ``sort`` acepta un parámetro con nombre llamado ``key``,
que debe ser una función que asocia a cada elemento
el valor que será usado para ordenar.

Por ejemplo,
para ordenar la lista de mayor a menor
uno puede usar una función que cambie el signo de cada número::

    >>> def negativo(x):
    ...     return -x
    ...
    >>> a = [6, 1, 4, 0, 9]
    >>> a.sort(key=negativo)
    >>> a
    [9, 6, 4, 1, 0]

Esto significa que la lista es ordenada
comparando los negativos de sus elementos,
aunque son los elementos originales
los que aparecen en el resultado.

Como segundo ejemplo,
veamos cómo ordenar una lista de números
por su último dígito, de menor a mayor::

    >>> def ultimo_digito(n):
    ...     return n % 10
    ...
    >>> a = [65, 71, 39, 30, 26]
    >>> a.sort(key=ultimo_digito)
    >>> a
    [30, 71, 65, 26, 39]

Resuelva los siguientes problemas de ordenamiento,
escribiendo la función criterio para cada caso,
e indicando qué es lo que debe ir
en la línea marcada con ``???????``.

* Ordenar una lista de strings de la más corta a la más larga::

    >>> animales = ['conejo', 'ornitorrinco', 'pez', 'hipopotamo', 'tigre']
    >>> # ???????
    >>> animales
    ['pez', 'tigre', 'conejo', 'hipopotamo', 'ornitorrinco']

* Ordenar una lista de strings de la más larga a la más corta::

    >>> animales = ['conejo', 'ornitorrinco', 'pez', 'hipopotamo', 'tigre']
    >>> # ???????
    >>> animales
    ['ornitorrinco', 'hipopotamo', 'conejo', 'tigre', 'pez']

* Ordenar una lista de listas
  según la suma de sus elementos,
  de menor a mayor::

    >>> a = [
    ...   [6, 1, 5, 9],
    ...   [0, 0, 4, 0, 1],
    ...   [3, 2, 12, 1],
    ...   [1000],
    ...   [7, 6, 1, 0],
    ... ]
    >>> # ??????
    >>>
    >>> a
    [[0, 0, 4, 0, 1], [7, 6, 1, 0], [3, 2, 12, 1], [6, 1, 5, 9], [1000]]

  (Las sumas en la lista ordenada son,
  respectivamente, 5, 14, 18, 21 y 1000).

* Ordenar una lista de tuplas ``(nombre, apellido, (anno, mes, dia))``
  por orden alfabético de apellidos::

    >>> personas = [
    ...     ('John',   'Doe',         (1992, 12, 28)),
    ...     ('Perico', 'Los Palotes', (1992, 10, 8)),
    ...     ('Yayita', 'Vinagre',     (1991,  4, 17)),
    ...     ('Fulano', 'De Tal',      (1992, 10, 4)),
    ... ]
    >>> # ???????
    >>> from pprint import pprint
    >>> pprint(personas)
    [('Fulano', 'De Tal', (1992, 10, 4)),
     ('John', 'Doe', (1992, 12, 28)),
     ('Perico', 'Los Palotes', (1992, 10, 8)),
     ('Yayita', 'Vinagre', (1991, 4, 17))]

  (La función ``pprint`` sirve para imprimir estructuras de datos
  hacia abajo en vez de hacia el lado).

* Ordenar una lista de tuplas ``(nombre, apellido, (anno, mes, dia))``
  por fecha de nacimiento, de la más antigua a la más reciente::

    >>> # ???????
    >>> pprint(personas)
    [('Yayita', 'Vinagre', (1991, 4, 17)),
     ('Fulano', 'De Tal', (1992, 10, 4)),
     ('Perico', 'Los Palotes', (1992, 10, 8)),
     ('John', 'Doe', (1992, 12, 28))]

* Ordenar una lista de tuplas ``(nombre, apellido, (anno, mes, dia))``
  por fecha de nacimiento,
  pero ahora de la más reciente a la más antigua::

    >>> # ???????
    >>> pprint(personas)
    [('John', 'Doe', (1992, 12, 28)),
     ('Perico', 'Los Palotes', (1992, 10, 8)),
     ('Fulano', 'De Tal', (1992, 10, 4)),
     ('Yayita', 'Vinagre', (1991, 4, 17))]

* Ordenar una lista de meses
  según la cantidad de días, de más a menos::

    >>> meses = ['agosto', 'noviembre', 'abril', 'febrero']
    >>> # ???????
    >>> meses
    ['febrero', 'noviembre', 'abril', 'agosto']

* Hacer que queden los números impares a la izquierda
  y los pares a la derecha::

    >>> from random import randrange
    >>> valores = []
    >>> for i in range(12):
    ...     valores.append(randrange(256))
    ...
    >>> valores
    [55, 222, 47, 81, 82, 44, 218, 82, 20, 96, 82, 251]
    >>> # ???????
    >>> valores
    [55, 47, 81, 251, 222, 82, 44, 218, 82, 20, 96, 82]

* Hacer que queden los palíndromos a la derecha
  y los no palíndromos a la izquierda::

    >>> a = [12321, 584, 713317, 8990, 44444, 28902]
    >>> # ????????
    >>> a
    [584, 8990, 28902, 12321, 713317, 44444]

