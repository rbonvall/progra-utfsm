Láminas
-------
El módulo ``random`` provee funciones
para entregar valores al azar.
En computación, los números creados al azar
se llaman **números aleatorios**.

La función ``randrange(n, m)``
entrega un número aleatorio en el rango entre ``n`` y ``m``::

    >>> from random import randrange
    >>> randrange(5, 15)
    14
    >>> randrange(5, 15)
    6
    >>> randrange(5, 15)
    14
    >>> randrange(5, 15)
    5
    >>> randrange(5, 15)
    12
    >>> randrange(5, 15)
    9

(Recuerde que los rangos incluyen el primer valor
pero no el último, así que la función retorna números
entre 5 y 14).

.. La función ``choice(l)`` entrega un elemento aleatorio de ``l``::
..
..     >>> from random import choice
..     >>> choice(['cara', 'sello'])
..     'cara'
..     >>> choice(['cara', 'sello'])
..     'cara'
..     >>> choice(['cara', 'sello'])
..     'sello'
..     >>> choice(['cara', 'sello'])
..     'cara'
..     >>> choice(['cara', 'sello'])
..     'sello'
..     >>> choice([1, 4, 9, 16])
..     4
..     >>> choice([1, 4, 9, 16])
..     4
..     >>> choice('tijera papel piedra'.split())
..     'tijera'
..
.. La función ``shuffle(l)`` «baraja» la lista ``l``::
..
..     >>> from random import shuffle
..     >>> a = [1, 5, 9, 12, 14]
..     >>> shuffle(a)
..     >>> a
..     [12, 1, 5, 9, 14]
..     >>> shuffle(a)
..     >>> a
..     [9, 12, 14, 1, 5]

#. Suponga que Pepito colecciona un álbum de láminas.
   Las láminas están numeradas desde 1 hasta 640,
   y se compran en sobres de cinco láminas al azar.

   Escriba la función ``nuevo_sobre()``
   que entregue una lista con las láminas que vienen
   en un sobre recién comprado::

    >>> nuevo_sobre()
    [27, 31, 207, 455, 529]
    >>> nuevo_sobre()
    [66, 577, 481, 171, 602]
    >>> nuevo_sobre()
    [275, 493, 167, 25, 592]
    >>> nuevo_sobre()
    [113, 35, 592, 560, 244]

#. Pepito lleva un registro de sus láminas
   en una lista llamada ``laminas_pepito``.
   Cada ciertos días,
   Pepito va al quiosco y compra algunos sobres,
   y los agrega a su lista.

   Escriba la función ``agregar_laminas(lista_laminas, m)``,
   que agregue las láminas de ``m`` nuevos sobres
   a la ``lista_laminas``::

    >>> laminas_pepito = []
    >>> agregar_laminas(laminas_pepito, 1)
    >>> laminas_pepito
    [190, 130, 53, 537, 167]
    >>> agregar_laminas(laminas_pepito, 2)
    >>> laminas_pepito
    [190, 130, 53, 537, 167, 572, 537, 375, 496, 469, 249, 545, 95, 279, 131]
    >>>
    >>> agregar_laminas(laminas_pepito, 14)
    >>> len(laminas_pepito)
    85

   Note que la función no retorna nada.
   Sólo modifica la lista que recibe como parámetro.

#. Escriba la función ``faltantes(lista_laminas)``
   que entregue el conjunto de las láminas que faltan para completar el álbum::

    >>> laminas_pepito = []
    >>> agregar_laminas(laminas_pepito, 128)
    >>> faltantes(laminas_pepito)
    {514, 3, 5, 7, 10, 523, 12, 525, 14, 16, 529, ...}

   Note que Pepito compró 128 sobres,
   que en total tienen el mismo número de láminas del álbum,
   pero como hay muchas láminas repetidas y otras que no salen,
   no es suficiente para completar el álbum.

#. Escriba la función ``cuenta(lista_laminas)``
   que entregue un diccionario que asocie a cada lámina
   el número de veces que está en la lista de láminas::

    >>> laminas_pepito = [4, 6, 9, 12, 9, 9, 6, 12, 2]
    >>> cuenta(laminas_pepito)
    {9: 3, 2: 1, 4: 1, 6: 2, 12: 2}

#. Pepito intercambia láminas con Yayita,
   que también colecciona el álbum.
   A Pepito le interesa obtener las láminas que Yayita tiene repetidas
   y que a él le faltan, y viceversa.

   Escriba la función ``cuales_me_sirven(lista_quiere, lista_tiene)``
   que entregue el conjunto de las láminas que le faltan a ``lista_quiere``
   y que ``lista_tiene`` tiene repetidas::

    >>> laminas_pepito = [4, 6, 9, 12, 9, 9, 6, 12, 2]
    >>> laminas_yayita = [4, 9, 7, 7, 4, 4, 8]
    >>> cuales_me_sirven(laminas_pepito, laminas_yayita)
    {7}
    >>> cuales_me_sirven(laminas_yayita, laminas_pepito)
    {12, 6}

   A Pepito le falta la lámina 7, que Yayita tiene repetida.
   También le falta la 8, pero ella no la tiene repetida,
   así que no le sirve.
   Yayita tiene repetida la 4,
   pero Pepito ya la tiene,
   así que tampoco le sirve.

#. El sobre de láminas vale $250.
   Pepito quiere saber cuánto va a gastar en láminas
   para completar el álbum.

   Escriba la función ``costo_laminas()``
   que vaya comprando sobres hasta completar las 640 láminas distintas,
   y que retorne cuál fue el gasto total::

    # Si no sale ninguna repetida, el resultado será:
    >>> costo_laminas()
    32000

    # Si salen algunas repetidas:
    >>> costo_laminas()
    54250

    # Muy mala suerte:
    >>> costo_laminas()
    241750

#. Vladimiro es un fanfarrón:
   él desea sacar pica a Yayita
   por las láminas que él tiene
   y que ella no.

   Escriba la función ``tengo_y_tu_no(mis_laminas, tus_laminas)``
   que entregue el conjunto de láminas que
   están en ``mis_laminas`` y no en ``tus_laminas``::

    >>> laminas_vladimiro = [6, 1, 3, 3, 4, 7]
    >>> laminas_yayita = [8, 4, 9, 12, 2, 11, 4, 6, 13, 14]
    >> tengo_y_tu_no(laminas_vladimiro, laminas_yayita)
    {1, 3, 7}

