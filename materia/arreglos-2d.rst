Arreglos bidimensionales
========================

.. index:: arreglo bidimensional

Los **arreglos bidimensionales**
son tablas de valores.
Cada elemento de un arreglo bidimensional
está simultáneamente en una fila y en una columna.

.. index:: matriz

En matemáticas,
a los arreglos bidimensionales se les llama matrices_,
y son muy utilizados en problemas de Ingeniería.

En un arreglo bidimensional,
cada elemento tiene una posición
que se identifica mediante dos índices:
el de su fila y el de su columna.


Crear arreglos bidimensionales
------------------------------

Los arreglos bidimensionales
también son provistos por NumPy,
por lo que debemos comenzar
importando las funciones de este módulo::

    from numpy import *

Al igual que los arreglos de una dimensión,
los arreglos bidimensionales también pueden ser creados
usando la función ``array``,
pero pasando como argumentos
una lista con las filas de la matriz::

    a = array([[5.1, 7.4, 3.2, 9.9],
               [1.9, 6.8, 4.1, 2.3],
               [2.9, 6.4, 4.3, 1.4]])

Todas las filas deben ser del mismo largo,
o si no ocurre un error de valor::

    >>> array([[1], [2, 3]])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: setting an array element with a sequence.

Los arreglos tienen un atributo llamado ``shape``,
que es una tupla con los tamaños de cada dimensión.
En el ejemplo,
``a`` es un arreglo de dos dimensiones
que tiene tres filas y cuatro columnas::

    >>> a.shape
    (3, 4)

Los arreglos también tienen otro atributo llamado ``size``
que indica cuántos elementos tiene el arreglo::

    >>> a.size
    12

Por supuesto, el valor de ``a.size`` siempre es el producto
de los elementos de ``a.shape``.

Hay que tener cuidado con la función ``len``,
ya que no retorna el tamaño del arreglo,
sino su cantidad de filas::

    >>> len(a)
    3

Las funciones ``zeros`` y ``ones``
también sirven para crear arreglos bidimensionales.
En vez de pasarles como argumento un entero,
hay que entregarles una tupla
con las cantidades de filas y columnas
que tendrá la matriz::

    >>> zeros((3, 2))
    array([[ 0.,  0.],
           [ 0.,  0.],
           [ 0.,  0.]])

    >>> ones((2, 5))
    array([[ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.]])

Lo mismo se cumple para muchas otras funciones
que crean arreglos; por ejemplom la función ``random``::

    >>> from numpy.random import random
    >>> random((5, 2))
    array([[ 0.80177393,  0.46951148],
           [ 0.37728842,  0.72704627],
           [ 0.56237317,  0.3491332 ],
           [ 0.35710483,  0.44033758],
           [ 0.04107107,  0.47408363]])

Operaciones con arreglos bidimensionales
----------------------------------------
Al igual que los arreglos de una dimensión,
las operaciones sobre las matrices
se aplican término a término::

    >>> a = array([[5, 1, 4],
    ...            [0, 3, 2]])
    >>> b = array([[2, 3, -1],
    ...            [1, 0, 1]])

    >>> a + 2
    array([[7, 3, 6],
           [2, 5, 4]])

    >>> a ** b
    array([[25,  1,  0],
          [ 0,  1,  2]])

Cuando dos matrices aparecen en una operación,
ambas deben tener exactamente la misma forma::

    >>> a = array([[5, 1, 4],
    ...            [0, 3, 2]])
    >>> b = array([[ 2,  3],
    ...            [-1,  1],
    ...            [ 0,  1]])
    >>> a + b
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: shape mismatch: objects cannot be broadcast to a single shape



