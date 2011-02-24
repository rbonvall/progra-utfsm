Directorio telefónico
---------------------

Un directorio telefónico se estructura sólo utilizando
dos parametros, el "nombre" de la persona y su "telefono".

Realice entonces un programa que cumpla la misma función
de un directorio telefónico, es decirm, agregar entradas,
buscar algún número en particular, eliminar entradas y
poder ver todo el contenido.

Para facilitar el funcionamiento de su programa,
es recomendable utilizar *diccionarios* y *funciones*.

El comportamientos de las funciones debe ser:

::

	>>> agregar_telefono("Fulano Perez",123456)
	Contacto agregado.
	>>> ver_directorio()
	"Fulano Perez" 123456
	>>> agregar_telefono("Maria Merino",912354)
	Contacto agregado.
	>>> ver_directorio()
	"Fulano Perez" 123456
	"Maria Merino" 912354
	>>> buscar("Fulano Perez")
	"Fulano Perez" 123456
	>>> buscar("Juan Perez")
	Contacto no encontrado.	
