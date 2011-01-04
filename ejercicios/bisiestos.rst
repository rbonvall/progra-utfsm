Años Bisiestos
--------------

Desarrollar un programa que pueda determinar si un año
es bisiesto o no.

Recuerde que un año bisiesto es cuando dura 366 días,
existiendo un día adicional en el mes más corto,
es decir, el 29 de febrero.

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


