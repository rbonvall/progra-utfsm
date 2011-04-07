Expresiones con listas
======================

Considere las siguientes listas::

    >>> a = [5, 1, 4, 9, 0]
    >>> b = range(3, 10) + range(20, 23)
    >>> c = [[1, 2], [3, 4, 5], [6, 7]]
    >>> d = ['perro', 'gato', 'jirafa', 'elefante']
    >>> e = ['a', a, 2 * a]

Sin usar el computador,
indique cuál es el resultado y el tipo de las siguientes expresiones.
A continuación,
verifique sus respuestas en el computador.

* ``a[2]``
* ``b[9]``
* ``c[1][2]``
* ``e[0] == e[1]``
* ``len(c)``
* ``len(c[0])``
* ``len(e)``
* ``c[-1]``
* ``c[-1][+1]``
* ``c[2:] + d[2:]``
* ``a[3:10]``
* ``a[3:10:2]``
* ``d.index('jirafa')``
* ``e[c[0][1]].count(5)``
* ``sorted(a)[2]``
* ``complex(b[0], b[1])``

