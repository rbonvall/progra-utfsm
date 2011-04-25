Polinomios
----------
Un polinomio_ de grado `n` es una función matemática
de la forma:

.. math::

   p(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 +
          \cdots + a_n x^n,

donde `x` es el parámetro
y `a_0, a_1, \dots, a_n`
son números reales dados.

.. _polinomio: http://es.wikipedia.org/wiki/Polinomio

Algunos ejemplos de polinomios son:

* `p(x) = 1 + 2x + x^2`,
* `q(x) = 4 - 17x`,
* `r(x) = -1 - 5x^3 + 3x^5`,
* `s(x) = 5x^{40} + 2x^{80}`.

Los grados de estos polinomios son, respectivamente, 2, 1, 5 y 80.

Evaluar un polinomio
significa reemplazar `x` por un valor
y obtener el resultado.
Por ejemplo, si evaluamos el polinomio `p`
en el valor `x = 3`,
obtenemos el resultado:

.. math::

   p(3) = 1 + 2\cdot 3 + 3^2 = 16

Un polinomio puede ser representado
como una lista con los valores `a_0, a_1, \dots, a_n`.
Por ejemplo,
los polinomios anteriores
pueden ser representados así
en un programa::

    >>> p = [1, 2, 1]
    >>> q = [4, -17]
    >>> r = [-1, 0, 0, -5, 0, 3]
    >>> s = [0] * 40 + [5] + [0] * 39 + [2]

#. Escriba la función ``grado(p)``
   que entregue el grado de un polinomio::

     >>> grado(r)
     5
     >>> grado(s)
     80

#. Escriba la función ``evaluar(p, x)``
   que evalúe el polinomio ``p``
   (representado como una lista)
   en el valor ``x``::

     >>> evaluar(p, 3)
     16
     >>> evaluar(q, 0.0)
     4.0
     >>> evaluar(r, 1.1)
     -2.82347
     >>> evaluar([4, 3, 1], 3.14)
     23.2796

#. Escriba la función ``sumar_polinomios(p1, p2)``
   que entregue la suma de dos polinomios::

     >>> sumar_polinomios(p, r)
     [0, 2, 1, -5, 0, 3]

#. Escriba la función ``derivar_polinomio(p)``
   que entregue la `derivada de un polinomio`_::

     >>> derivar_polinomio(r)
     [0, 0, -15, 0, 15]

#. Escriba la función ``multiplicar_polinomios(p1, p2)``
   que entregue el producto de dos polinomios::

     >>> multiplicar_polinomios(p, q)
     [4, -9, -30, -17]

.. _derivada de un polinomio: http://www.youtube.com/watch?v=7XQMghs_6vg

