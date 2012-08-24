Uso del módulo ``turtle``
=========================

Las funciones para manejar la tortuga
no son parte del lenguaje Python,
sino que son provistas por el módulo ``turtle``.

Vaya ingresando los siguientes ejemplos en la consola
para ver en vivo y en directo cómo se comporta la tortuga.

Primero que todo,
importe las funciones del módulo ``turtle``.
En su tarea,
debe poner esto al principio del programa::

    from turtle import *

Comencemos haciendo que la tortuga realmente parezca tortuga,
y cambiemos su color::

    shape('turtle')
    color('orange')

Ahora hagamos que la tortuga avance 100 píxeles hacia adelante.
Note que al desplazarse va dejando una huella de su mismo color::

    forward(100)

La función ``left(a)`` hace que la tortuga gire
``a`` grados hacia la izquierda.
Seguramente usted podrá deducir sin problemas
qué es lo que hace la función ``right(a)``::

    left(45)
    forward(20)
    left(45)
    forward(50)
    right(90)
    forward(50)
    right(159)

La función ``up()`` «levanta el lápiz».
Cuando el lápiz está levantado,
la tortuga no deja huella al moverse.
Para volver a apoyar el lápiz
se usa la función ``down()``::

    up()
    forward(100)
    down()
    forward(100)


