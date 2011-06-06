Interfaces gráficas
===================

Todo programa necesita contar con algún mecanismo
para recibir la entrada y entregar la salida.
Ya hemos visto dos maneras de hacer entrada:

* entrada por teclado (``raw_input``), y
* entrada por archivo (``for linea in archivo: ...``);

y dos maneras de hacer salida:

* salida por consola (``print``), y
* salida por archivo (``archivo.write(...)``).

.. index:: interfaz gráfica

La mayoría de los programas que ocupamos a diario no funcionan así,
sino que tienen una **interfaz gráfica**,
compuesta por ventanas, menúes, botones y otros elementos,
a través de los cuales podemos interactuar con el programa.

Los programas con interfaces gráficas
son fundamentalmente diferentes a los programas
con interfaces de texto.
Los programas que hemos escrito hasta ahora
se ejecutan completamente de principio a fin,
deteniéndose sólo cuando debemos ingresar datos.

Los programas gráficos, por otra parte,
realizan acciones sólo cuando ocurren
ciertos eventos provocados por el usuario
(como hacer clic en un botón, o escribir algo en una casilla de texto),
y el resto del tiempo se quedan esperando que algo ocurra, sin hacer nada.
El programa no tiene control sobre cuándo debe hacer algo.
Esto requiere que los programas sean estructurados
de una manera especial, que iremos aprendiendo de a poco.

.. index:: Tkinter

Python incluye un módulo llamado ``Tkinter``
que provee todas las funciones necesarias,
que deben ser importadas al principio del programa::

    from Tkinter import *

Creación de la ventana
----------------------
El siguiente programa
es la interfaz gráfica más simple que se puede crear::

    from Tkinter import *
    w = Tk()
    w.mainloop()

Haga la prueba:
copie este programa en el editor de texto,
guárdelo y ejecútelo.
Debería aparecer una ventana vacía:

.. image:: ../diapos/programas/tkinter/capturas/01.png

La sentencia ``w = Tk()``
crea la ventana principal del programa,
y la asigna a la variable ``w``.
Toda interfaz gráfica debe tener una ventana principal
en la que se irán agregando cosas.
Esta línea va al principio del programa.

La sentencia ``w.mainloop()``
indica a la interfaz que debe quedarse esperando
a que el usuario haga algo.
Esta línea siempre debe ir al final del programa.

.. index:: ciclo de eventos

Al ejecutarlo,
puede darse cuenta que el programa no termina.
Esto ocurre porque la llamada al método ``mainloop()``
se «queda pegada» esperando que algo ocurra.
Esto se llama un **ciclo de eventos**,
y es simplemente un ciclo infinito que está continuamente esperando
que algo ocurra.

Todos los programas con interfaz gráfica
deben seguir esta estructura:
la creación de la ventana al principio del programa
y la llamada al ciclo de eventos al final del programa.

Creación de widgets
-------------------
.. index:: widget

Un **widget** es cualquier cosa que uno puede poner en una ventana.
Por ahora, veremos tres tipos de widgets sencillos,
que son suficientes para crear una interfaz gráfica funcional:

* las **etiquetas** (``Label``)
  sirven para mostrar datos,
* los **botones** (``Button``)
  sirven para hacer que algo ocurra en el programa, y
* los **campos de entrada** (``Entry``)
  sirven para ingresar datos al programa.

En un programa en ejecución,
estos widgets se ven así:

.. image:: ../diapos/programas/tkinter/capturas/widgets.png

El ``Entry`` es análogo al ``raw_input``
de los programas de consola:
sirve para que el programa reciba la entrada.
El ``Label`` es análogo al  ``print``:
sirve para que el programa entregue la salida.

Un botón puede ser visto como un «llamador de funciones»:
cada vez que un botón es presionado,
se hace una llamada a la función asociada a ese botón.
Los botones no tienen un análogo,
pues los programas de consola
se ejecutan de principio a fin inmediatamente,
y por esto no necesitan que las llamadas a las funciones
sean gatilladas por el usuario.

Para agregar un widget a un programa,
hay que ocupar las funciones con los nombres de los widgets
(``Label``, ``Button`` y ``Entry``).
Estas funciones reciben como primer parámetro obligatorio
la ventana que contendrá el widget.
Además,
tienen parámetros opcionales
que deben ser pasados usando la sintaxis de asignación
de parámetros por nombre.
Por ejemplo,
el parámetro ``text`` sirve para indicar
cuál es el texto que aparecerá en un botón o en una etiqueta.

Por ejemplo,
la siguiente sentencia
crea un botón con el texto ``Saludar``,
contenido en la ventana ``w``::

    b = Button(w, text='Saludar')

Si bien esto crea el botón
y lo asigna a la variable ``b``,
el botón no es agregado a la ventana ``w`` inmediatamente:
lo que hicimos fue simplemente decirle al botón cuál es su contenedor,
para que lo tenga en cuenta al momento de ser agregado.
Para que esto ocurra,
debemos llamar al método ``pack``,
que es una manera de decirle al widget
«empaquétate dentro de tu contenedor»::

    b.pack()

Como referencia,
el programa que crea la ventana de la imagen
es el siguiente (¡pruébelo!):

.. literalinclude:: ../diapos/programas/tk-widgets.py

Los widgets van siendo apilados verticalmente,
desde arriba hacia abajo,
en el mismo orden en que van siendo apilados.
Ya veremos cómo empaquetarlos en otras direcciones.

Controladores
-------------
(Por escribir)

Modelos
-------
(Por escribir)
