Buscaminas
==========

El juego del buscaminas
se basa en una grilla rectangular
que representa un campo minado.
Algunas de las casillas de la grilla
tienen una mina, y otras no.
El juego consiste en descubrir
todas las casillas que no tienen minas.

En un programa,
podemos representar un campo de buscaminas
como un arreglo en el que las casillas minadas
están marcadas con el valor −1,
y las demás casillas con el valor 0::

    >>> from numpy import *
    >>> campo = array([[ 0,  0, -1,  0,  0,  0,  0,  0],
                       [-1,  0,  0,  0, -1,  0,  0,  0],
                       [ 0,  0,  0,  0, -1,  0,  0, -1],
                       [ 0,  0, -1,  0,  0,  0,  0,  0],
                       [ 0,  0,  0,  0,  0,  0, -1,  0],
                       [ 0, -1,  0,  0, -1,  0,  0,  0],
                       [ 0,  0, -1,  0,  0,  0,  0,  0],
                       [ 0,  0,  0,  0,  0,  0,  0,  0]])



#. Escriba la función ``crear_campo(forma, n)``,
   ``forma`` es una tupla ``(filas, columnas)``,
   que retorne un nuevo campo aleatorio con la forma indicada
   que tenga ``n`` minas.

   Hágalo en los siguientes pasos:

   a. Construya un vector de tamaño ``filas * columnas``
      que tenga ``n`` veces el valor −1, y a continuación sólo ceros.
   b. Importe la función ``shuffle`` desde el módulo ``numpy.random``.
      Esta función desordena (o «baraja») los elementos de un arreglo.
   c. Desordene los elementos del vector que creó.
   d. Cambie la forma del vector.

   ::

      >>> crear_campo((4, 4), 5)
      array([[-1,  0,  0,  0],
             [ 0,  0,  0,  0],
             [ 0, -1, -1,  0],
             [ 0, -1, -1,  0]])
      >>> crear_campo((4, 4), 5)
      array([[ 0,  0, -1,  0],
             [ 0,  0,  0, -1],
             [-1,  0,  0,  0],
             [ 0,  0, -1, -1]])
      >>> crear_campo((4, 4), 5)
      array([[ 0,  0,  0, -1],
             [ 0,  0, -1, -1],
             [-1,  0,  0,  0],
             [ 0,  0, -1,  0]])

#. Al descubrir una casilla no minada,
   en ella aparece un número,
   que indica la cantidad de minas
   que hay en sus ocho casillas vecinas.

   Escriba la función ``descubrir(campo)``
   que modifique el campo
   poniendo en cada casilla
   la cantidad de minas vecinas::

       >>> c = crear_campo((4, 4), 5)
       >>> c
       array([[ 0,  0, -1, -1],
              [ 0,  0, -1,  0],
              [ 0,  0,  0, -1],
              [ 0,  0,  0, -1]])
       >>> descubrir(c)
       >>> c
       array([[ 0,  2, -1, -1],
              [ 0,  2, -1,  4],
              [ 0,  1,  3, -1],
              [ 0,  0,  2, -1]])

