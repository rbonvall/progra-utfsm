Torre y alfil
=============

*Este problema apareció en el certamen 1 del primer semestre de 2011.*

Un tablero de ajedrez es una grilla
de ocho filas y ocho columnas, numeradas de 1 a 8.
Dos de las piezas del juego de ajedrez son el alfil y la torre.
El alfil se desplaza en diagonal,
mientras que la torre se desplaza horizontal o verticalmente.
Una pieza puede ser capturada por otra
si está en una casilla a la cual la otra puede desplazarse:

.. image:: ../../diagramas/torre-alfil.png

Escriba un programa que reciba como entrada
las posiciones en el tablero de un alfil y de una torre,
e indique cuál pieza captura a la otra:

.. testcase::

    Fila alfil: `7`
    Columna alfil: `6`
    Fila torre: `4`
    Columna torre: `3`
    Alfil captura

.. testcase::

    Fila alfil: `3`
    Columna alfil: `4`
    Fila torre: `7`
    Columna torre: `4`
    Torre captura

.. testcase::

    Fila alfil: `3`
    Columna alfil: `3`
    Fila torre: `8`
    Columna torre: `5`
    Ninguna captura

Suponga que los datos ingresados son válidos.
Su programa debe funcionar para tableros de cualquier tamaño.
