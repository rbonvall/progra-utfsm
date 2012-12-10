Tipos de datos
==============

.. index:: tipo de datos

Un **tipo de datos** es la propiedad de un valor
que determina su dominio (qué valores puede tomar),
qué operaciones se le pueden aplicar
y cómo es representado internamente por el computador.

Todos los valores que aparecen en un programa tienen un tipo.

A continuación revisaremos los tipos de datos elementales de Python.
Además de éstos, existen muchos otros,
y más adelante aprenderemos a crear
nuestros propios tipos de datos.

Números enteros
---------------
.. index:: número entero, int

El tipo **int**
(del inglés *integer*, que significa «entero»)
permite representar números enteros.

Los valores que puede tomar un ``int`` son
todos los números enteros:
... ``-3``, ``-2``, ``-1``, ``0``, ``1``, ``2``, ``3``, ...

Los números enteros literales
se escriben con un signo opcional
seguido por una secuencia de dígitos::

    1570
    +4591
    -12

Números reales
--------------
.. index:: número real, número de punto flotante, float

El tipo **float** permite representar números reales.

El nombre ``float`` viene del término `punto flotante`_,
que es la manera en que el computador representa internamente
los números reales.

.. _punto flotante: http://es.wikipedia.org/wiki/Punto_flotante

Hay que tener mucho cuidado,
porque los números reales no se pueden representar
de manera exacta en un computador.
Por ejemplo,
el número decimal 0.7
es representado internamente por el computador
mediante la aproximación 0.69999999999999996.
Todas las operaciones entre valores ``float``
son aproximaciones.
Esto puede conducir a resultados algo sorpresivos::

    >>> 1/7 + 1/7 + 1/7 + 1/7 + 1/7 + 1/7 + 1/7
    0.9999999999999998

Los números reales literales
se escriben separando la parte entera de la decimal
con un punto.
Las partes entera y decimal pueden ser omitidas
si alguna de ellas es cero::

    >>> 881.9843000
    881.9843
    >>> -3.14159
    -3.14159
    >>> 1024.
    1024.0
    >>> .22
    0.22


.. index:: notación científica

Otra representación es la notación científica,
en la que se escribe un factor y una potencia de diez
separados por una letra ``e``.  Por ejemplo::

    >>> -2.45E4
    -24500.0
    >>> 7e-2
    0.07
    >>> 6.02e23
    6.02e+23
    >>> 9.1094E-31
    9.1094e-31

Los dos últimos valores del ejemplo
son iguales, respectivamente, a
:math:`6.02\times 10^{23}` (la `constante de Avogadro`_) y
:math:`9.1094\times 10^{-31}` (la `masa del electrón`_).

.. _constante de Avogadro: http://es.wikipedia.org/wiki/Constante_de_Avogadro
.. _masa del electrón: http://es.wikipedia.org/wiki/Electr%C3%B3n#Propiedades

.. Cuando se combinan valores reales y enteros en una operación,
.. el entero es convertido a un número real antes de evaluarla.
.. Por ejemplo, ``5.3 + 2`` primero es convertido a ``5.3 + 2.0``,
.. y el resultado es real::
.. 
..     >>> 5.3 + 2
..     7.3
.. 
.. La regla general es:
.. si en una expresión aritmética aparece algún ``float``,
.. el resultado es de tipo ``float``.

Números complejos
-----------------
.. index:: número complejo, complex

El tipo **complex** permite representar números complejos.

Los números complejos tienen una parte real y una imaginaria.
La parte imaginaria es denotada
agregando una ``j`` inmediatamente después de su valor::

    3 + 9j
    -1.4 + 2.7j

Valores lógicos
---------------
.. index:: bool, valor lógico, valor booleano

Los valores lógicos ``True`` y ``False``
(verdadero y falso)
son de tipo **bool**, que representa valores lógicos.

El nombre ``bool`` viene del matemático `George Boole`_,
quien creó un sistema algebraico para la lógica binaria.
Por lo mismo,
a ``True`` y ``False`` también se les llama
**valores booleanos**.
El nombre no es muy intuitivo,
pero es el que se usa en informática,
así que hay que conocerlo.

.. _George Boole: http://es.wikipedia.org/wiki/George_Boole

.. Las operaciones lógicas ``and``, ``or`` y ``not``
.. pueden ser aplicadas sobre valores booleanos,
.. y entregan como resultado un valor booleano::
.. 
..     >>> not True or (True and False)
..     False
.. 
.. Las operaciones relacionales
.. ``<``, ``>``, ``==``, etc.,
.. pueden ser aplicadas sobre valores de tipos comparables,
.. pero siempre entregan como resultado un valor booleano::
.. 
..     >>> 2 + 2 == 5
..     False
..     >>> x = 95.4
..     >>> 50 < x < 100
..     True

Texto
-----
.. index:: string, tipo de datos de texto, str

A los valores que representan texto
se les llama **strings**,
y tienen el tipo **str**.

Los strings literales
pueden ser representados
con texto entre comillas simples o comillas dobles::

   "ejemplo 1"
   'ejemplo 2'

