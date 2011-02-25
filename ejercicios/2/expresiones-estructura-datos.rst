Expresiones con estructuras de datos anidadas
=============================================

Considere el siguiente trozo de programa::

    d = {
      (1, 2): [{1, 2}, {3}, {1, 3}],
      (2, 1): [{3}, {1, 2}, {1, 2, 3}],
      (2, 2): [{}, {2, 3}, {1, 3}],
    }

Indique el valor y el tipo de las siguientes expresiones:

* ``len(d)`` (respuesta: el valor es ``3``, el tipo es ``int``)
* ``d[(1, 2)][2]`` (respuesta: el valor es ``{1, 3}``, el tipo es ``set``)
* ``d[(2, 2)][0]``
* ``(1, 2)``
* ``(1, 2)[1]``
* ``d[(1, 2)][1]``
* ``d[(1, 2)]``
* ``d[1, 2]``
* ``len(d[2, 1])``
* ``len(d[2, 1][1])``
* ``d[2, 2][1] & d[1, 2][2]``
* ``(d[2, 2] + d[2, 1])[4]``
* ``max(map(len, d.values()))``
* ``min(map(len, d[2, 1]))``
* ``d[1, 2][-3] & d[2, 1][-2] & d[2, 2][-1]``
* ``d[len(d[2, 1][1]), len(d[1, 2][-1])][1]``

Puede verificar sus respuestas
usando la consola interactiva.
Para obtener el tipo,
use la función ``type``::

    >>> v = d[(1, 2)][2]
    >>> v
    {1, 3}
    >>> type(v)
    <class 'set'>

