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
el operador ``+`` es un operador binario que representa la suma,
y sus operandos son ``2.0`` y ``x``.

Los principales operadores se pueden clasificar en:
lógicos, aritméticos y relacionales.

Operadores aritméticos
~~~~~~~~~~~~~~~~~~~~~~
.. index:: operador aritmético

Los **operadores aritméticos** son los que representan operaciones numéricas.
Tanto sus operandos como sus resultados son valores numéricos.

.. index:: + (binario), - (binario), /, //, %, ** , *
.. index:: suma, resta, multiplicación, división, módulo, potencia

Algunos operadores aritméticos binarios son:

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

El operador de módulo entrega el resto de la división
entre sus operandos::

    >>> 7 % 3
    1

Una relación entre ``/`` y ``%`` que siempre se cumple
para los números enteros es::

    (a // b) * b + (a % b) == a

.. index:: + (unario), - (unario), positivo, negativo

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

Operadores relacionales
~~~~~~~~~~~~~~~~~~~~~~~
.. index:: operador relacional, comparación

Los **operadores relacionales** son los que permiten comparar valores.
Sus operandos son cualquier cosa que pueda ser comparada,
y sus resultados siempre son valores lógicos.

Algunos operadores relacionales son:

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

Operadores lógicos
~~~~~~~~~~~~~~~~~~
.. index:: operador lógico, operador booleano

Los **operadores lógicos** son los que tienen valores lógicos
(verdadero y falso) como operandos y como resultado.
Los valores lógicos posibles son
``True`` (verdadero) y ``False`` (falso).

Hay tres operadores lógicos:

.. index:: and, or, not

* **and** (en español: «y») representa la conjunción lógica;
* **or** (en español: «o») representa la disyunción lógica.
* **not** (en español: «negación») representa la negación lógica.

Los operadores ``and`` y ``or`` son binarios,
mientras que ``not`` es unario.

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

Operadores de texto
~~~~~~~~~~~~~~~~~~~
Los operadores ``+`` y ``*`` tienen otras interpretaciones
cuando sus operandos son strings.

``+`` es el operador de **concatenación** de strings:
pega dos strings uno después del otro::

    >>> 'perro' + 'gato'
    'perrogato'

La concatenación no es una suma.
Ni siquiera es una operación conmutativa.

``*`` es el operador de **repetición** de strings.
Recibe un operando string y otro entero,
y entrega como resultado el string repetido tantas veces como indica el entero::

    >>> 'waka' * 2
    'wakawaka'

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
* ``*``, ``/``, ``//``, ``%``
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

