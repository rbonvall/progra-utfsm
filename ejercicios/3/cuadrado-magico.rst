Cuadrado mágico
===============

Un `cuadrado mágico`_ es una disposición de números naturales
en una tabla cuadrada, de modo que las sumas de cada columna,
de cada fila y de cada diagonal son iguales.

Los cuadrados mágicos más populares
son aquellos que tienen los números consecutivos desde el 1 hasta `n^2`,
donde `n` es el número de filas y de columnas del cuadrado.

Por ejemplo, el siguiente es un cuadrado mágico
con `n = 4`. Todas sus filas, columnas y diagonales suman 34:

.. image:: ../../diagramas/cuadrado-magico.png

#. Escriba una función que reciba un arreglo cuadrado de enteros de `n\times n`,
   e indique si está conformado por los números consecutivos
   desde 1 hasta `n^2`::

     >>> from numpy import array
     >>> consecutivos(array([[3, 1, 5],
     ...                     [4, 7, 2],
     ...                     [9, 8, 6]]))
     True
     >>> consecutivos(array([[3, 1, 4],
     ...                     [4, 0, 2],
     ...                     [9, 9, 6]]))
     False

#. Escriba una función que reciba un arreglo
   e indique si se trata o no de un cuadrado mágico::

     >>> es_magico(array([[3, 1, 5],
     ...                  [4, 7, 2],
     ...                  [9, 8, 6]]))
     False
     >>> es_magico(array([[2, 7, 6],
     ...                  [9, 5, 1],
     ...                  [4, 3, 8]]))
     True

