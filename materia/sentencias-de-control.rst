.. _sentencias de control:

Sentencias de control
=====================

Un programa es una sucesión de **sentencias**
que son ejecutadas secuencialmente.

Por ejemplo, el siguiente programa tiene cuatro sentencias::

    n = int(raw_input('Ingrese n: '))
    m = int(raw_input('Ingrese m: '))
    suma = n + m
    print 'La suma de n y m es:', suma

Las primeras tres son asignaciones,
y la última es una llamada a función.
Al ejecutar el programa,
cada una de estas sentencias es ejecutada,
una después de la otra, una sola vez.

.. index:: sentencia de control

Además de las sentencias simples,
que son ejecutadas en secuencia,
existen las **sentencias de control**
que permiten modificar el flujo del programa
introduciendo ciclos y condicionales.

.. index:: condicional

Un **condicional** es un conjunto de sentencias
que pueden o no ejecutarse,
dependiendo del resultado de una condición.

.. index:: ciclo

Un **ciclo** es un conjunto de sentencias
que son ejecutadas varias veces,
hasta que una condición de término es satisfecha.

.. index:: indentación

Tanto los condicionales como los ciclos
contienen a otras sentencias.
Para indicar esta relación
se utiliza la **indentación**:
las sentencias contenidas
no se escriben en la misma columna
que la sentencia de control,
sino un poco más a la derecha::

    n = int(raw_input())
    m = int(raw_input())
    if m < n:
        t = m
        m = n
        n = t
    print m, n

En este ejemplo, las tres asignaciones
están contenidas dentro de la sentencia de control ``if``.
El ``print m, n`` no está indentado,
por lo que no es parte de la sentencia ``if``.

Este programa tiene cuatro sentencias,
de las cuales la tercera es una sentencia de control,
que contiene a otras tres sentencias.

Para indentar,
utilizaremos siempre cuatro espacios.


Condicional if
--------------
.. index:: if

La sentencia **if** («si»)
ejecuta las instrucciones
sólo si se cumple una condición.
Si la condición es falsa,
no se hace nada:

.. image:: ../diagramas/if.png
   :alt: (Diagrama de flujo if)

La sintaxis es la siguiente::

    if condición:
        sentencias

Por ejemplo,
el siguente programa felicita a alguien
que aprobó la asignatura::

    nota = int(raw_input('Ingrese su nota: '))
    if nota >= 55:
        print 'Felicitaciones'

Ejecute este programa,
probando varias veces con valores diferentes.

Condicional if-else
-------------------
.. index:: if-else

La sentencia **if-else** («si-o-si-no»)
decide qué instrucciones ejecutar
dependiendo si una condición es verdadera o falsa:

.. image:: ../diagramas/if-else.png
   :alt: (Diagrama de flujo if-else)

La sintaxis es la siguiente::

    if condición:
        qué hacer cuando la condición es verdadera
    else
        qué hacer cuando la condición es falsa

Por ejemplo,
el siguiente programa indica a alguien si es mayor de edad::

    edad = int(raw_input('Cual es su edad? '))
    if edad < 18:
        print 'Usted es menor de edad'
    else:
        print 'Usted es adulto'

El siguiente programa realiza acciones distintas
dependiendo de si el número de entrada
es par o impar::

    n = int(raw_input('Ingrese un numero: '))
    if n % 2 == 0:
        print 'El numero es par'
        print 'La mitad del numero es', n / 2
    else:
        print 'El numero es impar'
        print 'El sucesor del numero es', n + 1
    print 'Listo'

La última sentencia no está indentada,
por lo que no es parte del condicional,
y será ejecutada siempre.

Condicional if-elif-else
------------------------
.. index:: if-elif-else

La sentencia **if-elif-else**
depende de dos o más condiciones,
que son evaluadas en orden.
La primera que es verdadera
determina qué instrucciones serán ejecutadas:

.. image:: ../diagramas/if-elif-else.png
   :alt: (Diagrama de flujo if-elif-else)

La sintaxis es la siguiente::

    if condición1:
        qué hacer si condición1 es verdadera
    elif condición2:
        qué hacer si condición2 es verdadera
    ...
    else:
        qué hacer cuando ninguna de las
        condiciones anteriores es verdadera

El último ``else`` es opcional.

Por ejemplo,
la tasa de impuesto a pagar por una persona según su sueldo
puede estar dada por la siguiente tabla:

====================== ====================
**sueldo**             **tasa de impuesto**
---------------------- --------------------
menos de 1000                            0%
1000 ≤ sueldo < 2000                     5%
2000 ≤ sueldo < 4000                    10%
4000 o más                              12%
====================== ====================

Entonces, el programa que calcula el impuesto a pagar
es el siguiente::

    sueldo = int(raw_input('Ingrese su sueldo: '))
    if sueldo < 1000:
        tasa = 0.00
    elif sueldo < 2000:
        tasa = 0.05
    elif sueldo < 4000:
        tasa = 0.10
    else:
        tasa = 0.12
    print 'Usted debe pagar', tasa * sueldo, 'de impuesto'

Siempre sólo una de las alternativas será ejecutada.
Apenas una de las condiciones es verdadera,
el resto de ellas no siguen siendo evaluadas.

Otra manera de escribir el mismo programa
usando sólo sentencias ``if`` es la siguiente::

    sueldo = int(raw_input('Ingrese su sueldo: '))
    if sueldo < 1000:
        tasa = 0.00
    if 1000 <= sueldo < 2000:
        tasa = 0.05
    if 2000 <= sueldo < 4000:
        tasa = 0.10
    if 4000 < sueldo:
        tasa = 0.12
    print 'Usted debe pagar', tasa * sueldo, 'de impuesto'

