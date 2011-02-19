Supermercado
-------------

Un supermercado tiene la información de sus productos en un
archivo llamado *productos.txt.*
Cada línea del archivo tiene tres datos:

* el código del producto (un numero entero),
* el nombre del producto, y
* el precio del producto.

Los datos están separados por una coma (",").

::

	1265,Reloj,5000
	613,Cuaderno,900
	9801,Vuvuzela,15000
	321,Lapiz,400
	5413,Martillo,3000
	857,Paleta,6000
	612,Pizza,1200


* Escriba una funcion *existe_producto(codigo)*
  que indique si existe en el archivo el producto con el código dado:

::

	>>> existe_producto(321)
	True
	>>> existe_producto(512)
	False

*  Escriba una función *cuenta_menores_que(precio_maximo)*
   que entregue la cantidad de productos cuyo precio es menor que *precio_maximo*:

::


	>>> cuenta_menores_que(1000)
	2
	>>> cuenta_menores_que(7500)
	6
	>>> cuenta_menores_que(300)
	0

* A partir del archivo *productos.txt*, escriba un programa que
  cree un nuevo archivo llamado *nombres.txt*, que tenga sólo
  los nombres de los productos.

::

	Reloj
	Cuaderno
	Vuvuzela
	Lapiz
	Martillo
	Paleta
	Pizza


