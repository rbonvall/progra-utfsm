Ordenamiento
------------

Realizar un programa que pueda
determinar la secuencia ordenada
de tres números ingresados por
el usuario, de menor a mayor.


::

	Ingrese número: 8
	Ingrese número: 1
	Ingrese número: 4
	[1, 4, 8]

::

	Ingrese números: 1
	Ingrese números: 3
	Ingrese números: 2
	[1, 2, 3]

::

	Ingrese números: 1
	Ingrese números: 6
	Ingrese números: 7
	[1, 6, 7]

* Solución

::
	
	num1 = int(raw_input("Ingrese número: "))
	num2 = int(raw_input("Ingrese número: "))
	num3 = int(raw_input("Ingrese número: "))
	print sorted([num1,num2,num3])
	
