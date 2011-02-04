.. _programas-simples:

Programas simples
=================

.. index:: sentencia

Un programa es una secuencia de **sentencias**.
Una sentencia representa una instrucción bien definida
que es ejecutada por el computador.

Hay que distinguir entre:

#. **sentencias simples**: son una única instrucción; y
#. **sentencias de control**: contienen varias otras sentencias,
   que a su vez pueden ser simples o de control.

Las sentencias simples son ejecutadas secuencialmente,
una después de la otra.



En Python, cada línea del código representa una sentencia.

A continuación veremos algunas sentencias simples,
con las que se pueden escribir algunos programas sencillos.
Más adelante introduciremos las sentencias de control.

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

En el algoritmo para resolver la ecuación cuadrática
aparece la expresión `b² − 4ac`,
cuyo resultado depende de cuáles son los valores de
`a`, `b` y `c` al momento de la evaluación.
A diferencia de los valores literales,
`a`, `b` y `c` son **variables**.
Una variable es un nombre que es asociado a un valor,
para poder usarlo de manera independiente
al valor específico que representa.

En el programa en Python,
esa expresión aparece escrita de la siguiente manera::

    b ** 2 - 4 * a * c

En general, en un programa no se puede usar la misma notación que en matemáticas.
En este caso, el operador ``**`` representa la exponenciación
y ``*`` la multiplicación.

Una expresión puede ser usada como una sentencia de un programa por sí sola,
pero la mayoría de las veces esto no tiene ningún efecto.
El programa evaluará la expresión, pero no hará nada con el resultado obtenido.

Asignaciones
------------
.. index:: asignación

Una **asignación** es una sentencia que asocia un nombre a un valor.

En el programa de la ecuación cuadrática


Salida
------
En Python, la salida del programa es realizada
por la sentencia **print**.
