Matrices especiales
===================

#. Una matriz ``a`` es **simétrica**
   si para todo par de índices ``i`` y ``j``
   se cumple que ``a[i, j] == a[j, i]``.

   Escriba la función ``es_simetrica(a)``
   que indique si la matriz ``a``
   es simétrica o no.

   Cree algunas matrices simétricas
   y otras que no lo sean
   para probar su función.

#. Una matriz ``a`` es **antisimétrica**
   si para todo par de índices ``i`` y ``j``
   se cumple que ``a[i, j] == -a[j, i]``
   (note el signo menos).

   Escriba la función ``es_antisimetrica(a)``
   que indique si la matriz ``a``
   es antisimétrica o no.

   Cree algunas matrices antisimétricas
   y otras que no lo sean
   para probar su función.

#. Una matriz ``a`` es **diagonal**
   si todos sus elementos que no están en la diagonal principal
   tienen el valor cero.
   Por ejemplo,
   la siguiente matriz es diagonal:

   .. math:: 

     \begin{bmatrix}
       9 & 0 & 0 & 0 \\
       0 & 2 & 0 & 0 \\
       0 & 0 & 0 & 0 \\
       0 & 0 & 0 & -1 \\
     \end{bmatrix}

   Escriba la función ``es_diagonal(a)``
   que indique si la matriz ``a``
   es diagonal o no.

#. Una matriz ``a`` es **triangular superior**
   si todos sus elementos que están bajo la diagonal principal
   tienen el valor cero.
   Por ejemplo,
   la siguiente matriz es triangular superior:

   .. math:: 

     \begin{bmatrix}
       9 & 1 & 0 & 4 \\
       0 & 2 & 8 & -3 \\
       0 & 0 & 0 & 7 \\
       0 & 0 & 0 & -1 \\
     \end{bmatrix}

   Escriba la función ``es_triangular_superior(a)``
   que indique si la matriz ``a``
   es trangular superior o no.

#. No es dificil adivinar
   qué es lo que es
   una matriz **triangular inferior**.
   Escriba la función ``es_triangular_inferior(a)``.
   Para ahorrarse trabajo,
   llame a ``es_triangular_superior`` desde dentro de la función.

#. Una matriz es **idempotente**
   si el resultado del producto matricial consigo misma
   es la misma matriz.
   Por ejemplo:

   .. math::

        \begin{bmatrix}
           2 & -2 & -4 \\
          -1 &  3 &  4 \\
           1 & -2 & -3 \\
        \end{bmatrix}
        \begin{bmatrix}
           2 & -2 & -4 \\
          -1 &  3 &  4 \\
           1 & -2 & -3 \\
        \end{bmatrix}
        =
        \begin{bmatrix}
           2 & -2 & -4 \\
          -1 &  3 &  4 \\
           1 & -2 & -3 \\
        \end{bmatrix}

   Escriba la función ``es_idempotente(a)``
   que indique si la matriz ``a``
   es idempotente o no.

#. Se dice que dos matrices *A* y *B* **conmutan**
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

   Escriba la función ``conmutan``
   que indique si dos matrices conmutan o no.
   Pruebe su función con estos ejemplos::

       >>> a = array([[ 1, 3], [3, 2]])
       >>> b = array([[-1, 3], [3, 0]])
       >>> conmutan(a, b)
       True

       >>> a = array([[3, 1, 2], [9, 2, 4]])
       >>> b = array([[1, 7], [2, 9]])
       >>> conmutan(a, b)
       False

