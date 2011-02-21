Edad
-----

Realice un programa que ingresando su fecha de cumpleaños,
pueda calcular que edad tiene.

Para poder obtener la fecha actual puede acceder al *módulo* ``time``,
y se puede utilizar de la siguiente forma:

::

	>>> import time
	>>> time.strftime("%A %d %B %Y")
	'Sunday 20 February 2011'

Si sólo se quisiera acceder al número de día, número de mes o número de año
se podría realizar de la siguiente forma:

(considerando que hoy fuera 01 de Marzo del 2011)

::

	>>> import time
	>>> time.strftime("%d")
	'01'
	>>> time.strftime("%m")
	'03'
	>>> time.strftime("%Y")
	'2011'

Como pudo notar la fecha es devuelta como *string*,
pero puede ser transformada fácilmente a un *entero*
utilizando la función *int()*:

::

	>>> n = "12"
	>>> print n
	'12'
	>>> print int(n)
	12
