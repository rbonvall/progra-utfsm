Años Bisiestos
--------------

Desarrollar un programa que pueda determinar si un año
es bisiesto o no.

Recuerde que un año bisiesto es cuando dura 366 días,
existiendo un día adicional en el mes más corto,
es decir, el 29 de febrero.

El programa debe tener como entrada un determinado *año*,
y como salida debe decirnos si el *año* ingresado es o no
bisiesto.

* Comportamiento

::

	Ingrese un año: 1988
	True

::

	Ingrese un año: 2010
	False

* Solución

::

    num = int(raw_input("Ingrese un año: "))
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        print True
    else:
        print False
