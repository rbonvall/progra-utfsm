Expresiones con tuplas
======================

Considere las siguientes asignaciones::

    >>> a = (2, 10, 1991)
    >>> b = (25, 12, 1990)
    >>> c = ('Donald', True, b)
    >>> x, y = ((27, 3), 9)
    >>> z, w = x
    >>> v = (x, a)

Sin usar el computador,
indique cuál es el resultado y el tipo de las siguientes expresiones.
A continuación,
verifique sus respuestas en el computador.

* ``a < b``
* ``y + w``
* ``x + a``
* ``len(v)``
* ``v[1][1]``
* ``c[0][0]``
* ``z, y``
* ``a + b[1:5]``
* ``(a + b)[1:5]``
* ``str(a[2]) + str(b[2])``
* ``str(a[2] + b[2])``
* ``str((a + b)[2])``
* ``str(a + b)[2]``

