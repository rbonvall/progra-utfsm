Números deleitables
-------------------

Un número de nueve dígitos se dice deleitable si
contiene exactamente los dígitos del 1 al 9,
una sola vez cada uno, y además los números
creados tomando los `n` primeros dígitos
(`n\in [1,9]`) son cada uno de ellos divisibles
por `n`, de tal forma que el primer dígito será
divisible por 1 (siempre lo será), los dos primeros
dígitos forman un número divisible por 2, los tres
primeros uno divisible por 3 y así sucesivamente.

Por ejemplo, si tomamos el número de nueve dígitos
123456789:

.. math::

   1 : 1 = 1
   12 : 2 = 6
   123 : 3 = 41

Sin embargo, esto falla porque 1234 no es divisible
por 4.

Sólo hay un número de nueve dígitos que cumple estas
condiciones.
Desarrolle un programa que permita encontrar tal número.
