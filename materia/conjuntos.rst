Conjuntos
=========
.. index:: conjuntos

Un **conjunto** es una colección desordenada de valores no repetidos.

Los conjuntos de Python son análogos a los conjuntos matemáticos.
El tipo de datos que representa a los conjuntos se llama ``set``.

El tipo ``set`` es mutable:
una vez que se ha creado un conjunto, puede ser modificado.

Cómo crear conjuntos
--------------------
Las dos maneras principales de crear un conjunto son:

* usar un conjunto literal, entre llaves::

    >>> colores = {'azul', 'rojo', 'blanco', 'blanco'}
    >>> colores
    {'rojo', 'azul', 'blanco'}

  Note que el conjunto no incluye elementos repetidos,
  y que los elementos no quedan en el mismo orden en que fueron agregados.

* usar la función ``set`` aplicada sobre un iterable::

    >>> set('abracadabra')
    {'a', 'r', 'b', 'c', 'd'}
    >>> set(range(50, 2000, 400))
    {1250, 50, 1650, 850, 450}
    >>> set([(1, 2, 3), (4, 5), (6, 7, 8, 9)])
    {(4, 5), (6, 7, 8, 9), (1, 2, 3)}

  El conjunto vacío debe ser creado usando ``set()``,
  ya que ``{}`` representa el diccionario vacío.

Los elementos de un conjunto deben ser inmutables.
Por ejemplo, no es posible crear un conjunto de listas,
pero sí un conjunto de tuplas::

    >>> s = {[2, 4], [6, 1]}
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'
    >>> s = {(2, 4), (6, 1)}
    >>>

Como un conjunto no es ordenado,
no tiene sentido intentar obtener un elemento usando un índice::

    >>> s = {'a', 'b', 'c'}
    >>> s[0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing

Sin embargo,
sí es posible iterar sobre un conjunto usando un ciclo ``for``::

    >>> for i in {'a', 'b', 'c'}:
    ...     print i
    ...
    a
    c
    b

Operaciones sobre conjuntos
---------------------------
``len(s)`` entrega el número de elementos del conjunto ``s``::

    >>> len({'azul', 'verde', 'rojo'})
    3
    >>> len(set('abracadabra'))
    5
    >>> len(set())
    0

``x in s`` permite saber si el elemento ``x`` está en el conjunto ``s``::

    >>> 3 in {2, 3, 4}
    True
    >>> 5 in {2, 3, 4}
    False

``x not in s`` permite saber si ``x`` no está en ``s``::

    >>> 10 not in {2, 3, 4}
    True

``s.add(x)`` agrega el elemento ``x`` al conjunto ``s``::

    >>> s = {6, 1, 5, 4, 3}
    >>> s.add(-37)
    >>> s
    {1, 3, 4, 5, 6, -37}
    >>> s.add(4)
    >>> s
    {1, 3, 4, 5, 6, -37}

``s.remove(x)`` elimina el elemento ``x`` del conjunto ``s``::

    >>> s = {6, 1, 5, 4, 3}
    >>> s.remove(1)
    >>> s
    {3, 4, 5, 6}

Si el elemento ``x`` no está en el conjunto, ocurre un **error de llave**::

    >>> s.remove(10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 10

``&`` y ``|`` son, respectivamente,
los operadores de intersección y unión::

    >>> a = {1, 2, 3, 4}
    >>> b = {2, 4, 6, 8}
    >>> a & b
    {2, 4}
    >>> a | b
    {1, 2, 3, 4, 6, 8}

``s - t`` entrega la diferencia entre ``s`` y ``t``;
es decir, los elementos de ``s`` que no están en ``t``::

    >>> a - b
    {1, 3}

``s ^ t`` entrega la diferencia simétrica entre ``s`` y ``t``;
es decir, los elementos que están en ``s`` o en ``t``,
pero no en ambos::

    >>> a ^ b
    {1, 3, 6, 8}

El operador ``<`` aplicado sobre conjuntos
significa «es subconjunto de»::

    >>> {1, 2} < {1, 2, 3}
    True
    >>> {1, 4} < {1, 2, 3}
    False

``s <= t`` también indica si ``s`` es subconjunto de ``t``.
La distinción ocurre cuando los conjuntos son iguales::

    >>> {1, 2, 3} < {1, 2, 3}
    False
    >>> {1, 2, 3} <= {1, 2, 3}
    True


