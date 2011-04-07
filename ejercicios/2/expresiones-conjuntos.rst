Expresiones con conjuntos
=========================

Considere las siguientes asignaciones::

    >>> a = {5, 2, 3, 9, 4}
    >>> b = {3, 1}
    >>> c = {7, 5, 5, 1, 8, 6}
    >>> d = [6, 2, 4, 5, 5, 3, 1, 3, 7, 8]
    >>> e = {(2, 3), (3, 4), (4, 5)}
    >>> f = [{2, 3}, {3, 4}, {4, 5}]

Sin usar el computador,
indique cuál es el resultado y el tipo de las siguientes expresiones.
A continuación,
verifique sus respuestas en el computador.

* ``len(c)``
* ``len(set(d))``
* ``a & (b | c)``
* ``(a & b) | c``
* ``c - a``
* ``max(e)``
* ``f[0] < a``
* ``set(range(4)) & a``
* ``(set(range(4)) & a) in f``
* ``len(set('perro'))``
* ``len({'perro'})``

