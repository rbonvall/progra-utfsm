.. _expresiones:

Expresiones
===========
.. index:: expresión

Una **expresión** es una combinación de valores y operaciones
que, al ser evaluados, entregan un valor.

.. index:: literal, variable, operador, llamada a función, expresión

Algunos elementos que pueden formar parte de una expresión son:
valores **literales** (como ``2``, ``"hola"`` o ``5.7``),
**variables**, **operadores** y **llamadas a funciones**.

Por ejemplo,
la expresión ``4 * 3 - 2``
entrega el valor 10 al ser evaluada por el intérprete::

    >>> 4 * 3 - 2
    10

El valor de la siguiente expresión
depende del valor que tiene la variable ``n``
en el momento de la evaluación::

    >>> n / 7 + 5

Una expresión está compuesta de otras expresiones,
que son evaluadas recursivamente
hasta llegar a sus componentes más simples,
que son los literales y las variables.

Operadores
----------
.. index:: operador, operador unario, operador binario, operando

Un **operador** es un símbolo en una expresión
que representa una operación aplicada a los valores sobre los que actúa.

Los valores sobre los que actúa un operador se llaman **operandos**.
Un **operador binario** es el que tiene dos operandos, mientras que
un **operador unario** es el que tiene sólo uno.

Por ejemplo,
en la expresión ``2.0 + x``
el operador ``+`` es un operador binario
que en este contexto representa la operación de adición.
Sus operandos son ``2.0`` y ``x``.

Las operaciones más comunes se pueden clasificar en:
aritméticas, relacionales, lógicas y de texto.

Operadores aritméticos
~~~~~~~~~~~~~~~~~~~~~~
.. index:: operación aritmética

Las **operaciones aritméticas** son las que operan sobre valores numéricos
y entregan otro valor numérico como resultado.
Los valores numéricos son los que tienen tipo entero, real o complejo.

.. index:: + (suma), - (resta), /, %, ** , *
.. index:: suma, resta, multiplicación, división, módulo, potencia

Las siguientes son algunas operaciones aritméticas básicas,
junto con el operador que las representa en Python:

* la **suma** ``+``;
* la **resta** ``-``;
* la **multiplicación** ``*``;
* la **división** ``/``;
* el **módulo** ``%`` (resto de la división);
* la **potencia** ``**`` («elevado a»).

En general,
si los operandos son de tipo entero,
el resultado también será de tipo entero.
Pero basta que uno de los operandos sea real
para que el resultado también lo sea::

    >>> 8 - 5
    3
    >>> 8 - 5.0
    3.0
    >>> 8.0 - 5
    3.0
    >>> 8.0 - 5.0
    3.0

Esta regla suele causar confusión en el caso de la división.
Al dividir números enteros,
el resultado siempre es entero,
y es igual al resultado real **truncado**,
es decir, sin su parte decimal::

    >>> 5 / 2
    2
    >>> 5 / -2
    -3

Si uno de los operandos es complejo,
el resultado también será complejo::

    >>> 3 + 4
    7
    >>> 3 + (4+0j)
    (7+0j)

El operador de módulo entrega el resto de la división
entre sus operandos::

    >>> 7 % 3
    1

Un uso bastante común del operador de módulo
es usarlo para determinar si un número es divisible por otro::

    >>> 17 % 5   # 17 no es divisible por 5
    2
    >>> 20 % 5   # 20 si es divisible por 5
    0

Una relación entre ``/`` y ``%`` que siempre se cumple
para los números enteros es::

    (a / b) * b + (a % b) == a

.. index:: + (positivo), - (negativo), positivo, negativo

Hay dos operadores aritméticos unarios:

* el **positivo** ``+``, y
* el **negativo** ``-``.

El positivo entrega el mismo valor que su operando,
y el negativo también pero con el signo cambiado::

    >>> n = -4
    >>> +n
    -4
    >>> -n
    4

Operaciones relacionales
~~~~~~~~~~~~~~~~~~~~~~~~
.. index:: operación relacional, comparación

Las **operaciones relacionales** sirven para comparar valores.
Sus operandos son cualquier cosa que pueda ser comparada,
y sus resultados siempre son valores lógicos.

Algunas operaciones relacionales son:

* el **igual a** ``==`` (no confundir con el ``=`` de las asignaciones);
* el **distinto a** ``!=``;
* el **mayor que** ``>``;
* el **mayor o igual que** ``>=``;
* el **menor que** ``<``;
* el **menor o igual que** ``<=``;

Algunos ejemplos en la consola interactiva::

    >>> a = 5
    >>> b = 9
    >>> c = 14
    >>> a < b
    True
    >>> a + b != c
    False
    >>> 2.0 == 2
    True
    >>> 'amarillo' < 'negro'
    True

Los operadores relacionales pueden ser encadenados,
como se usa en matemáticas,
de la siguiente manera::

    >>> x = 4
    >>> 0 < x <= 10
    True
    >>> 5 <= x <= 20
    False

