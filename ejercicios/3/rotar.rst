Rotar matrices
==============

#. Escriba la función ``rotar90(a)``
   que retorne el arreglo ``a``
   rotado 90 grados en el sentido contrario
   a las agujas del reloj::

      >>> a = arange(12).reshape((3, 4))
      >>> a
      array([[ 0,  1,  2,  3],
             [ 4,  5,  6,  7],
             [ 8,  9, 10, 11]])
      >>> rotar90(a)
      array([[ 3,  7, 11],
             [ 2,  6, 10],
             [ 1,  5,  9],
             [ 0,  4,  8]])

   Hay dos maneras de hacerlo:
   la larga (usando ciclos anidados)
   y la corta (usando operaciones de arreglos).
   Trate de hacerlo de las dos maneras.

#. Escriba las funciones ``rotar180(a)`` y ``rotar270(a)``::

      >>> rotar180(a)
      array([[11, 10,  9,  8],
             [ 7,  6,  5,  4],
             [ 3,  2,  1,  0]])
      >>> rotar270(a)
      array([[ 8,  4,  0],
             [ 9,  5,  1],
             [10,  6,  2],
             [11,  7,  3]])

   Hay tres maneras de hacerlo:
   la larga (usando ciclos anidados),
   la corta (usando operaciones de arreglos)
   y la astuta.
   Trate de hacerlo de las tres maneras.

#. Escriba el  módulo ``rotar.py``
   que contenga estas tres funciones.
   Le será útil más adelante::

      >>> from rotar import rotar90
      >>> a = array([[6, 3, 8],
      ...            [9, 2, 0]])
      >>> rotar90(a)
      array([[8, 0],
             [3, 2],
             [6, 9]])

