Sudoku
======

El sudoku es un puzzle que consiste en llenar una grilla de 9 × 9
con los dígitos del 1 al 9, de modo que no haya ningún valor repetido
en cada fila, en cada columna y en cada uno de las regiones de 3 × 3
marcadas por las líneas más gruesas.

El sudoku sin resolver tiene algunos de los dígitos puestos de antemano en la grilla.
Cuando el puzzle ha sido resuelto, todas las casillas tienen un dígito,
y entre todos satisfacen las condiciones señaladas.

.. image:: ../../diagramas/sudoku.png

En un programa,
un sudoku resuelto puede ser guardado en un arreglo de 9 × 9::

    from numpy import array
    sr = array([[4, 2, 6, 5, 7, 1, 3, 9, 8],
                [8, 5, 7, 2, 9, 3, 1, 4, 6],
                [1, 3, 9, 4, 6, 8, 2, 7, 5],
                [9, 7, 1, 3, 8, 5, 6, 2, 4],
                [5, 4, 3, 7, 2, 6, 8, 1, 9],
                [6, 8, 2, 1, 4, 9, 7, 5, 3],
                [7, 9, 4, 6, 3, 2, 5, 8, 1],
                [2, 6, 5, 8, 1, 4, 9, 3, 7],
                [3, 1, 8, 9, 5, 7, 4, 6, 2]])

Escriba la función ``solucion_es_correcta(sudoku)``
que reciba como parámetro un arreglo de 9 × 9
representando un sudoku resuelto,
y que indique si la solución es correcta
(es decir, si no hay elementos repetidos
en filas, columnas y regiones)::

    >>> solucion_es_correcta(s)
    True
    >>> s[0, 0] = 9
    >>> solucion_es_correcta(s)
    False

.. 2. (¡Difícil!).
..    Un sudoku sin resolver puede ser representado como un arreglo
..    donde las casillas vacías se marcan con el número cero::
.. 
..     s = array([[0, 2, 0, 5, 0, 1, 0, 9, 0],
..                [8, 0, 0, 2, 0, 3, 0, 0, 6],
..                [0, 3, 0, 0, 6, 0, 0, 7, 0],
..                [0, 0, 1, 0, 0, 0, 6, 0, 0],
..                [5, 4, 0, 0, 0, 0, 0, 1, 9],
..                [0, 0, 2, 0, 0, 0, 7, 0, 0],
..                [0, 9, 0, 0, 3, 0, 0, 8, 0],
..                [2, 0, 0, 8, 0, 4, 0, 0, 7],
..                [0, 1, 0, 9, 0, 7, 0, 6, 0]])
.. 
..    Escriba una función ``resolver(sudoku)``
..    que reciba un sudoku sin resolver
..    y retorne el sudoku resuelto::
.. 
..     >>> resolver(s)
..     array([[4, 2, 6, 5, 7, 1, 3, 9, 8],
..            [8, 5, 7, 2, 9, 3, 1, 4, 6],
..            [1, 3, 9, 4, 6, 8, 2, 7, 5],
..            [9, 7, 1, 3, 8, 5, 6, 2, 4],
..            [5, 4, 3, 7, 2, 6, 8, 1, 9],
..            [6, 8, 2, 1, 4, 9, 7, 5, 3],
..            [7, 9, 4, 6, 3, 2, 5, 8, 1],
..            [2, 6, 5, 8, 1, 4, 9, 3, 7],
..            [3, 1, 8, 9, 5, 7, 4, 6, 2]])
.. 
..    Sugerencia: en vez de intentar resolver el sudoku completo,
..    intente resolver sólo algunas de las casillas
..    (las más sencillas).
