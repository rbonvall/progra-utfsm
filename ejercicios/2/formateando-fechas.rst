Formateando fechas
------------------

Realice una función
que sea capaz de recibir una lista
como parámetro, la cual estará compuesta
por distintas fechas de la siguiente forma:

::

	[DD,MM,AAAA,DD,MM,AAAA,DD,MM,AAAA,DD,MM,AAAA, ... ]

La función deberá separar las fechas correspondientes,
y mostrarlas por pantalla de la forma:

::

	DD-MM-AAAA
	DD-MM-AAAA
	DD-MM-AAAA
	...
	DD-MM-AAAA

Controle que el largo de la lista deberá ser un múltiplo de 3.


Recuerde la función *join()* y *str()*.

::
	
	lista = [19,05,1988,25,12,1987,18,11,1964,07,02,1969,06,05,1992]
	formatea_fecha(lista)
	19-05-1988
	25-12-1987
	18-11-1964
	07-02-1969
	06-05-1992

::

	lista = [01,01]
	formatea_fecha(lista)
	Error!
