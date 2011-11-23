Números primos
==============

Un `número primo`_ es un número natural
que sólo es divisible por 1 y por sí mismo.

Los números que tienen más de un divisor
se llaman números compuestos.
El número 1 no es ni primo ni compuesto.

.. _número primo: http://es.wikipedia.org/wiki/N%C3%BAmero_primo

#. Escriba un programa que reciba como entrada un número natural,
   e indique si es primo o compuesto:

   .. testcase::

      Ingrese un numero: `17`
      17 es primo

   .. testcase::

      Ingrese un numero: `221`
      221 es compuesto

#. Escriba un programa que muestre los `n` primeros números primos,
   donde `n` es ingresado por el usuario:

   .. testcase::

      Cuantos primos: `10`
      2
      3
      5
      7
      11
      13
      17
      19
      23
      29

#. Escriba un programa que muestre los números primos menores que `m`,
   donde `m` es ingresado por el usuario:

   .. testcase::

      Primos menores que: `19`
      2
      3
      5
      7
      11
      13
      17

#. Escriba un programa que cuente cuántos son los números primos menores que `m`,
   donde `m` es ingresado por el usuario:

   .. testcase::

      Contar primos menores que: `1000000`
      Hay 78498 primos menores que 1000000

   En matemáticas, a este valor se le llama `función π`_.

   .. _función π: http://es.wikipedia.org/wiki/Funci%C3%B3n_%CF%80

#. Todos los números naturales mayores que 1
   pueden ser factorizados de una única manera
   como un `producto de divisores primos`_.

   .. _producto de divisores primos: http://es.wikipedia.org/wiki/Factorizaci%C3%B3n_de_enteros

   Escriba un programa que muestre los factores primos
   de un número entero ingresado por el usuario:

   .. testcase::

      Ingrese numero: `204`
      2
      2
      3
      17

   .. testcase::

      Ingrese numero: `8575`
      5
      5
      7
      7
      7

#. La `conjetura de Goldbach`_ sugiere que todo número par mayor que dos
   puede ser escrito como la suma de dos números primos.
   Hasta ahora no se conoce ningún número para el que esto no se cumpla.

   .. _conjetura de Goldbach: http://es.wikipedia.org/wiki/Conjetura_de_Goldbach

   Escriba un programa que reciba un número par como entrada
   y muestre todas las maneras en que puede ser escrito como una suma de dos primos:

   .. testcase::

      Ingrese número par: `338`
      7 + 331
      31 + 307
      61 + 277
      67 + 271
      97 + 241
      109 + 229
      127 + 211
      139 + 199
      157 + 181

   Muestre sólo una de las maneras de escribir cada suma
   (por ejemplo, si muestra 61 + 271, no muestre 271 + 61).

#. Escriba programas que respondan las siguientes preguntas:

   * ¿Cuántos primos menores que diez mil terminan en 7?
   * ¿Cuál es la suma de los cuadrados de los números primos entre 1 y 1000?
     (Respuesta: 49.345.379).
   * ¿Cuál es el producto de todos los números primos menores que 100 que tienen algún dígito 7?
     (Respuesta: 7 × 17 × 37 × 47 × 67 × 71 × 73 × 79 × 97 = 550.682.633.299.463).



