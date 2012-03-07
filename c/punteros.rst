Punteros
========

.. highlight:: c

Un **puntero** es un tipo de datos cuyo valor es una dirección de memoria.

Nunca olvide esta sencilla definición.
Los punteros son un concepto que suele causar mucha confusión
a quienes están aprendiendo C.
Sin embargo, no se trata de un concepto difícil
si uno comprende cómo están representadas las variables en la memoria.

Por otra parte,
el uso incorrecto de punteros es una fuente muy común de errores críticos,
y que no siempre son fáciles de depurar.
Por esto es importante siempre entender muy bien lo que se está haciendo
cuando hay punteros involucrados.


Cuando una variable de tipo puntero tiene almacenada una dirección de memoria,
se dice que «apunta» al valor que está en esa dirección.

.. code-block:: none

              +----------+
   0x3ad900   |      398 |  int n;
   0x3ad904   |    2.717 |  float b;
   0x3ad908   | 0x3ad900 |  puntero a n
   0x3ad90c   | 0x3ad904 |  puntero a x
   0x3ad910   |          |
              +----------+

Un valor especial llamado ``NULL``
puede ser asignado a cualquier puntero
para indicar aún no está apuntando a ninguna parte de la memoria.

Declaración de punteros
-----------------------
La siguiente es la manera de declarar un puntero
que apunte a un entero::

    int *x;

Esto se puede leer «lo apuntado por ``x`` es un entero».
En este caso, ``*`` no es una multiplicación,
sino una derreferenciación, como veremos más abajo.

Una vez declarada ``x`` de la manera mostrada,
los únicos valores válidos que se puede asignar a ``x``
son ``NULL`` o una dirección de memoria donde haya un entero::

    int a, b, c;
    float z;
    int *x;
    int *y;

    x = NULL;   /* valido */
    x = &a;     /* valido */
    x = &b;     /* valido */
    x = &z;     /* invalido (z no es un entero) */
    x = 142857; /* invalido (142857 no es una dirección de memoria) */

    y = &b;     /* valido */
    y = x;      /* valido */
    y = NULL;   /* valido */
    y = &x;     /* invalido (x no es un entero) */

Ojo con la siguiente sutileza al declarar varios punteros de una vez::

    int *x, *y;    /* x e y son punteros */
    int *x, y;     /* x es puntero, y es entero */

Derreferenciación de punteros
-----------------------------
El operador unario ``*`` de los punteros
es el operador de **derreferenciación**.
Lo que hace es entregar el valor que está
en la dirección de memoria.

En otras palabras,
``*`` significa «lo apuntado por».

Al derreferenciar un puntero a entero,
se obtiene un entero.

