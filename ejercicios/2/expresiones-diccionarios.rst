Expresiones con diccionarios
============================

Considere las siguientes asignaciones::

    >>> a = {'a': 14, 'b': 23, 'c': 88}
    >>> b = {12: True, 55: False, -2: False}
    >>> c = dict()
    >>> d = {1: [2, 3, 4], 5: [6, 7, 8, 9], 10: [11]}
    >>> e = {2 + 3: 4, 5: 6 + 7, 8: 9, 10: 11 + 12}

Sin usar el computador,
indique cuál es el resultado y el tipo de las siguientes expresiones.
A continuación,
verifique sus respuestas en el computador.

* ``a['c']``
* ``a[23]``
* ``b[-2] or b[55]``
* ``23 in a``
* ``'a' in a``
* ``5 in d[5]``
* ``sum(b)``
* ``len(c)``
* ``len(d)``
* ``len(d[1])``
* ``len(b.values())``
* ``len(e)``
* ``sum(a.values())``
* ``max(list(e))``
* ``d[1] + d[5] + d[10]``
* ``max(map(len, d.values()))``

