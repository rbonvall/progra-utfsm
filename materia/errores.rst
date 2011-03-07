Errores y excepciones
=====================
.. index:: error

No siempre los programas que escribiremos están correctos.
Existen muchos tipos de errores que pueden estar presentes en un programa.

No todos los errores pueden ser detectados por el computador.
Por ejemplo,
el siguiente programa tiene un error lógico bastante evidente::

    n = int(raw_input('Escriba un numero: '))
    doble = 3 * n
    print 'El doble de n es', doble

El computador no se dará cuenta del error,
pues todas las instrucciones del programa son correctas.
El programa simplemente entregará siempre la respuesta equivocada.

Existen otros errores que sí pueden ser detectados.
Cuando un error es detectado *durante* la ejecución del programa
ocurre una **excepción**.

El intérprete anuncia una excepción
deteniendo el programa
y mostrando un mensaje con la descripción del error.
Por ejemplo,
podemos crear el siguiente programa
y llamarlo ``division.py``::

    n = 8
    m = 0
    print n / m
    print 'Listo'

Al ejecutarlo,
el intérprete lanzará una excepción,
pues la división por cero
es una operación inválida::

    Traceback (most recent call last):
      File "division.py", line 3, in <module>
        print n / m
    ZeroDivisionError: division by zero

La segunda línea del mensaje
indica cómo se llama el archivo donde está el error
y en qué línea del archivo está.
En este ejemplo,
el error esta en la línea 3 de ``division.py``.
La última línea muestra el nombre de la excepción
(en este caso es ``ZeroDivisionError``)
y un mensaje explicando cuál es el error.

Los errores y excepciones presentados aquí
son los más básicos y comunes.

Error de sintaxis
-----------------
.. index:: error de sintaxis

Un **error de sintaxis** ocurre cuando el programa
no cumple las reglas del lenguaje.
Cuando ocurre este error,
significa que el programa está mal escrito.
El nombre del error es ``SyntaxError``.

Los errores de sintaxis siempre ocurren *antes*
de que el programa sea ejecutado.
Es decir, un programa mal escrito no logra ejecutar ninguna instrucción.
Por lo mismo, el error de sintaxis no es una excepción.

A continuación veremos algunos ejemplos de errores de sintaxis ::

    >>> 2 * (3 + 4))               
      File "<stdin>", line 1
        2 * (3 + 4))
                   ^
    SyntaxError: invalid syntax

::

    >>> n + 2 = 7
      File "<stdin>", line 1
    SyntaxError: can't assign to operator

::

    >>> True = 1000
      File "<stdin>", line 1
    SyntaxError: assignment to keyword

Error de nombre
---------------
.. index:: error de nombre

Un **error de nombre**
ocurre al usar una variable que no ha sido creada con anterioridad.

El nombre de la excepción es ``NameError``::

    >>> x = 20
    >>> 5 * x
    100
    >>> 5 * y
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'y' is not defined

Para solucionar este error,
es necesario asignar un valor a la variable
antes de usarla.

Error de tipo
-------------
.. index:: error de tipo

En general,
todas las operaciones en un programa
pueden ser aplicadas sobre valores
de tipos bien específicos.
Un **error de tipo** ocurre
al aplicar una operación
sobre operandos de tipo incorrecto.

El nombre de la excepción es ``TypeError``.

Por ejemplo,
no se puede multiplicar dos strings::

    >>> 'seis' * 'ocho'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can't multiply sequence by non-int of type 'str'

Tampoco se puede obtener el largo de un número::

    >>> len(68)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()

Cuando ocurre un error de tipo,
generalmente el programa está mal diseñado.
Hay que revisarlo, idealmente hacer un ruteo
para entender el error,
y finalmente corregirlo.


Error de valor
--------------
.. index:: error de valor

El **error de valor**
ocurre cuando los operandos son del tipo correcto,
pero la operación no tiene sentido para ese valor.

El nombre de la excepción es ``ValueError``.

Por ejemplo,
la función ``int`` puede convertir un string a un entero,
pero el string debe ser la representación de un número entero.
Cualquier otro valor lanza un error de valor::

    >>> int('41')
    41
    >>> int('perro')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'perro'
    >>> int('cuarenta y uno')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'cuarenta y uno'

Para corregir el error,
hay que preocuparse de siempre usar valores adecuados.

    
Error de división por cero
--------------------------
.. index:: error de división por cero

El **error de division por cero** ocurre al intentar dividir por cero.

El nombre de la excepción es ``ZeroDivisionError``::

    >>> 1/0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero


Error de desborde
-----------------
.. index:: error de desborde

El **error de desborde**
ocurre cuando el resultado de una operación es tan grande
que el computador no puede representarlo internamente.

El nombre de la excepción es ``OverflowError``::

    >>> 20.0 ** 20.0 ** 20.0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OverflowError: (34, 'Numerical result out of range')

Para los interesados en saber más sobre excepciones,
pueden revisar `la sección sobre excepciones`_
en la documentación oficial de Python.

.. _la sección sobre excepciones: http://docs.python.org/library/exceptions.html

