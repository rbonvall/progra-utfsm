Módulos
=======

Las funciones de Python que hemos estado usando hasta ahora
(

.. index:: módulo, biblioteca

Un **módulo** (o **biblioteca**) es una colección de definiciones
de variables, funciones y tipos (entre otras cosas)
que pueden ser importadas para ser usadas desde cualquier programa.

Ya hemos visto algunos ejemplos de cómo usar módulos,
particularmente el módulo matemático,
del que podemos importar funciones
como la exponencial y el coseno,
y las constantes π y *e*::

    >>> from math import exp, cos
    >>> from math import pi, e
    >>> print cos(pi / 3)
    0.5

Las ventajas de usar módulos son:

* las funciones y variables deben ser definidas sólo una vez,
  y luego pueden ser utilizadas en muchos programas
  sin necesidad de reescribir el código;
* permiten que un programa pueda ser organizado en varias secciones lógicas,
  puestas cada una en un archivo separado;
* hacen más fácil compartir componentes con otros programadores.

Python viene «de fábrica» con muchos módulos listos para ser usados.
Además, es posible descargar de internet e instalar módulos
prácticamente para hacer cualquier cosa.
Por último, aprenderemos a crear nuestros propios módulos.

Módulos presentes en Python
---------------------------
Éstos son algunos de los módulos estándares de Python,
que pueden ser usado desde cualquier programa.

El módulo math_ contiene funciones y constantes matemáticas::

    >>> from math import floor, radians
    >>> floor(-5.9)
    -6.0
    >>> radians(180)
    3.1415926535897931

El módulo random_ contiene funciones para producir números aleatorios
(es decir, al azar)::

    >>> from random import choice, randrange, 
    >>> choice(['cara', 'sello'])
    'cara'
    >>> choice(['cara', 'sello'])
    'sello'
    >>> choice(['cara', 'sello'])
    'sello'
    >>> randrange(10)
    7
    >>> randrange(10)
    2
    >>> randrange(10)
    5
    >>> r = range(5)
    >>> r
    [0, 1, 2, 3, 4]
    >>> shuffle(r)
    >>> r
    [4, 2, 0, 3, 1]

El módulo datetime_ provee tipos de datos
para manipular fechas y horas::

    >>> from datetime import date
    >>> hoy = date(2011, 5, 31)
    >>> fin_del_mundo = date(2012, 12, 21)
    >>> (fin_del_mundo - hoy).days
    570

El módulo fractions_ provee un tipo de datos
para representar números racionales::

    >>> from fractions import Fraction
    >>> a = Fraction(5, 12)
    >>> b = Fraction(9, 7)
    >>> a + b
    Fraction(143, 84)

El módulo turtle_ permite manejar una tortuga
(¡haga la prueba!)::

    >>> from turtle import Turtle
    >>> t = Turtle()

.. _math: http://docs.python.org/library/math.html
.. _random: http://docs.python.org/library/random.html
.. _datetime: http://docs.python.org/library/datetime.html
.. _fractions: http://docs.python.org/library/fractions.html
.. _turtle: http://docs.python.org/library/turtle.html

