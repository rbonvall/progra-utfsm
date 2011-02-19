Póker
-----
En los juegos de naipes,
una carta tiene dos atributos:
un valor (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
y una pinta (♥, ♦, ♣, ♠).

En un programa,
el valor puede ser representado como un número
del 1 al 13,
y la pinta como un string:
♥ → ``'C'``,
♦ → ``'D'``,
♣ → ``'T'`` y
♠ → ``'P'``.

Una carta puede ser representada
como una tupla de dos elementos:
el valor y la pinta::

    carta1 = (5, 'T')
    carta2 = (10, 'D')

Para simplificar,
se puede representar el as como un 1,
y los «monos» J, Q y K como 11, 12 y 13::

    # as de picas y reina de corazones
    carta3 = (1, 'P')
    carta4 = (12, 'C')

En el juego de póker,
una mano tiene cinco cartas.
Esto sería un conjunto de cinco tuplas::

    mano = {(1, 'P'), (1, 'C'), (1, 'T'), (13, 'D'), (12, 'P')}

**Ejercicio 1:** en el póker,
un *full* es una mano en que tres cartas tienen un valor común,
y las otras dos tienen otro valor común.
Escriba una función que indique
si la mano es un full::

    >>> mano_1 = {(1, 'P'), (1, 'C'), (6, 'T'), (1, 'D'), (6, 'D')}
    >>> mano_2 = {(2, 'T'), (1, 'C'), (12, 'C'), (1, 'D'), (6, 'D')}
    >>> full(mano_1)
    True
    >>> full(mano_2)
    False

**Ejercicio 2:**
un *color* es una mano en que todas las cartas tienen la misma pinta.
Escriba una función que indique
si la mano es un color::

    >>> mano_1 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}
    >>> mano_2 = {(12, 'T'), (1, 'C'), (5, 'C'), (2, 'C'), (2, 'D')}
    >>> color(mano_1)
    True
    >>> color(mano_2)
    False

**Ejercicio 3:**
una *escalera* es una mano en que las cartas tienen valores consecutivos
(por ejemplo: 5, 6, 7, 8 y 9).
Escriba una función que indique
si la mano es una escalera::

    >>> mano_1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
    >>> mano_2 = {(12, 'T'), (7, 'C'), (3, 'C'), (12, 'C'), (5, 'T')}
    >>> escalera(mano_1)
    True
    >>> escalera(mano_2)
    False

