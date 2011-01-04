Ordenamiento
------------

Determinar el orden de tres números ingresados

* **Entrada**

  Tres números enteros.

* **Salida**

  Los tres números ordenados de menor a mayor.

* Comportamiento::

	Ingrese número: 8
	Ingrese número: 1
	Ingrese número: 4
	[1, 4, 8]
	Ingrese números: 1
	Ingrese números: 3
	Ingrese números: 2
	[1, 2, 3]
	Ingrese números: 1
	Ingrese números: 6
	Ingrese números: 7
	[1, 6, 7]

* Solución::
	
	num1 = int(raw_input("Ingrese número: "))
	num2 = int(raw_input("Ingrese número: "))
	num3 = int(raw_input("Ingrese número: "))
	print sorted([num1,num2,num3])
	
