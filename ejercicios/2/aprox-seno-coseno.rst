Aproximación de seno y coseno
=============================

La funciones seno y coseno puede ser representadas
mediante sumas infinitas:

.. math::

    \text{sen}(x) =
      \frac{x^1}{1!} -
      \frac{x^3}{3!} +
      \frac{x^5}{5!} -
      \frac{x^7}{7!} +
      \cdots

.. math::

    \text{cos}(x) =
      \frac{x^0}{0!} -
      \frac{x^2}{2!} +
      \frac{x^4}{4!} -
      \frac{x^6}{6!} +
      \cdots

(Éstas son las `series de Taylor`_ en torno a `x=0`
de las funciones seno y coseno,
que usted estudiará en Matemáticas 2).

.. _series de Taylor: http://es.wikipedia.org/wiki/Serie_de_Taylor

Los términos de ambas sumas son cada vez más pequeños,
por lo que tomando algunos de los primeros términos
es posible obtener una buena aproximación.

#. Escriba la función ``factorial_reciproco(n)``,
   que retorne el valor ``1/n!``.
#. Escriba la función ``signo(n)``
   que retorne `1` cuando ``n`` es par
   y `-1` cuando ``n`` es impar.
#. Escriba las funciones ``seno_aprox(x, m)`` y ``coseno_aprox(x, m)``
   que aproximen respectivamente el seno y el coseno
   usando los ``m`` primeros términos de las sumas correspondientes.
   Las funciones deben llamar a las funciones
   ``factorial_reciproco`` y ``signo``.
#. Escriba la función ``error(f_exacta, f_aprox, m, x)``
   que entreguen cuál es la diferencia entre el valor exacto
   de la función ``f_exacta`` y su aproximación con ``m`` términos
   usando la función ``f_aprox`` en `x =` ``x``.

   Por ejemplo,
   el error del seno en `x=2` al usar 20 términos
   se obtendría así::

       >>> from math import sin
       >>> error(sin, seno_aprox, 20, 2)

