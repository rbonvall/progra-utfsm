Parte decimal
-------------

Realizar un programa que pueda
determinar la parte decimal de un
número *n* ingresado por el usuario.


::
	
	Ingrese un número: 4.5
	0.5

::

	Ingrese un número: -1.19
	0.19

::
	Ingrese un número: 4
	0.0
	
* Solución

::

	num = float(raw_input("Infrese un número: "))
	print(num-int(int))
	

