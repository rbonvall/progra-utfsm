.. _programas-simples:

Programas simples
=================

.. index:: sentencia

Un programa es una secuencia de **sentencias**.
Una sentencia representa una instrucción bien definida
que es ejecutada por el computador.
En Python, cada línea del código representa una sentencia.

Hay que distinguir entre:

#. **sentencias simples**: son una única instrucción; y
#. **sentencias de control**: contienen varias otras sentencias,
   que a su vez pueden ser simples o de control.

Las sentencias simples son ejecutadas secuencialmente,
una después de la otra.

.. index:: sintaxis

Todas las sentencias siguen ciertas reglas
acerca de cómo deben ser escritas.
Si no son seguidas,
el programa está incorrecto y no se ejecutará.
A este conjunto de reglas se le denomina **sintaxis**.

A continuación veremos algunas sentencias simples,
con las que se pueden escribir algunos programas sencillos.
Más adelante introduciremos las sentencias de control.

Como ejemplo,
consideremos el siguiente programa,
que pide al usuario ingresar una temperatura en grados Fahrenheit
y entrega como resultado el equivalente en grados Celsius:

.. literalinclude:: ../_static/programas/temperatura.py
   :lines: 1-3

Descargue el programa `temperatura.py`_
y pruébelo para cerciorarse que funciona.

.. _temperatura.py: ../_static/programas/temperatura.py


Salida
------
.. index:: print, salida

En Python, la salida del programa es realizada
por la sentencia **print** (*imprimir* en inglés).
Cada vez que aparece una sentencia ``print`` en el programa,
algún texto es escrito en la pantalla del computador.

Si se desea imprimir un texto tal cual,
la sintaxis es la siguente::

    print valor_a_imprimir

Si los valores a imprimir son varios,
deben ser puestos separados por comas.

Por ejemplo,
el programa de conversión de temperaturas
tiene la siguiente sentencia de salida::

    print 'El equivalente en Celsius es:', c

En este caso,
el mensaje entre comillas es mostrado tal cual aparece,
mientras que el valor ``c`` impreso a continuación
es el que tiene esa variable 
por lo que representa un mensaje que es impreso tal cual aparece.

Otra sentencia de salida que aparece en el programa es::

    print 'La solucion unica es x =', x

En este caso,
``x`` es una variable,
y el valor impreso será el valor que tiene
al momento de ejecutar la sentencia,
como veremos a continuación.

Expresiones y variables
-----------------------
.. index:: expresión

Una **expresión** es una combinación de valores y operaciones
que son evaluados durante la ejecución del algoritmo
para obtener un resultado.

Por ejemplo, ``2 + 3`` es una expresión aritmética
que, al ser evaluada, siempre entrega el valor ``5`` como resultado.
En esta expresión,
``2`` y ``3`` son **valores literales**
y ``+`` es el operador de adición.

En el programa de conversión de temperaturas
aparece la expresión ``(f - 32.0) * (5.0 / 9.0)``,
cuyo resultado depende de cuál es el valor de ``f``
al momento de la evaluación.
A diferencia de los valores literales,
`f` es una **variable**.
que tiene un valor específico que puede ser distinto
cada vez que la expresión es evaluada.

En esta expresión, ``*`` es el operador de multiplicación
y ``/`` el de división.

Una expresión puede ser usada como una sentencia de un programa por sí sola,
pero la mayoría de las veces esto no tiene ningún efecto.
El programa evaluará la expresión, pero no hará nada con el resultado obtenido.

Asignaciones
------------
.. index:: asignación, variable

Una **asignación** es una sentencia que asocia un nombre
al resultado de una expresión.
El nombre asociado al valor se llama **variable**.

La sintaxis de una asignación es la siguiente:

.. code-block:: none

    variable = expresión

Por ejemplo,
el programa de conversión de temperaturas
tiene la siguiente asignación::

    c = (f - 32.0) * (5.0 / 9.0)

Cuando aparece una asignación en un programa,
es interpretada de la siguiente manera:

1. primero la expresión a la derecha del signo ``=`` es evaluada,
   utilizando los valores que tienen en ese momento
   las variables que aparecen en ella;
2. una vez obtenido el resultado,
   el valor de la variable a la izquierda del signo ``=``
   es reemplazado por ese resultado.

Bajo esta interpretación,
es perfectamente posible una asignación como ésta::

    i = i + 1

Primero la expresión ``i + 1`` es evaluada,
entregando como resultado el sucesor del valor actual de ``i``.
A continuación, la variable ``i`` toma el nuevo valor.
Por ejemplo, si ``i`` tiene el valor 15,
después de la asignación tendrá el valor 16.

Esto *no* significa que 15 = 16.
Una asignación no es una igualdad matemática o una ecuación.

Por ejemplo, las siguientes asignaciones son correctas::

    nombre = 'Perico Los Palotes'
    discriminante = b ** 2 - 4 * a * c
    pi = 3.14159
    r = 5.0
    perimetro = 2 * pi * r
    sucesor = n + 1
    a = a
    es_menor = x < 4
    x0 = x1 + x2
    r = 2 * abs(x - x0)
    nombre = raw_input('Ingrese su nombre')

Todas las siguientes asignaciones tienen errores
(tarea: indíquelos)::

    n + 1 = 5
    7 = a
    2_pi_r = 2 * pi * r
    area del circulo = pi * r ** 2
    x ** 2 = x * x

