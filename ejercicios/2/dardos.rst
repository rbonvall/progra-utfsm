Checkouts de dardos
===================
Un tablero de dardos está dividido en 20 sectores,
numerados del 1 al 20.
Al tirar un dardo en uno de los sectores,
el puntaje obtenido es el número asociado al sector.

Cada sector tiene una zona de doble puntaje (anillo exterior)
y una de triple puntaje (anillo central).
El centro del tablero (llamado *bull*)
entrega 50 puntos, y el anillo alrededor de él, 25.

.. image:: ../../diagramas/dardos.png

En cada juego de una partida de dardos,
ambos jugadores comienzan con 501 puntos.
En cada turno, un jugador lanza tres dardos,
y descuenta de su total el puntaje obtenido.

El objetivo es llegar exactamente a 0 puntos antes que el contrario.
La única restricción es que el último dardo
debe ser un doble (anillo exterior) o el *bull*.

Escriba un programa que reciba como entrada
el puntaje que le queda a un jugador,
y entregue todas las combinaciones
con las que puede lograr exactamente ese puntaje
lanzando tres dardos o menos,
bajo la restricción que el último
debe ser un doble o un *bull*.

.. testcase::

    Puntaje: `178`
    Imposible

.. testcase::

    Puntaje: `167`
    T20 T19 BULL
    T19 T20 BULL

.. testcase::

    Puntaje: `5`
    3 D1
    2 1 D1
    1 2 D1
    1 D2
    1 D1 D1
    D1 1 D1
    T1 D1

.. testcase::

    Puntaje: `142`
    T20 T20 D11
    T20 T18 D14
    T20 D16 BULL
    T20 T16 D17
    T20 T14 D20
    T20 BULL D16
    D19 T18 BULL
    T19 T19 D14
    T19 T17 D17
    T19 T15 D20
    T18 T20 D14
    T18 D19 BULL
    T18 T18 D17
    T18 T16 D20
    T18 BULL D19
    T17 T19 D17
    T17 T17 D20
    D16 T20 BULL
    T16 T20 D17
    T16 T18 D20
    T15 T19 D20
    T14 T20 D20
    T14 BULL BULL
    BULL T20 D16
    BULL T18 D19
    BULL T14 BULL

Como referencia,
para hacer 100 puntos hay 546 combinaciones
(una de las cuales es ``20 T20 D10``),
y para hacer 132 puntos hay 60 combinaciones
(una de las cuales es ``25 T19 BULL``).

