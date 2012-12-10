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

Descargue_ el programa
y ejecútelo para convencerse de que funciona correctamente.

.. _Descargue: ../_static/programas/temperatura.py


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
`f` es una **variable**
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

Esto no significa que `15 = 16`.
Una asignación no es una igualdad matemática ni una ecuación.

Por ejemplo, las siguientes asignaciones son correctas,
suponiendo que las variables que aparecen en ellas
ya fueron asignadas previamente::

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

Las siguientes no son asignaciones válidas,
pues no respetan la sintaxis ``nombre = expresión``
(tarea: identifique los errores)::

    n + 1 = 5
    7 = a
    2_pi_r = 2 * pi * r
    area del circulo = pi * r ** 2
    x ** 2 = x * x

Entrada
-------
.. index:: entrada (programa)

La **entrada** es la parte del programa
en que el usuario ingresa datos.

.. index:: raw_input

La manera más simple de ingresar datos
es hacerlo a través del teclado.
La función ``raw_input(mensaje)``
pide al usuario ingresar un valor,
que puede ser asignado a una variable
para ser usado por el programa.
El ``mensaje`` es lo que se mostrará al usuario
antes de que él ingrese el valor.

El valor ingresado por el usuario
siempre es interpretado como texto,
por lo que es de tipo ``str``.
Si es necesario usarlo como si fuera de otro tipo,
hay que convertirlo explícitamente.

Por ejemplo,
en el programa de conversión de temperaturas,
la entrada es realizada por la sentencia::

    f = float(raw_input('Ingrese temperatura en Fahrenheit: '))

Cuando el programa llega a esta línea,
el mensaje ``Ingrese temperatura en Fahrenheit:``
es mostrado al usuario,
que entonces debe ingresar un valor,
que es convertido a un número real
y asociado al nombre ``f``.

Desde esa línea en adelante,
la variable ``f`` puede ser usada en el programa
para referirse al valor ingresado.

Salida
------
.. index:: salida (programa)

La **salida** es la parte del programa
en que los resultados son entregados al usuario.

.. index:: print

La manera más simple de entregar la salida
es mostrando texto en la pantalla.
En Python, la salida del programa es realizada
por la sentencia **print** (*imprimir* en inglés).

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
se está imprimiendo el mensaje ``El equivalente en Celsius es:``
y a continuación, en la misma línea,
el valor de la variable ``c``.

Las comillas sólo sirven para representar un string en el código,
y no forman parte del string.
Al imprimir el string usando ``print``
las comillas no aparecen::

    >>> 'Hola'
    'Hola'
    >>> print 'Hola'
    Hola

Comentarios
-----------
.. index:: comentario, #

Un **comentario** es una sección del código
que es ignorada por el intérprete.
Un comentario puede ser utilizado por el programador
para dejar un mensaje en el código
que puede ser útil para alguien que tenga que leerlo en el futuro.

En Python,
cualquier texto que aparezca a la derecha de un signo ``#``
es un comentario::

    >>> 2 + 3  # Esto es una suma
    5
    >>> # Esto es ignorado
    >>>

La excepción son los signos ``#`` que aparecen en un string::

    >>> "123 # 456" # 789
    '123 # 456'

Evitar que se cierre el programa
--------------------------------

La ejecución de programas en Windows presenta un inconveniente práctico:
cuando el programa termina, la ventana de ejecución se cierra inmediatamente,
por lo que no es posible alcanzar a leer la salida del programa.

Por ejemplo,
al ejecutar el programa ``temperatura.py`` tal como está arriba,
el usuario verá el mensaje ``Ingrese temperatura...``
y a continuación ingresará el valor.
Una vez que el programa entrega como resultado
el equivalente en grados Celcius,
no quedan más sentencias para ejecutar,
por lo que el programa se cierra.

Existen otras maneras de ejecutar programas
con las que este problema no ocurre.
Por ejemplo, al ejecutar un programa desde una IDE,
generalmente la salida aparece en una ventana que no se cierra.

Una solución para evitar que la ventana se cierre
es agregar un ``raw_input()`` al final del código.
De este modo,
el programa quedará esperando que el usuario ingrese cualquier cosa
(un enter basta) antes de cerrarse.

Los programas presentados en este apunte no tendrán el ``raw_input()`` al final,
pero usted puede agregarlo por su cuenta si así lo desea.
En controles y certámenes, no será necesario hacerlo.

