Conjunto potencia
=================

El `conjunto potencia`_ de un conjunto *S*
es el conjunto de todos los subconjuntos de *S*.

Por ejemplo, el conjunto potencia de `\{1, 2, 3\}` es:

.. math::

    \left\{
      \emptyset,
      \{1\},
      \{2\},
      \{3\},
      \{1, 2\},
      \{1, 3\},
      \{2, 3\},
      \{1, 2, 3\}
    \right\}

En Python,
un conjunto no puede contener a otros conjuntos,
ya que no puede tener elementos mutables,
y los conjuntos lo son::

    >>> a = set()
    >>> a.add({1, 2})        # :(
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    TypeError: unhashable type: 'set'

Lo que sí podemos crear es una lista de conjuntos::

    >>> l = list()
    >>> l.append({1, 2})     # :)
    >>> l
    [set([1, 2])]

.. 1. Escriba la función ``subconjuntos_de_tamano(s, n)``
..    que reciba como parámetros
..    un conjunto ``s`` cualquiera y un número entero no negativo ``n``,
..    y que retorne la lista de todos los subconjuntos de ``s``
..    que tienen tamaño ``n``::
..
..        >>> subconjuntos_de_tamano({2, 4, 5, 6}, 2)
..        [set([2, 4]), set([2, 5]), set([2, 6]), set([4, 5]), set([4, 6]), set([5, 6])]
..

Escriba la función ``conjunto_potencia(s)``
que reciba como parámetro un conjunto cualquiera ``s``
y retorne su «lista potencia»
(la lista de todos sus subconjuntos)::

   >>> conjunto_potencia({6, 1, 4})
   [set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]

