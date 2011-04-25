Manos de póker
--------------
En los juegos de naipes,
una carta tiene dos atributos:
un valor (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)
y un palo (♥, ♦, ♣, ♠).

En un programa,
el valor puede ser representado como un número
del 1 al 13,
y el palo como un string:
♥ → ``'C'``,
♦ → ``'D'``,
♣ → ``'T'`` y
♠ → ``'P'``.

Una carta puede ser representada
como una tupla de dos elementos:
el valor y el palo::

    carta1 = (5, 'T')
    carta2 = (10, 'D')

Para simplificar,
se puede representar el as como un 1,
y los «monos» J, Q y K como 11, 12 y 13::

    # as de picas y reina de corazones
    carta3 = (1, 'P')
    carta4 = (12, 'C')

En el juego de póker,
una mano tiene cinco cartas,
lo que en un programa vendría a ser
un conjunto de cinco tuplas::

    mano = {(1, 'P'), (1, 'C'), (1, 'T'), (13, 'D'), (12, 'P')}

#. Un *full* es una mano en que tres cartas tienen el mismo valor,
   y las otras dos tienen otro valor común.
   Por ejemplo, A♠ A♥ 6♣ A♦ 6♦ es un full (tres ases y dos seis),
   pero 2♣ A♥ Q♥ A♦ 6♦ no.

   Escriba la función que indique si la mano es un full::

    >>> mano_1 = {(1, 'P'), (1, 'C'), (6, 'T'), (1, 'D'), (6, 'D')}
    >>> mano_2 = {(2, 'T'), (1, 'C'), (12, 'C'), (1, 'D'), (6, 'D')}
    >>> es_full(mano_1)
    True
    >>> es_full(mano_2)
    False

#. Un *color* es una mano en que todas las cartas tienen el mismo palo.
   Por ejemplo, 8♠ K♠ 4♠ 9♠ 2♠ es un color (todas las cartas son picas),
   pero Q♣ A♥ 5♥ 2♥ 2♦ no lo es.

   Escriba la función que indique si la mano es un color::

    >>> mano_1 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}
    >>> mano_2 = {(12, 'T'), (1, 'C'), (5, 'C'), (2, 'C'), (2, 'D')}
    >>> es_color(mano_1)
    True
    >>> es_color(mano_2)
    False

#. Una *escalera* es una mano en que las cartas tienen valores consecutivos.
   Por ejemplo, 4♠ 7♥ 3♥ 6♣ 5♣ es una escalera (tiene los valores 3, 4, 5, 6 y 7),
   pero Q♣ 7♥ 3♥ Q♥ 5♣ no lo es.

   Escriba la función que indique si la mano es una escalera::

    >>> mano_1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
    >>> mano_2 = {(12, 'T'), (7, 'C'), (3, 'C'), (12, 'C'), (5, 'T')}
    >>> es_escalera(mano_1)
    True
    >>> es_escalera(mano_2)
    False

#. Una *escalera de color* es una escalera en la que todas las cartas
   tienen el mismo palo.
   Por ejemplo, 4♦ 7♦ 3♦ 6♦ 5♦ es una escalera de color
   (son sólo diamantes, y los valores 3, 4, 5, 6 y 7 son consecutivos).

   Escriba la función que indique si la mano es una escalera de color::

    >>> mano_1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
    >>> mano_2 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}
    >>> mano_3 = {(4, 'D'), (7, 'D'), (3, 'D'), (6, 'D'), (5, 'D')}
    >>> es_escalera_de_color(mano_1)
    False
    >>> es_escalera_de_color(mano_2)
    False
    >>> es_escalera_de_color(mano_3)
    True

#. Escriba las funciones
   para identificar las demás `manos del póker`_.

   .. _manos del póker: http://www.poquer.com.es/ranking.html

#. Escriba un programa que pida al usuario ingresar cinco cartas,
   y le indique qué tipo de mano es:

   .. testcase::

     Carta 1: `5D`
     Carta 2: `QT`
     Carta 3: `QD`
     Carta 4: `10P`
     Carta 5: `5C`
     Doble pareja

   .. testcase::

     Carta 1: `KP`
     Carta 2: `KT`
     Carta 3: `8T`
     Carta 4: `KC`
     Carta 5: `2P`
     Trio

   .. testcase::

     Carta 1: `4P`
     Carta 2: `4C`
     Carta 3: `QD`
     Carta 4: `4D`
     Carta 5: `QT`
     Full
