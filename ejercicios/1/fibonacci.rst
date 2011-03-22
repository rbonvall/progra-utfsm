Números de Fibonacci
====================

Los `números de Fibonacci`_ `F_k`
son una sucesión de números naturales
definidos de la siguiente manera:

.. math::

    F_0 &= 0, \\
    F_1 &= 1, \\
    F_k &= F_{k - 1} + F_{k - 2}, \qquad\text{cuando } k\ge 2.

.. _números de Fibonacci: http://es.wikipedia.org/wiki/N%C3%BAmeros_de_Fibonacci

En palabras simples,
la sucesión de Fibonacci comienza con 0 y 1,
y los siguientes términos
siempre son la suma de los dos anteriores.

En la siguiente tabla,
podemos ver los números de Fibonacci
desde el 0-ésimo hasta el duodécimo.

=========== == == == == == == == == == == == == === ===
:math:`n`    0  1  2  3  4  5  6  7  8  9 10 11  12 ...
:math:`F_n`  0  1  1  2  3  5  8 13 21 34 55 89 144 ...
=========== == == == == == == == == == == == == === ===

#. Escriba un programa que reciba como entrada un número entero *n*,
   y entregue como salida el *n*-ésimo número de Fibonacci:

   .. testcase::

      Ingrese n: `11`
      F11 = 89

#. Escriba un programa que reciba como entrada un número entero
   e indique si es o no un número de Fibonacci:

   .. testcase::

      Ingrese un numero: `34`
      34 es numero de Fibonacci

   .. testcase::

      Ingrese un numero: `78`
      78 no es numero de Fibonacci

#. Escriba un programa que muestre los *m* primeros números de Fibonacci,
   donde *m* es un número ingresado por el usuario:

   .. testcase::

      Ingrese m: `7`
      Los 7 primeros numeros de Fibonacci son:
      0 1 1 2 3 5 8

