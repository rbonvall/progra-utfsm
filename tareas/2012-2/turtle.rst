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

La función ``goto(x, y)`` lleva a la tortuga
al punto `(x, y)` en el plano,
independientemente de cuál es su posición actual::

    goto(-200, 0)
    goto(-200, 200)
    goto(0, 200)
    goto(-100, 100)

La función ``seth(a)`` cambia la orientación de la tortuga.
Pruebe y verifique a qué dirección queda apuntando la tortuga
al hacer las siguientes llamadas::

    seth(0)
    seth(90)
    seth(180)
    seth(270)

Con estas funciones ya puede resolver la `tarea 1`_.

Si quiere aprender más sobre ``turtle``
y quizás buscar otras funciones que le podrían servir,
revise la `documentación oficial`_ del módulo.

.. _tarea 1: tarea-1.html
.. _documentación oficial: http://docs.python.org/library/turtle.html

