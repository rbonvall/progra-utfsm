Palabras palíndromas
====================

Así como hay `números palíndromos`_,
también hay palabras palíndromas,
que son las que no cambian
al invertir el orden de sus letras.

.. _números palíndromos: es-numero-palindromo.html

Por ejemplo, «reconocer», «Neuquén» y «acurruca» son palíndromos.

1. Escriba un programa que reciba como entrada una palabra
   e indique si es palíndromo o no.
   Para simplificar, suponga que la palabra no tiene acentos
   y todas sus letras son minúsculas:

   .. testcase::

       Ingrese palabra: `sometemos`
       Es palindromo

   .. testcase::

       Ingrese palabra: `rascar`
       No es palindromo

2. Modifique su programa para que reconozca oraciones palíndromas.
   La dificultad radica en que hay que ignorar los espacios:

   .. testcase::

       Ingrese oracion: `dabale arroz a la zorra el abad`
       Es palindromo

   .. testcase::

       Ingrese oracion: `eva usaba rimel y le miraba suave`
       Es palindromo

   .. testcase::

       Ingrese oracion: `puro chile es tu cielo azulado`
       No es palindromo

