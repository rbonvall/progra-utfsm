Trios pitagóricos
------------------

Un trío pitagórico se define como un
conjunto de tres números, *a*, *b* y *c*
que cumplen con la relación.

.. math::

	a^{2} + b^{2} = c^{2}


Desarrolle un programa
que contenga una función
llamada:

::

	son_pitagoricos(a,b,c)

que retorne **True** si *a*, *b* y *c*
son un trío pitagórico, y **False** si no
lo son.

Por ejemplo:

::

	son_pitagoricos(3, 4, 5)
	True
	son_pitagoricos(4, 6, 9)
	False
	son_pitagoricos(5, 12, 13)
	True

A continuación, en el mismo programa cree
una función

::

	pitagoricos()

(sin parámetros) que imprima por pantalla
todos los tríos pitagóricos con valores
menores que 10:

::

	pitagoricos()
	0 0 0
	0 1 1
	0 2 2
	0 3 3
	0 4 4
	0 5 5
	0 6 6
	0 7 7
	0 8 8
	0 9 9
	1 0 1
	2 0 2
	3 0 3
	3 4 5
	4 0 4
	4 3 5
	5 0 5
	6 0 6
	7 0 7
	8 0 8
	9 0 9