Esta manera es menos clara,
porque no es evidente a primera vista
que sólo una de las condiciones será verdadera.

Ciclo while
-----------
.. index:: while

El ciclo **while**
(«mientras»)
ejecuta una secuencia de instrucciones
mientras una condición sea verdadera:

.. image:: ../diagramas/while.png
   :alt: (Diagrama de flujo while)

La condición es evaluada antes de cada iteración.
Si la condición es inicialmente falsa,
el ciclo no se ejecutará ninguna vez.

La sintaxis es la siguiente::

    while condición:
        sentencias

Por ejemplo,
el siguiente programa
multiplica dos números enteros
sin usar el operador ``*``::

    m = int(raw_input())
    n = int(raw_input())
    p = 0
    while m > 0:
        m = m - 1
        p = p + n
    print 'El producto de m y n es', p

Para ver cómo funciona este programa,
hagamos un ruteo con la entrada ``m`` = 4
y ``n`` = 7:

   +-------+-------+-------+
   | ``p`` | ``m`` | ``n`` |
   +=======+=======+=======+
   |       |     4 |       |
   +-------+-------+-------+
   |       |       |     7 |
   +-------+-------+-------+
   |     0 |       |       |
   +-------+-------+-------+
   |       |     3 |       |
   +-------+-------+-------+
   |     7 |       |       |
   +-------+-------+-------+
   |       |     2 |       |
   +-------+-------+-------+
   |    14 |       |       |
   +-------+-------+-------+
   |       |     1 |       |
   +-------+-------+-------+
   |    21 |       |       |
   +-------+-------+-------+
   |       |     0 |       |
   +-------+-------+-------+
   |    28 |       |       |
   +-------+-------+-------+

En cada iteración,
el valor de ``m`` decrece en 1.
Cuando llega a 0,
la condición del ``while`` deja de ser verdadera
por lo que el ciclo termina.
De este modo,
se consigue que el resultado sea
sumar ``m`` veces el valor de ``n``.

Note que el ciclo no termina apenas el valor de ``m`` pasa a ser cero.
La condición es evaluada una vez que la iteración completa ha terminado.

Ciclo for con rango
-------------------
.. index:: for, variable de control

El ciclo **for con rango**
ejecuta una secuencia de sentencias
una cantidad fija de veces.

Para llevar la cuenta,
utiliza una **variable de control**
que toma valores distintos en cada iteración.

Una de las sintaxis para usar un ``for``
con rango es la siguiente::

    for variable in range(fin):
        qué hacer para cada valor de la variable de control

En la primera iteración,
la variable de control toma el valor 0.
Al final de cada iteración,
el valor de la variable aumenta automáticamente.
El ciclo termina justo antes que la variable
tome el valor ``fin``.

Por ejemplo,
el siguiente programa muestra los cubos
de los números del 0 al 20::

    for i in range(21):
        print i, i ** 3

.. index:: range, rango

En general,
un **rango** es una sucesión de números enteros equiespaciados.
Incluyendo la presentada más arriba,
hay tres maneras de definir un rango::

    range(final)
    range(inicial, final)
    range(inicial, final, incremento)

El valor inicial siempre es parte del rango.
El valor final nunca es parte del rango.
El incremento indica la diferencia
entre dos valores consecutivos del rango.

Si el valor inicial es omitido, se supone que es 0.
Si el incremento es omitido, se supone que es 1.

Con algunos ejemplos quedará más claro:

==================== ===================================
``range(9)``         0, 1, 2, 3, 4, 5, 6, 7, 8
``range(3, 13)``     3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
``range(3, 13, 2)``  3, 5, 7, 9, 11
``range(11, 4)``     ningún valor
``range(11, 4, -1)`` 11, 10, 9, 8, 7, 6, 5
==================== ===================================

Usando un incremento negativo,
es posible hacer ciclos que van hacia atrás::

    for i in range(10, 0, -1):
        print i
    print 'Feliz anno nuevo!'


.. Una regla general para saber qué ciclo conviene usar es:
.. el ``for`` se ocupa cuando se sabe de antemano cuántas iteraciones serán ejecutadas,
.. y el ``while`` cuando esto no es conocido.


.. El iterable de un ``for`` también puede ser un string.
.. En este caso,
.. los valores que toma la variable de control
.. son cada uno de los símbolos que son parte del string.
..
.. Por ejemplo,
.. el siguiente programa le dice al usuario
.. cuántas veces aparece la letra *e* en su nombre::
..
..     nombre = input('Escriba su nombre: ')
..     n = 0
..     for letra in nombre:
..         if letra == 'e' or letra == 'E':
..             n = n + 1
..     print('La letra e aparece', n, 'veces en su nombre')
..
.. También es posible usar una lista como iterable.
.. Las listas (que veremos en detalle más adelante)
.. son representadas entre corchetes,
.. con sus valores separados por comas.
..
.. Por ejemplo,
.. el siguiente programa
.. muestra el largo de los nombres de varios animales::
..
..     for animal in ['perro', 'gato', 'vaca', 'hamster']:
..         largo_nombre = len(animal)
..         print(animal, 'tiene largo', largo_nombre)
..
.. La salida del programa es::
..
..     perro tiene largo 5
..     gato tiene largo 4
..     vaca tiene largo 4
..     hamster tiene largo 7
