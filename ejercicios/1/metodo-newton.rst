Método de Newton
================

*Ejercicio sacado de* [Abel96]_ (fuente_).

.. _fuente: http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_1.1.7
.. _método de Newton: http://es.wikipedia.org/wiki/M%C3%A9todo_de_Newton

El método computacional más común para calcular raíces cuadradas
(y otras funciones también) es el `método de Newton`_
de aproximaciones sucesivas.
Cada vez que tenemos una estimación `y`
del valor de la raíz cuadrada de un número `x`,
podemos hacer una pequeña manipulación
para obtener una mejor aproximación
(una más cercana a la verdadera raíz cuadrada)
promediando `y` con `x/y`.

Por ejemplo,
calculemos la raíz cuadrada de 2
usando la aproximación inicial `\sqrt{2}\approx 1`:

=============== ============================ ==============================
Estimación `y`  Cuociente `x/y`              Promedio
=============== ============================ ==============================
`1`             `2/1      = 2`               `(2      + 1     )/2 = 1.5`
`1.5`           `2/1.5    = 1.3333`          `(1.3333 + 1.5   )/2 = 1.4167`
`1.4167`        `2/1.4167 = 1.4118`          `(1.4118 + 1.4167)/2 = 1.4142`
`1.4142`        ...                          ...
=============== ============================ ==============================

Al continuar este proceso,
obtenemos cada vez mejores estimaciones de la raíz cuadrada.

El algoritmo debe detenerse cuando la estimación es
«suficientemente buena», que debe ser un criterio bien definido.

#. Escriba un programa que reciba como entrada un número real `x`
   y calcule su raíz cuadrada usando el método de Newton.
   El algoritmo debe detenerse cuando
   el cuadrado de la raíz cuadrada estimada
   difiera de `x` en menos de 0,0001.

   (Este criterio de detención no es muy bueno).

#. Escriba un programa que reciba como entrada el número real `x`
   y un número entero indicando
   con cuántas cifras decimales de precisión
   se desea obtener su raíz cuadrada.

   El método de Newton debe detenerse
   cuando las cifras de precisión deseadas
   no cambien de una iteración a la siguiente.

   Por ejemplo, para calcular `\sqrt{2}` con dos cifras de precisión,
   las estimaciones sucesivas son aproximadamente
   1; 1,5; 1,416667 y 1,414216.
   El algoritmo debe detenerse en la cuarta iteración,
   pues en ella las dos primeras cifras decimales
   no cambiaron con respecto a la iteración anterior:

   .. testcase::

       Ingrese x: `2`
       Cifras decimales: `2`
       La raiz es 1.4142156862745097

   (La cuarta aproximación es bastante cercana
   a la verdadera raíz 1.4142135623730951).

.. [Abel96] Harold Abelson, Gerald Jay Sussman.
            *Structure and Interpretation of Computer Programs*.
            2nd Edition.
            MIT Press, 1996.

