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

              ┌──────────┐
   0x3ad900   │      398 │  int n
              ├──────────┤
   0x3ad904   │ ???????? │
              ├──────────┤
   0x3ad908   │ 0x3ad900 │  int *p
              ├──────────┤
   0x3ad90c   │ 0x3ad904 │  float *q
              ├──────────┤
   0x3ad910   │    2.717 │  float x
              └──────────┘

.. x*

En general no importa cuál es valor exacto de un puntero,
sino que basta con comprender qué es lo que hay «al otro lado».
Por esto, en los diagramas de la memoria
se suele preferir usar flechas
en lugar de las direcciones explícitas:

.. code-block:: none

               ┌──────────┐
        int n  │      398 │◂────┐
               ├──────────┤     │
               │ ???????? │     │
               ├──────────┤     │
       int *p  │     ●────┼─────┘
               ├──────────┤
     float *q  │     ●────┼────┐
               ├──────────┤    │
      float x  │    2.717 │◂───┘
               └──────────┘

.. x*

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

Una vez declarada ``x`` de la manera ya mostrada,
los únicos valores válidos que se puede asignar a ``x``
son ``NULL`` o una dirección de memoria donde haya un entero::

    int a, b, c;
    float z;
    int *p;
    int *q;

    p = NULL;   /* valido */
    p = &a;     /* valido */
    p = &b;     /* valido */
    p = &z;     /* invalido (z no es un entero) */
    p = 142857; /* invalido (142857 no es una dirección de memoria) */

    q = &b;     /* valido */
    q = p;      /* valido */
    q = NULL;   /* valido */
    q = &p;     /* invalido (p no es un entero) */

Por supuesto,
es posible cambiar ``int`` por cualquier otro tipo
para declarar punteros a datos de otra naturaleza.

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
El puntero derreferenciado puede ser usado
en cualquier contexto en que un entero sea válido::

    int x, y;
    int *p;

    x = 5;
    p = &x;

    printf("%d\n", *p);      /* imprime 5 */
    y = *p * 10 - 7;         /* y toma el valor 43 */
    *p = 9;                  /* x toma el valor 9 */

En la última sentencia,
se está asignando el valor ``9``
en la memoria que está reservada para la variable ``x``,
por lo que la asignacion
cambia en efecto el valor de la variable ``x``
de manera indirecta.

Derreferenciar el puntero ``NULL`` no está permitido.
Al hacerlo,
lo más probable es que el programa se termine abruptamente
y sin razón aparente.
Errores de este tipo son muy fastidiosos,
pues son difíciles de detectar,
e incluso pueden ocurrir en un programa
que ha estado funcionando correctamente
durante mucho tiempo.

Si existe alguna remota posibilidad
de que un puntero pueda tener el valor ``NULL``,
lo sensato es revisar su valor
antes de derreferenciarlo::

    if (p != NULL)
        hacer_algo(*p);

Ejercicio
---------
¿Qué imprime el siguiente programa?

.. literalinclude:: programas/ejercicio-punteros.c

