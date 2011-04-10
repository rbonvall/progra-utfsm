Funciones
=========
Supongamos que necesitamos escribir un programa
que calcule el `número combinatorio`_ `C(m, n)`,
definido como:

.. math::

    C(m, n) = \frac{m!}{(m - n)! n!},

donde `n!` (el factorial_ de `n`)
es el producto de los números enteros desde 1 hasta `n`:

.. math::

    n! = 1\cdot 2\cdot\cdots\cdot(n - 1)\cdot n = \prod_{i=1}^n i

.. _número combinatorio: http://es.wikipedia.org/wiki/Número_combinatorio
.. _factorial: http://es.wikipedia.org/wiki/Factorial

El código para calcular el factorial de un número entero `n`
es sencillo::

    f = 1
    for i in range(1, n + 1):
        f *= i

Sin embargo,
para calcular el número combinatorio,
hay que hacer lo mismo tres veces::

    comb = 1

    # multiplicar por m!
    f = 1
    for i in range(1, m + 1):
        f = f * i
    comb = comb * f

    # dividir por (m - n)!
    f = 1
    for i in range(1, m - n + 1):
        f = f * i
    comb = comb / f

    # dividir por n!
    f = 1
    for i in range(1, n + 1):
        f = f * i
    comb = comb / f

La única diferencia entre los tres cálculos de factoriales
es el valor de término de cada ciclo ``for``
(``m``, ``m - n`` y ``n``, respectivamente).

Escribir el mismo código varias veces es tedioso y propenso a errores.
Además, el código resultante es mucho más dificil de entender,
pues no es evidente a simple vista qué es lo que hace.

Lo ideal sería que existiera una función llamada ``factorial``
que hiciera el trabajo sucio, y que pudiéramos usar de la siguiente manera::

    factorial(m) / (factorial(m - n) * factorial(n))

Ya vimos anteriormente que Python ofrece «de fábrica»
algunas funciones, como ``int``, ``min`` y ``abs``.
Ahora veremos cómo crear nuestras propias funciones.

Funciones
---------
.. index:: función

En programación,
una **función** es una sección de un programa
que calcula un valor
de manera independiente al resto del programa.

.. index:: parámetro (de una función), resultado (de una función), valor de retorno

Una función tiene tres componentes importantes:

* los **parámetros**,
  que son los valores que recibe la función como entrada;
* el **código de la función**,
  que son las operaciones que hace la función; y
* el **resultado** (o **valor de retorno**),
  que es el valor final que entrega la función.

En esencia, una función es un mini programa.
Sus tres componentes son análogos a
la entrada, el proceso y la salida de un programa.

En el ejemplo del factorial,
el parámetro es el entero al que queremos calcularle el factorial,
el código es el ciclo que hace las multiplicaciones,
y el resultado es el valor calculado.

Definición de funciones
~~~~~~~~~~~~~~~~~~~~~~~
Las funciones en Python son creadas mediante la sentencia ``def``::

    def nombre(parámetros):
        # código de la función

Los parámetros son variables
en las que quedan almacenados los valores de entrada.

La función contiene código igual al de cualquier programa.
La diferencia es que, al terminar,
debe entregar su resultado
usando la sentencia ``return``.

Por ejemplo,
la función para calcular el factorial
puede ser definida de la siguiente manera::

    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

En este ejemplo,
el resultado que entrega una llamada a la función
es el valor que tiene la variable ``f``
al llegar a la última línea de la función.

Una vez creada,
la función puede ser usada como cualquier otra,
todas las veces que sea necesario::

    >>> factorial(0)
    1
    >>> factorial(12) + factorial(10)
    482630400
    >>> factorial(factorial(3))
    720
    >>> n = 3
    >>> factorial(n ** 2)
    362880

.. index:: variable local

Las variables que son creadas dentro de la función
(incluyendo los parámetros y el resultado)
se llaman **variables locales**,
y sólo son visibles dentro de la función,
no desde el resto del programa.

.. index:: variable global

Por otra parte,
las variables creadas fuera de alguna función
se llaman **variables globales**,
y son visibles desde cualquier parte del programa.
Sin embargo, su valor no puede ser modificado,
ya que una asignación crearía una variable local
del mismo nombre.

En el ejemplo, las variables locales son ``n``, ``f`` e ``i``.
Una vez que la llamada a la función termina,
estas variables dejan de existir::

    >>> factorial(5)
    120
    >>> f
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    NameError: name 'f' is not defined

Después de definir la función ``factorial``,
podemos crear otra función llamada ``comb``
para calcular números combinatorios::

    def comb(m, n):
        fact_m = factorial(m)
        fact_n = factorial(n)
        fact_m_n = factorial(m - n)
        c = fact_m / (fact_n * fact_m_n)
        return c

Esta función llama a ``factorial`` tres veces,
y luego usa los resultados para calcular su resultado.
La misma función puede ser escrita también de forma más sucinta::

    def comb(m, n):
        return factorial(m) / (factorial(n) * factorial(m - n))

El programa completo es el siguiente:

.. literalinclude:: ../_static/programas/combinatorios.py

(Puede descargarlo aquí_).

.. _aquí: ../_static/programas/combinatorios.py

Note que, gracias al uso de las funciones,
la parte principal del programa ahora tiene sólo cuatro líneas,
y es mucho más fácil de entender.

Múltiples valores de retorno
----------------------------
En Python, una función puede retornar más de un valor.

Por ejemplo,
la siguiente función
recibe una cantidad de segundos,
y retorna el equivalente
en horas, minutos y segundos::

    def convertir_segundos(segundos):
        horas = segundos / (60 * 60)
        minutos = (segundos / 60) % 60
        segundos = segundos % 60
        return horas, minutos, segundos

Al llamar la función,
se puede asignar un nombre a cada uno de los valores retornados::

    >>> h, m, s = convertir_segundos(9814)
    >>> h
    2
    >>> m
    43
    >>> s
    34

Técnicamente, la función está retornando una **tupla** de valores,
un tipo de datos que veremos más adelante::

    >>> convertir_segundos(9814)
    (2, 43, 34)

Funciones que no retornan nada
------------------------------
Una función puede realizar acciones
sin entregar necesariamente un resultado.

Por ejemplo,
si un programa necesita imprimir cierta información muchas veces,
conviene encapsular esta acción en una función que haga los ``print`` ::

    def imprimir_datos(nombre, apellido, rol, dia, mes, anno):
        print 'Nombre completo:', nombre, apellido
        print 'Rol:', rol
        print 'Fecha de nacimiento:', dia, '/', mes, '/', anno

    imprimir_datos('Perico', 'Los Palotes', '201101001-1',  3, 1, 1993)
    imprimir_datos('Yayita', 'Vinagre',     '201101002-2', 10, 9, 1992)
    imprimir_datos('Fulano', 'De Tal',      '201101003-3', 14, 5, 1990)

En este caso,
cada llamada a la función ``imprimir_datos``
muestra los datos en la pantalla, pero no entrega un resultado.
Este tipo de funciones son conocidas en programación
como **procedimientos** o **subrutinas**,
pero en Python son funciones como cualquier otra.

Técnicamente, todas las funciones retornan valores.
En el caso de las funciones que no tienen una sentencia ``return``,
el valor de retorno siempre es ``None``.
Pero como la llamada a la función no aparece en una asignación,
el valor se pierde, y no tiene ningún efecto en el programa.

