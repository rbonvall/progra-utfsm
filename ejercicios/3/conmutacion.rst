Matrices que conmutan
=====================

Se dice que dos matrices *A* y *B* **conmutan**
si los productos matriciales entre *A* y *B*
y entre *B* y *A* son iguales.

Por ejemplo, estas dos matrices sí conmutan:

.. math::

    \begin{bmatrix}
      1 & 3 \\ 3 & 2 \\
    \end{bmatrix}
    \begin{bmatrix}
      -1 & 3 \\ 3 & 0 \\
    \end{bmatrix} =
    \begin{bmatrix}
      -1 & 3 \\ 3 & 0 \\
    \end{bmatrix}
    \begin{bmatrix}
      1 & 3 \\ 3 & 2 \\
    \end{bmatrix} =
    \begin{bmatrix}
      8 & 3 \\ 3 & 9 \\
    \end{bmatrix}

Escriba una función que indique si dos matrices conmutan.
Pruebe su función con estos ejemplos::

    >>> a = array([[ 1, 3], [3, 2]])
    >>> b = array([[-1, 3], [3, 0]])
    >>> conmutan(a, b)
    True

    >>> a = array([[3, 1, 2], [9, 2, 4]])
    >>> b = array([[1, 7], [2, 9]])
    >>> conmutan(a, b)
    False