La expresión ``0 < x <= 10``
es equivalente a ``(0 < x) and (x <= 10)``

Operaciones lógicas
~~~~~~~~~~~~~~~~~~~
.. index:: operación lógica, operación booleana

Los **operadores lógicos** son los que tienen operandos y resultado
de tipo lógico.

En Python, hay tres operaciones lógicas:

.. index:: and, or, not

* la conjunción lógica **and** (en español: «y»),
* la disyunción lógica **or** (en español: «o»), y
* la negación lógica **not** (en español: «no»).

Los operadores ``and`` y ``or`` son binarios, mientras que ``not`` es unario::

    >>> True and False
    False
    >>> not True
    False

La siguiente tabla muestra todos los resultados posibles
de las operaciones lógicas.
Las primeras dos columnas representan los valores de los operandos,
y las siguientes tres, los resultados de las operaciones.

========= ========= =========== ========== =========
``p``     ``q``     ``p and q`` ``p or q`` ``not p``
--------- --------- ----------- ---------- ---------
``True``  ``True``  ``True``    ``True``   ``False``
``True``  ``False`` ``False``   ``True``
``False`` ``True``  ``False``   ``True``   ``True``
``False`` ``False`` ``False``   ``False``
========= ========= =========== ========== =========

Operaciones de texto
~~~~~~~~~~~~~~~~~~~~
Los operadores ``+`` y ``*`` tienen otras interpretaciones
cuando sus operandos son strings.

.. index:: concatenación (strings), + (concatenación)

``+`` es el operador de **concatenación** de strings:
pega dos strings uno después del otro::

    >>> 'perro' + 'gato'
    'perrogato'

La concatenación no es una suma.
Ni siquiera es una operación conmutativa.

.. index:: repetición (strings), + (repetición)

``*`` es el operador de **repetición** de strings.
Recibe un operando string y otro entero,
y entrega como resultado el string repetido tantas veces como indica el entero::

    >>> 'waka' * 2
    'wakawaka'

Más adelante veremos muchas más operaciones para trabajar sobre texto.
Por ahora utilizaremos las más elementales.
Otras operaciones que pueden serle útiles por el momento son:

* obtener el `i`-ésimo caracter de un string (partiendo desde cero)
  usando los corchetes::

    >>> nombre = 'Perico'
    >>> nombre[0]
    'P'
    >>> nombre[1]
    'e'
    >>> nombre[2]
    'r'

* comprarar strings alfabéticamente
  con los operadores relacionales
  (lamentablemente no funciona con acentos y eñes)::

    >>> 'a' < 'abad' < 'abeja'
    True
    >>> 'zapato' <= 'alpargata'
    False

* obtener el largo de un string con la función ``len``::

    >>> len('papalelepipedo')
    14
    >>> len("")
    0

* verificar si un string está dentro de otro
  con el operador ``in``::

   >>> 'pollo' in 'repollos'
   True
   >>> 'pollo' in 'gallinero'
   False

Precedencia
-----------
.. index:: precedencia de operadores, paréntesis

La **precedencia de operadores**
es un conjunto de reglas que especifica
en qué orden deben ser evaluadas
las operaciones de una expresión.

La precedencia está dada por la siguiente lista,
en que los operadores han sido listados
en orden de menor a mayor precedencia:

* ``or``
* ``and``
* ``not``
* ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``
* ``+``, ``-`` (suma y resta)
* ``*``, ``/``, ``%``
* ``+``, ``-`` (positivo y negativo)
* ``**``

Esto significa, por ejemplo,
que las multiplicaciones se evalúan antes que las sumas,
y que las comparaciones se evalúan antes que las operaciones lógicas::

    >>> 2 + 3 * 4
    14
    >>> 1 < 2 and 3 < 4
    True

Operaciones dentro de un mismo nivel
son evaluadas en el orden en que aparecen en la expresión,
de izquierda a derecha::

    >>> 15 * 12 % 7    # es igual a (15 * 12) % 7
    5

La única excepción a la regla anterior son las potencias,
que son evaluadas de derecha a izquierda::

    >>> 2 ** 3 ** 2    # es igual a 2 ** (3 ** 2)
    512

Para forzar un orden de evaluación distinto a la regla de precedencia,
debe usarse paréntesis::

    >>> (2 + 3) * 4
    20
    >>> 15 * (12 % 7)
    75
    >>> (2 ** 3) ** 2
    64

Otra manera de forzar el orden
es ir guardando los resultados intermedios en variables::

    >>> n = 12 % 7
    >>> 15 * n
    75

Como ejemplo, consideremos la siguiente expresión::

    15 + 59 * 75 / 9 < 2 ** 3 ** 2 and (15 + 59) * 75 % n == 1

