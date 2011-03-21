Módulos
=======

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
    >>> t.forward(10)
    >>> t.left(45)
    >>> t.forward(20)
    >>> t.left(45)
    >>> t.forward(30)
    >>> for i in range(10):
    ... t.right(30)
    ... t.forward(10 * i)
    ...
    >>>

.. _math: http://docs.python.org/library/math.html
.. _random: http://docs.python.org/library/random.html
.. _datetime: http://docs.python.org/library/datetime.html
.. _fractions: http://docs.python.org/library/fractions.html
.. _turtle: http://docs.python.org/library/turtle.html

La lista completa de módulos de Python
puede ser encontrada en la `documentación de la biblioteca estándar`_.

.. _documentación de la biblioteca estándar: http://docs.python.org/library/index.html

Importación de nombres
----------------------
.. index:: import, módulo (uso)

La sentencia ``import`` importa objetos desde un módulo
para poder ser usados en el programa actual.

Una manera de usar ``import`` es importar sólo los nombres específicos
que uno desea utilizar en el programa::

    from math import sin, cos
    print sin(10)
    print cos(20)

En este caso, las funciones ``sin`` y ``cos`` no fueron creadas por nosotros,
sino importadas del módulo de matemáticas, donde están definidas.

La otra manera de usar ``import`` es importando el módulo completo,
y accediendo a sus objetos mediante un punto::

    import math
    print math.sin(10)
    print math.cos(10)

Las dos formas son equivalentes.
Como siempre, hay que optar por la que hace que el programa
sea más fácil de entender.

Creación de módulos
-------------------
.. index:: módulo (creación)

Un módulo sencillo es simplemente un archivo con código en Python.
El nombre del archivo indica cuál es el nombre del módulo.

Por ejemplo, podemos crear un archivo llamado ``pares.py``
que tenga funciones relacionadas con los números pares::

    def es_par(n):
        return n % 2 == 0

    def es_impar(n):
        return not es_par(n)

    def pares_hasta(n):
        return range(0, n, 2)

En este caso, el nombre del módulo es ``pares``.
Para poder usar estas funciones desde otro programa,
el archivo ``pares.py`` debe estar en la misma carpeta
que el programa.

Por ejemplo,
el programa ``mostrar_pares.py``
puede ser escrito así::

    from pares import pares_hasta

    n = int(raw_input('Ingrese un entero: '))
    print 'Los numeros pares hasta', n, 'son:'
    for i in pares_hasta(n):
        print i

Y el programa ``ver_si_es_par.py``
puede ser escrito así::

    import pares

    n = int(raw_input('Ingrese un entero: '))
    if pares.es_par(n):
        print n, 'es par'
    else:
        print n, 'no es par'

Como se puede ver,
ambos programas pueden usar los objetos definidos en el módulo
simplemente importándolos.

Usar módulos como programas
---------------------------
Un archivo con extensión ``.py`` puede ser un módulo o un programa.
Si es un módulo,
contiene definiciones que pueden ser importadas desde un programa o desde otro módulo.
Si es un programa,
contiene código para ser ejecutado.

A veces, un programa también contiene definiciones
(por ejemplo, funciones y variables)
que también pueden ser útiles desde otro programa.
Sin embargo, no pueden ser importadas,
ya que al usar la sentencia ``import``
el programa completo sería ejecutado.
Lo que ocurriría en este caso es que,
al ejecutar el segundo programa,
también se ejecutaría el primero.

Existe un truco para evitar este problema:
siempre que hay código siendo ejecutado,
existe una variable llamada ``__name__``.
Cuando se trata de un programa,
el valor de esta variable es ``'__main__'``,
mientras que en un módulo,
es el nombre del módulo.

Por lo tanto,
se puede usar el valor de esta variable
para marcar la parte del programa
que debe ser ejecutada al ejecutar el archivo,
pero no al importarlo.

Por ejemplo,
el siguiente programa convierte
unidades de medidas de longitud:

.. literalinclude:: ../_static/programas/conversion_unidades.py

Este programa es útil por sí solo,
pero además sus cuatro funciones
y las constantes ``km_por_milla`` y ``cm_por_pulgada``
podrían ser útiles para ser usadas en otro programa.

Al poner el cuerpo del programa
dentro del ``if __name__ == '__main__'``,
el archivo puede ser usado como un módulo.
Si no hiciéramos esto,
cada vez que otro programa importe una función
se ejecutaría el programa completo.

Haga la prueba: `descargue el programa`_ y ejecútelo.
Luego, escriba otro programa que importe alguna de las funciones.
A continuación, haga lo mismo,
pero eliminando el ``if``.

.. _descargue el programa: ../_static/programas/conversion_unidades.py
