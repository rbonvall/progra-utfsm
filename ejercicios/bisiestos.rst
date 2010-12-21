Bisiesto
--------
#. Años bisiestos

 * **Entrada**

   Un año cualquiera.

 * **Salida**

   *True*, si el año es bisiesto, *False*, si el año no es bisiesto.

 * Comportamiento::

	Ingrese un año: 1988
	True
	Ingrese un año: 2010
	False

 * Solución::

	num = int(raw_input("Ingrese un año: "))
	if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
		print True
	else:
		print False


