Dígito verificador
------------------

Desarrolle un programa que
calcule el dígito verificador
de un rol UTFSM.

Para calcular el dígito verificador, se deben
realizar los siguiente pasos:

#. Obtener el rol sin guión ni dígito verificador.
#. Invertir el número. (e.g: de 201012341 a 143210102).
#. Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7,
   si es que se acaban los números, se debe comenzar denuevo,
   por ejemplo, con 143210102:

.. math::

   1\times2+ 4\times3+ 3\times4+ 2\times5+ 1\times6+ 0\times7+ 1\times2+ 0\times3+ 2\times4 = 52

#. Al resultado obtenido, es decir, 52,
   debemos sacarle el módulo 11, es decir:

      52 % 11 = 8

#. Con el resultado obtenido en el paso anterior, debemos restarlo de 11:

      11 − 8 = 3

#. Finalmente, el dígito verificador será el obtenido en la resta: 201012341-3.