La ventaja de tener dos tipos de comillas
es que se puede usar uno de ellos
cuando el otro aparece como parte del texto::

    "Let's go!"
    'Ella dijo "hola"'

.. Los operadores aritméticos no pueden ser aplicadas sobre strings,
.. salvo dos excepciones:
.. 
.. 1. El operador ``+`` aplicado a dos strings
..    no representa la suma,
..    sino la **concatenación**,
..    que significa pegar los strings
..    uno después del otro::
.. 
..        >>> "hola " + 'mundo'
..        'hola mundo'
.. 
.. 2. El operador ``*`` aplicado a un string y a un número entero
..    no representa la multiplicación,
..    sino la **repetición**,
..    es decir, el string es repetido tantas veces como indica el número::
.. 
..        >>> "lo" * 5
..        'lololololo'
.. 
.. Las operaciones relacionales permiten comparar strings alfabéticamente::
.. 
..     >>> "ala" < "alamo" < "bote" < "botero" < "boteros" < "zapato"
..     True
.. 
.. Para conocer el largo de un string,
.. se utiliza la función ``len()``::
.. 
..     >>> len('universidad')
..     11
.. 
.. La función ``input()``,
.. que usamos para leer la entrada del usuario,
.. siempre entrega como resultado un string.
.. Hay que tener la precaución
.. de convertir los valores que entrega
.. al tipo adecuado.
.. Por ejemplo,
.. el siguiente programa tiene
.. un error de incompatibilidad de tipos::
.. 
..     n = input('Escriba un número:')
..     cuadrado = n * n
..     print('El cuadrado de n es', cuadrado)

Es importante entender que los strings
no son lo mismo que los valores que en él
pueden estar representados::

   >>> 5 == '5'
   False
   >>> True == 'True'
   False

Los strings que difieren en mayúsculas y minúsculas,
o en espacios también son distintos::

   >>> 'mesa' == 'Mesa'
   False
   >>> ' mesa' == 'mesa '
   False

Nulo
----
.. index:: tipo nulo, None

Existe un valor llamado **None**
(en inglés, «ninguno»)
que es utilizado para representar casos
en que ningún valor es válido,
o para indicar que una variable
todavía no tiene un valor que tenga sentido.

El valor ``None`` tiene su propio tipo,
llamado ``NoneType``,
que es diferente al de todos los demás valores.

.. Conversión de tipos
.. -------------------
.. .. index:: conversión de tipos
.. 
.. Los tipos de los valores
.. indican qué operaciones pueden ser aplicadas sobre ellos.
.. 
.. A veces es necesario convertir valores de un tipo a otro
.. para poder operar sobre ellos.
.. Existen dos tipos de conversiones:
.. implícitas y explícitas.
.. 
.. Las conversiones implícitas
.. son las que se hacen automáticamente
.. según el contexto.
.. Las más importantes son las siguientes:
.. 
.. * cuando se utiliza un entero
..   en un contexto real,
..   el entero es convertido al real correspondiente::
.. 
..       >>> 56 * 8.0
..       448.0
.. 
.. * cuando se utiliza cualquier valor
..   en un contexto booleano,
..   es convertido al valor ``True``,
..   excepto por los siguientes casos,
..   en que es convertido al valor ``False``:
.. 
..   * el valor ``0``,
..   * el string vacío ``''``,
..   * ``None``.
.. 
..   Por ejemplo::
.. 
..       >>> not 0
..       True
..       >>> not 10
..       False
..       >>> not 'hola'
..       False
..       >>> bool(3.14)
..       True
.. 
..   Con los operadores ``and`` y ``or``
..   ocurre algo más extraño::
.. 
..       >>> 4 and 7
..       7
..       >>> 0 and 7
..       0
..       >>> 5 or 6
..       5
..       >>> 0 or 6 or 7
..       6
.. 
..   **Ejercicio:** deducir cómo funcionan ``and`` y ``or``
..   cuando los operandos no son booleanos.
.. 
.. * cuando se utiliza un valor lógico
..   en un contexto entero,
..   ``True`` es convertido a ``1``
..   y ``False`` a ``0``::
.. 
..       >>> True * 4 + False * 8
..       4
..       >>> True + True
..       2
..       >>> n = 5
..       >>> "el número es " + ((n % 2 != 0) * "im") + "par"
..       'el número es impar'
.. 
.. Las conversiones explícitas se realizan
.. usando el nombre del tipo de destino
.. como si fuera una función.
.. 
.. Por ejemplo,
.. para convertir un valor al tipo entero,
.. se utiliza la función ``int``::
.. 
..     >>> int('45')
..     45
..     >>> int(3.891)
..     3
..     >>> int(True)
..     1
..     >>> int(None)
..     TypeError: int() argument must be a string or a number, not 'NoneType'
..     >>> int('abc')
..     ValueError: invalid literal for int() with base 10: 'abc'
..     >>> int('doscientos')
..     ValueError: invalid literal for int() with base 10: 'doscientos'
.. 
.. Ya veremos qué significan los errores.
.. 
.. Para convertir un valor en un string,
.. se utiliza la función ``str``::
.. 
..     >>> str(87)
..     '87'
..     >>> str(True)
..     'True'

