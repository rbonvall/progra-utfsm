Caballo de ajedrez
==================

Un tablero de ajedrez es una grilla de 8 × 8 casillas.
Cada celda puede ser representada
mediante las coordenadas de su fila y su columna,
numeradas desde 1 hasta 8.

El caballo_ es una pieza que se desplaza en forma de L:
su movimiento consiste en avanzar dos casillas en una dirección
y luego una casilla en una dirección perpendicular a la primera:

.. image:: ../../diagramas/caballo.png

Escriba un programa que reciba como entrada
las coordenadas en que se encuentra un caballo,
y entregue como salida
todas las casillas hacia las cuales
el caballo puede desplazarse.

.. _caballo: http://es.wikipedia.org/wiki/Caballo_(ajedrez)

Todas las coordenadas mostradas deben estar dentro del tablero.

Si la coordenada ingresada por el usuario es inválida,
el programa debe indicarlo.

.. testcase::

    Ingrese coordenadas del caballo.
    Fila: `2`
    Columna: `8`

    El caballo puede saltar de 2 8 a:
    1 6
    3 6
    4 7

.. testcase::

    Ingrese coordenadas del caballo.
    Fila: `3`
    Columna: `4`

    El caballo puede saltar de 3 4 a:
    1 3
    1 5
    2 2
    2 6
    4 2
    4 6
    5 3
    5 5

.. testcase::

    Ingrese coordenadas del caballo.
    Fila: `1`
    Columna: `9`

    Posicion invalida.

