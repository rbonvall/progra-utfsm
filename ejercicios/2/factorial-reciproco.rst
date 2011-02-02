Factorial recíproco
-------------------

Desarrolle un programa
que contenga una función
llamada:

::

	factorial_reciproco(n)

la cual debe retornar el valor:

.. math::

	\frac{1}{x!}

Por ejemplo:

::

	factorial_reciproco(0)
	1.0
	factorial_reciproco(2)
	0.5
	factorial_reciproco(4)
	0.041666666666666664
	factorial_reciproco(9)
	2.7557319223985893e-06	

Luego, en el mismo programa,
cree una función 

::

	suma_fr(k)

que retorne la suma de los factoriales
recíprocos desde 1 hasta k:

.. math::

	\frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \ldots + \frac{1}{k!}

Por ejemplo:

::

	suma_fr(0)
	1.0
	suma_fr(1)
	2.0
	suma_fr(5)
	2.7166666666666663
	suma_fr(21)
	2.7182818284590455 
