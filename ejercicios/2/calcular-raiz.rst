Calcular la raíz cuadrada
-------------------------

Desarrolle una función que permita calcular aproximadamente
la raíz cuadrada de un número de acuerdo al siguiente procedimiento:

* Se toma el número inicial y se le resta el primer número impar
  (el uno), a este resultado se le resta el siguiente número impar
  y así sucesivamente hasta que el resultado de la resta sea menor
  o igual a cero.
* Si el resultado final es igual a cero se trata de un número con raíz
  entera y estará dada por la cantidad de veces que se hizo la resta,
  incluyendo el cero.
* Si el resultado es menor que cero, el número no tiene raíz perfecta
  y el resultado aproximado (truncado) estará dada por la cantidad de
  veces que se hizo la resta menos uno.

Por ejemplo::

	36

	36 - 1  = 35
	35 - 3  = 32
	32 - 5  = 27
	27 - 7  = 20
	20 - 9  = 11
	11 - 11 = 0

	6 veces
	raíz aproximada: 6

::

	8

	8 - 1 = 7
	7 - 3 = 4
	4 - 5 = -1

	3 veces
	raíz aproximada: 3


La dinámica de la función deberá ser la siguiente::

	>>> raiz_aproximada(25)
	5
	>>> raiz_aproximada(6)
	2
	>>> raiz_aproximada(1)
	1
