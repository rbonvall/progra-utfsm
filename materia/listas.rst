Listas
======

.. index:: lista

Una **lista** es una colección ordenada de valores.
Una lista puede contener cualquier cosa.

En Python, el tipo de datos que representa a las listas
se llama ``list``.

Cómo crear listas
-----------------
Las dos maneras principales de crear una lista son:

.. index:: []

* usar una lista literal, con los valores entre corchetes::

    >>> primos = [2, 3, 5, 7, 11]
    >>> primos
    [2, 3, 5, 7, 11]
    >>> []
    []
    >>> [1.0 + 2.0, 3.0 + 4.0 + 5.0]
    [3.0, 12.0]
    >>> ['hola ' + 'mundo', 24 * 7, True or False]
    ['hola mundo', 168, True]

.. index:: list

* usar la función ``list`` aplicada sobre un iterable::

    >>> list('hola')
    ['h', 'o', 'l', 'a']
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list()
    []

Operaciones sobre listas
------------------------
.. index:: len (listas)

``len(l)`` entrega el largo de la lista;
es decir, cuántos elementos tiene::

    >>> colores = ['azul', 'rojo', 'verde', 'amarillo']
    >>> len(colores)
    4
    >>> len([True, True, True])
    3
    >>> len([])
    0

.. index:: índice (listas)

``l[i]`` entrega el ``i``-ésimo valor de la lista.
El valor ``i`` se llama **índice** del valor.
Al igual que para los strings,
los índices parten de cero::

    >>> colores = ['azul', 'rojo', 'verde', 'amarillo']
    >>> colores[0]
    'azul'
    >>> colores[3]
    'amarillo'

Además, es posible modificar el valor del ``i``-ésimo elemento::

    >>> colores[1] = 'negro'
    >>> colores
    ['azul', 'negro', 'verde', 'amarillo']

.. index:: error de índice, IndexError

Si el índice ``i`` indica un elemento que no está en la lista,
ocurre un **error de índice**::

    >>> colores[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

Si el índice es negativo,
los elementos se cuentan desde el final hacia atrás::

    >>> colores[-1]
    'amarillo'
    >>> colores[-4]
    'azul'

.. index:: append

``l.append(x)`` agrega el elemento ``x`` al final de la lista::

    >>> primos = [2, 3, 5, 7, 11]
    >>> primos.append(13)
    >>> primos.append(17)
    >>> primos
    [2, 3, 5, 7, 11, 13, 17]

.. index:: método

Un comentario al margen:
``append`` es un **método**.
Los métodos son funciones que están dentro de un objeto.
Cada lista tiene su propia función ``append``.
Es importante tener esta distinción clara,
ya que hay operaciones que están implementadas como funciones
y otras como métodos.

.. index:: sum

``sum(x)`` entrega la suma de los valores de la lista::

    >>> sum([1, 2, 1, -1, -2])
    1
    >>> sum([])
    0

.. index:: concatenación (listas)

``l1 + l2`` concatena las listas ``l1`` y ``l2``::

    >>> list('perro') + [2, 3, 4]
    ['p', 'e', 'r', 'r', 'o', 2, 3, 4]

.. index:: repetición (listas)

``l * n`` repite ``n`` veces la lista ``l``::

    >>> [3.14, 6.28, 9.42] * 2
    [3.14, 6.28, 9.42, 3.14, 6.28, 9.42]
    >>> [3.14, 6.28, 9.42] * 0
    []

.. index:: in (listas), not in (listas)

Para saber si un elemento ``x`` está en la lista ``l``,
se usa ``x in l``.
La versión negativa de ``in`` es ``not in``::

    >>> r = range(0, 20, 2)
    >>> r
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    >>> 12 in r
    True
    >>> 15 in r
    False
    >>> 15 not in r
    True

.. index:: rebanado (listas)

``l[i:j]`` es el operador de rebanado,
que entrega una nueva lista
que tiene desde el ``i``-ésimo
hasta justo antes del ``j``-ésimo elemento
de la lista ``l``::

    >>> x = [1.5, 3.3, 8.4, 3.1, 2.9]
    >>> x[2:4]
    [8.4, 3.1]

.. index:: count (listas)

``l.count(x)`` cuenta cuántas veces está
el elemento ``x`` en la lista::

    >>> letras = list('paralelepipedo')
    >>> letras.count('p')
    3

.. index:: index (listas)

``l.index(x)`` entrega cuál es el índice del valor ``x``::

    >>> colores = ['azul', 'rojo', 'verde', 'amarillo']
    >>> colores.index('verde')
    2
    >>> colores.index('fucsia')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 'fucsia' is not in list

.. index:: remove

``l.remove(x)`` elimina el elemento ``x`` de la lista::

    >>> l = [7, 0, 3, 9, 8, 2, 4]
    >>> l.remove(2)
    >>> l
    [7, 0, 3, 9, 8, 4]

.. index:: del (listas)

``del l[i]`` elimina el ``i``-ésimo elemento de la lista::

    >>> l = [7, 0, 3, 9, 8, 2, 4]
    >>> del l[2]
    >>> l
    [7, 0, 9, 8, 2, 4]

.. index:: reverse

``l.reverse()`` invierte la lista::

    >>> l = [7, 0, 3, 9, 8, 2, 4]
    >>> l.reverse()
    >>> l
    [4, 2, 8, 9, 3, 0, 7]

.. index:: sort, ordenar lista

``l.sort()`` ordena la lista::

    >>> l = [7, 0, 3, 9, 8, 2, 4]
    >>> l.sort()
    >>> l
    [0, 2, 3, 4, 7, 8, 9]

Para todas estas operaciones,
siempre hay que tener muy claro
si la lista es modificada o no.
Por ejemplo, el rebanado no modifica la lista,
sino que crea una nueva::

    >>> ramos = ['Progra', 'Mate', 'Fisica', 'Ed.Fisica']
    >>> ramos[:2]
    ['Progra', 'Mate']
    >>> len(ramos)    # la lista sigue teniendo cuatro elementos
    4

Iteración sobre una lista
-------------------------
.. index:: iterable

Una lista es un objeto **iterable**.
Esto significa que sus valores se pueden recorrer
usando un ciclo ``for``::

    valores = [6, 1, 7, 8, 9]
    for i in valores:
        print i ** 2

En cada iteración del ``for``,
la variable ``i`` toma uno de los valores de la lista,
por lo que este programa imprime los siguientes valores:

.. testcase::

    36
    1
    49
    64
    81

