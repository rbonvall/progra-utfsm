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

.. _matrices: http://es.wikipedia.org/wiki/Matriz_(matem%C3%A1tica)

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

.. index:: shape

Los arreglos tienen un atributo llamado ``shape``,
que es una tupla con los tamaños de cada dimensión.
En el ejemplo,
``a`` es un arreglo de dos dimensiones
que tiene tres filas y cuatro columnas::

    >>> a.shape
    (3, 4)

.. index:: size

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

.. index:: zeros (bidimensional), ones (bidimensional)

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

Obtener elementos de un arreglo bidimensional
---------------------------------------------
Para obtener un elemento de un arreglo,
debe indicarse los índices de su fila ``i`` y su columna ``j``
mediante la sintaxis ``a[i, j]``::


    >>> a = array([[ 3.21,  5.33,  4.67,  6.41],
                   [ 9.54,  0.30,  2.14,  6.57],
                   [ 5.62,  0.54,  0.71,  2.56],
                   [ 8.19,  2.12,  6.28,  8.76],
                   [ 8.72,  1.47,  0.77,  8.78]])
    >>> a[1, 2]
    2.14

    >>> a[4, 3]
    8.78

    >>> a[-1, -1]
    8.78

    >>> a[0, -1]
    6.41

También se puede obtener secciones rectangulares del arreglo
usando el operador de rebanado con los índices::

    >>> a[2:3, 1:4]
    array([[ 0.54,  0.71,  2.56]])

    >>> a[1:4, 0:4]
    array([[ 9.54,  0.3 ,  2.14,  6.57],
           [ 5.62,  0.54,  0.71,  2.56],
           [ 8.19,  2.12,  6.28,  8.76]])

    >>> a[1:3, 2]
    array([ 2.14,  0.71])

    >>> a[0:4:2, 3:0:-1]
    array([[ 6.41,  4.67,  5.33],
           [ 2.56,  0.71,  0.54]])

    >>> a[::4, ::3]
    array([[ 3.21,  6.41],
           [ 8.72,  8.78]])


Para obtener una fila completa,
hay que indicar el índice de la fila,
y poner ``:`` en el de las columnas
(significa «desde el principio hasta el final»).
Lo mismo para las columnas::

    >>> a[2, :]
    array([ 5.62,  0.54,  0.71,  2.56])

    >>> a[:, 3]
    array([ 6.41,  6.57,  2.56,  8.76,  8.78])

Note que el número de dimensiones
es igual a la cantidad de rebanados
que hay en los índices::

    >>> a[2, 3]      # valor escalar (arreglo de cero dimensiones)
    2.56

    >>> a[2:3, 3]    # arreglo de una dimensión de 1 elemento
    array([ 2.56])

    >>> a[2:3, 3:4]  # arreglo de dos dimensiones de 1 x 1
    array([[ 2.56]])

Otras operaciones
-----------------
.. index:: trasposición, transpose

La **trasposicion** consiste en cambiar las filas por las columnas y viceversa.
Para trasponer un arreglo,
se usa el método ``transpose``::

    >>> a
    array([[ 3.21,  5.33,  4.67,  6.41],
           [ 9.54,  0.3 ,  2.14,  6.57],
           [ 5.62,  0.54,  0.71,  2.56]])

    >>> a.transpose()
    array([[ 3.21,  9.54,  5.62],
           [ 5.33,  0.3 ,  0.54],
           [ 4.67,  2.14,  0.71],
           [ 6.41,  6.57,  2.56]])

.. index:: reshape

El método ``reshape``
entrega un arreglo que tiene los mismos elementos pero otra forma.
El parámetro de ``reshape`` es una tupla
indicando la nueva forma del arreglo::

    >>> a = arange(12)
    >>> a
    array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    >>> a.reshape((4, 3))
    array([[ 0, 1, 2],
           [ 3, 4, 5],
           [ 6, 7, 8],
           [ 9, 10, 11]])

    >>> a.reshape((2, 6))
    array([[ 0, 1, 2, 3, 4, 5],
           [ 6, 7, 8, 9, 10, 11]])

.. index:: diag

La función ``diag`` aplicada a un arreglo bidimensional
entrega la diagonal principal de la matriz
(es decir, todos los elementos de la forma ``a[i, i]``)::

    >>> a
    array([[ 3.21,  5.33,  4.67,  6.41],
           [ 9.54,  0.3 ,  2.14,  6.57],
           [ 5.62,  0.54,  0.71,  2.56]])

    >>> diag(a)
    array([ 3.21,  0.3 ,  0.71])

Además, ``diag`` recibe un segundo parámetro opcional
para indicar otra diagonal que se desee obtener.
Las diagonales sobre la principal son positivas,
y las que están bajo son negativas::

    >>> diag(a, 2)
    array([ 4.67,  6.57])
    >>> diag(a, -1)
    array([ 9.54,  0.54])

La misma función ``diag`` también cumple el rol inverso:
al recibir un arreglo de una dimensión,
retorna un arreglo bidimensional
que tiene los elementos del parámetro en la diagonal::

    >>> diag(arange(5))
    array([[0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 2, 0, 0],
           [0, 0, 0, 3, 0],
           [0, 0, 0, 0, 4]])

Reducciones por fila y por columna
----------------------------------
Algunas operaciones pueden aplicarse tanto al arreglo completo
como a todas las filas o a todas las columnas.

Por ejemplo,
``a.sum()`` entrega la suma de todos los elementos del arreglo.
Además,
se le puede pasar un parámetro para hacer
que la operación se haga por filas o por columnas::

    >>> a = array([[ 4.3,  2.9,  9.1,  0.1,  2. ],
    ...            [ 8. ,  4.5,  6.4,  6. ,  4.3],
    ...            [ 7.8,  3.1,  3.4,  7.8,  8.4],
    ...            [ 1.2,  1.5,  9. ,  6.3,  6.8],
    ...            [ 7.6,  9.2,  3.3,  0.9,  8.6],
    ...            [ 5.3,  6.7,  4.6,  5.3,  1.2],
    ...            [ 4.6,  9.1,  1.5,  3. ,  0.6]])
    >>> a.sum()
    174.4
    >>> a.sum(0)
    array([ 38.8,  37. ,  37.3,  29.4,  31.9])
    >>> a.sum(1)
    array([ 18.4,  29.2,  30.5,  24.8,  29.6,  23.1,  18.8])

El parámetro indica a lo largo de qué dimensión se hará la suma.
El ``0`` significa «sumar a lo largo de las filas».
Pero hay que tener cuidado,
¡por que lo que se obtiene son las sumas de las columnas!
Del mismo modo, ``1`` significa «a lo largo de las columnas,
y lo que se obtiene es el arreglo
con las sumas de cada fila.

Las operaciones ``a.min()`` y ``a.max()``
funcionan del mismo modo::

    >>> a.min()
    0.1
    >>> a.min(0)
    array([ 1.2,  1.5,  1.5,  0.1,  0.6])
    >>> a.min(1)
    array([ 0.1,  4.3,  3.1,  1.2,  0.9,  1.2,  0.6])

``a.argmin()`` y ``a.argmax()`` también::

    >>> a.argmin(0)
    array([3, 3, 6, 0, 6])
    >>> a.argmin(1)
    array([3, 4, 1, 0, 3, 4, 4])