y supongamos que la variable ``n`` tiene el valor 2.
Aquí podemos ver cómo la expresión es evaluada
hasta llegar al resultado final, que es ``False``::

    15 + 59 * 75 / 9 < 2 ** 3 ** 2 and (15 + 59) * 75 % n == 1
    #                         ↓
    15 + 59 * 75 / 9 < 2 **   9    and (15 + 59) * 75 % n == 1
    #                    ↓
    15 + 59 * 75 / 9 < 512         and (15 + 59) * 75 % n == 1
    #       ↓
    15 +  4425   / 9 < 512         and (15 + 59) * 75 % n == 1
    #            ↓
    15 +        491  < 512         and (15 + 59) * 75 % n == 1
    #                                      ↓
    15 +        491  < 512         and    74     * 75 % n == 1
    #                                            ↓
    15 +        491  < 512         and          5550  % n == 1
    #                                                   ↓
    15 +        491  < 512         and          5550  % 2 == 1
    #                                                 ↓
    15 +        491  < 512         and                0   == 1
    #  ↓
      506            < 512         and                0   == 1
    #                ↓
                    True           and                0   == 1
    #                                                     ↓
                    True           and                  False
    #                               ↓
                                  False

La operación entre paréntesis ``(15 + 59)``
debe ser evaluada antes de la multiplicación por 75,
ya que es necesario conocer su resultado
para poder calcular el producto.
El momento preciso en que ello ocurre no es importante.

Lo mismo ocurre con la evaluación de la variable ``n``:
sólo importa que sea evaluada antes de ser usada
por el operador de módulo.

En el ejemplo,
ambos casos fueron evaluados
inmediatamente antes de que su valor sea necesario.

Las reglas completas de precedencia,
incluyendo otros operadores que aún no hemos visto,
pueden ser consultados en
`la sección sobre expresiones`_
de la documentación oficial de Python.

.. _la sección sobre expresiones: http://docs.python.org/reference/expressions.html#summary

¿Cómo aprenderse las reglas de precedencia?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
La respuesta es: mejor no aprendérselas.
Las reglas de precedencia son muchas y no siempre son intuitivas,

Un programa queda mucho más fácil de entender
si uno explícitamente indica el orden de evaluación usando paréntesis
o guardando en variables los resultados intermedios del cálculo.

Un buen programador siempre se preocupa
de que su código sea fácil de entender por otras personas,
¡e incluso por él mismo en unas semanas más adelante!

Llamadas a función
------------------
.. index:: función

Los operadores forman un conjunto bastante reducido de operaciones.
Más comúnmente,
las operaciones más generales son representadas como **funciones**.

.. index:: parámetro, argumento, llamada a función

Al igual que en matemáticas, las funciones tienen un nombre,
y reciben **parámetros** (o **argumentos**)
que van entre paréntesis después del nombre.
La operación de usar la función para obtener un resultado
se llama **llamar la función**.

Ya conocemos la función ``raw_input()``,
que entrega como resultado
el texto ingresado por el usuario mediante el teclado.

.. index:: abs

La función ``abs`` entrega el valor absoluto de su argumento::

    >>> abs(4 - 5)
    1
    >>> abs(5 - 4)
    1

.. index:: len (de un string)

La función ``len`` recibe un string y entrega su largo.
(más adelante veremos otros usos de la función ``len``)::

    >>> len('hola mundo')
    10
    >>> len('hola' * 10)
    40

.. index:: int (función), float (función), str (función)

Los nombres de los tipos también sirven como funciones,
que entregan el equivalente de su parámetro
en el tipo correspondiente::

    >>> int(3.8)
    3
    >>> float('1.5')
    1.5
    >>> str(5 + 6)
    '11'
    >>> int('5' + '6')
    56

.. index:: min, max

Las funciones ``min`` y ``max``
entregan el mínimo y el máximo de sus argumentos::

    >>> min(6, 1, 8)
    1
    >>> min(6.0, 1.0, 8.0)
    1.0
    >>> max(6, 1, 4, 8)
    8

.. index:: round

La función ``round`` redondea un número real
al entero más cercano::

    >>> round(4.4)
    4.0
    >>> round(4.6)
    5.0

.. index:: exp, sin, log, 

Algunas funciones matemáticas
como la exponencial, el logaritmo
y las trigonométricas pueden ser usadas,
pero deben ser importadas primero
usando la sentencia ``import``,
que veremos en detalle más adelante::

    >>> from math import exp
    >>> exp(2)
    7.3890560989306504
    >>> from math import sin, cos
    >>> cos(3.14)
    -0.9999987317275395
    >>> sin(3.14)
    0.0015926529164868282

La lista completa de funciones matemáticas que pueden ser importadas
está en la `descripción del módulo math`_
en la documentación de Python.

.. _descripción del módulo math: http://docs.python.org/library/math.html

Más adelante también aprenderemos
a crear nuestras propias funciones.
Por ahora, sólo necesitamos saber cómo llamarlas.

Por supuesto,
siempre es necesario que los argumentos de una llamada
tengan el tipo apropiado::

    >>> round('perro')
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    TypeError: a float is required
    >>> len(8)
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    TypeError: object of type 'int' has no len()

