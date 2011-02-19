Contraseñas
-----------

Actualmente un método muy utilizado
para escoger una contraseña es cambiar
ciertas letras de una determinada palabra
por números, por ejemplo:

::

	me gusta el futbol.

::

	m3 gust4 3l futb0l!

Por lo tanto, para poder hacer más fácil
esta tarea, realice una función que utilizando:

* una frase.
* un diccionario con los caracteres a reemplazar.

pueda entregar la contraseña con los caracteres
reemplazados.

Recuerde la función *replace()*.

::

	frase = "quiero mi password segura."
	diccionario = {'a':4,'e':3,'i':1,'o':0,'.':'?'}
	cambia(frase,diccionaio)
	"qu13r0 m1 p4ssw0rd s3gur4?"

::

	frase = "gatito bonito"
	diccionario = {'t':'n','o':''}
	cambia(frase,diccionario)
	"ganin bonin"


Además, como siempre se desea una contraseña mucho más segura
modifique la función anterior, para poder cambiar los caracteres
sólo una cantidad *n* de veces.

Por ejemplo::

	frase = "pablito clavo un clavito"
	diccionario = {'a':4,'o':0,'i':1}
	cambia(frase,diccionario,1)
	"p4bl1t0 clavo un clavito"
	cambia(frase,diccionario,3)
	"p4bl1t0 cl4v0 un cl4v1t0"
