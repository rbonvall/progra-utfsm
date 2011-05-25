Productos entre arreglos
========================

Recordemos que **vector** es sinónimo de arreglo de una dimensión,
y **matriz** es sinónimo de arreglo de dos dimensiones.

(Material en preparación)


Producto interno (vector-vector)
--------------------------------
El **producto interno** entre dos vectores
es la suma de los productos entre elementos correspondientes:

.. image:: ../diagramas/producto-interno.png
   :center:

Producto matriz-vector
----------------------
El **producto matriz-vector**
es el vector de los productos internos
entre las filas de la matriz y el vector:

.. image:: ../diagramas/matriz-vector.png
   :center:

Producto matriz-matriz
----------------------
El **producto matriz-matriz**
es la matriz de los productos internos
entre las filas de la primera matriz
y las columnas de la segunda:

.. image:: ../diagramas/matriz-matriz.png
   :center:


::

    dot(vector, vector) → número
    dot(matriz, vector) → vector
    dot(matriz, matriz) → matriz


