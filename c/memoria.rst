Cómo funciona la memoria
========================

.. highlight:: c

Todas las variables de un programa en C
tienen asociado un lugar en la memoria del computador.

La memoria puede ser vista como un gran arreglo de **bits**.
Un bit_ es la unidad básica de información
que se puede representar en un computador,
y puede tener los valores 0 o 1:

.. code-block:: none

        Memoria
    ┌──────────────────────────────────────────────┐
    │...0001001111011000001010110111110001010011...│
    └──────────────────────────────────────────────┘

.. _bit: http://en.wikipedia.org/wiki/Bit

Los bits están agrupados en **bytes**.
En cualquier computador moderno, un byte está formado por ocho bits:

.. code-block:: none

    ┌───┬────────┬────────┬────────┬────────┬────────┬───┐
    │...│00010011│11011000│00101011│01111100│01010011│...│
    └───┴────────┴────────┴────────┴────────┴────────┴───┘

Para que no pase vergüenzas: byte se pronuncia «bait».

Cualquier valor que aparezca en un programa
debe ser representado como uno o varios bytes.
Tanto el tamaño como la manera de interpretar un valor
están determinados por su **tipo de datos**.

Tipos de datos
--------------
El tamaño de un valor de tipo ``char`` es de 1 byte,
y el significado de los bits está determinado
usando la codificación ASCII_ (pronúnciese «asqui»).

.. _ASCII: http://en.wikipedia.org/wiki/ASCII

Una variable de tipo ``char`` estará almacenada, por lo tanto,
en uno de los bytes de la memoria.
Casi nunca nos interesará cuáles son exactamente los bits del valor,
por lo que podemos considerar
que lo que hay en ese byte es un caracter:

.. code-block:: none

      char a;

            a
    ┌───┬────────┬────────┬────────┬────────┬────────┬───┐
    │...│  'u'   │11011000│00101011│01111100│01010011│...│
    └───┴────────┴────────┴────────┴────────┴────────┴───┘

El tamaño de un ``int`` no es igual en todas las plataformas.
Si su procesador tiene una arquitectura de 32 bits,
lo más probable es que los enteros sean de 4 bytes.
Si es de 64 bits, probablemente son de 8 bytes.

Los enteros son almacenados en su `representación binaria`_.
La manera más común de representar los enteros negativos
es el `complemento a dos`_.

.. _representación binaria: http://en.wikipedia.org/wiki/Binary_numeral_system
.. _complemento a dos: http://en.wikipedia.org/wiki/Two's_complement

.. TODO: explicar otros tipos enteros.
.. Ver http://tsemba.org/c/inttypes.html.

El operador ``sizeof`` entrega el tamaño en bytes de una variable o de un tipo.
Para conocer los tamaños que tienen varios tipos de datos
en la plataforma que está usando,
ejecute el siguiente programa:

.. literalinclude:: programas/tamanos.c

Direcciones de memoria
----------------------
Todos los bytes en la memoria tienen una **dirección**,
que no es más que un índice correlativo.

Por conveniencia,
las direcciones de memoria suelen escribirse en `notación hexadecimal`_,
pero no hay que espantarse:
se trata simplemente de un número entero.

.. code-block:: none

       Dirección   Valor
                 ┌────────┐
                 │  ...   │
       0xf1e568  │00010011│
       0xf1e569  │11011000│
       0xf1e56a  │00101011│
       0xf1e56b  │01111100│
       0xf1e56c  │01010011│
                 │  ...   │
                 └────────┘

.. _notación hexadecimal: http://en.wikipedia.org/wiki/Hexadecimal

En C, el operador unario ``&`` permite obtener la dirección de la memoria
en que está almacenada una variable,
o más precisamente,
la dirección de su primer byte.

Las variables locales de una función
están almacenadas consecutivamente
en una región de la memoria llamada `pila de llamadas`_.

.. _pila de llamadas: http://es.wikipedia.org/wiki/Pila_de_llamadas

Copie y ejecute este programa,
e interprete cómo están distribuidas las variables en la pila:

.. literalinclude:: programas/direcciones.c

Por ejemplo,
yo ejecuté el programa una vez en el computador
y obtuve esta salida:

.. code-block:: none

    var     address   sizeof
    n:      0xe49808  4
    c:      0xe4980f  1
    x:      0xe49804  4
    h:      0xe497f0  12
    d:      0xe4980e  1

    h.anno: 0xe497f0  4
    h.mes : 0xe497f4  4
    h.dia : 0xe497f8  4


Esto significa que la pila está organizada más o menos así:

.. code-block:: none

                       ┌────────┐
            0xe497f0   │   2012 │  h.anno
            0xe497f1   │        │
            0xe497f2   │        │
            0xe497f3   │        │
                       ├────────┤
            0xe497f4   │      2 │  h.mes
            0xe497f5   │        │
            0xe497f6   │        │
            0xe497f7   │        │
                       ├────────┤
            0xe497f8   │     29 │  h.dia
            0xe497f9   │        │
            0xe497fa   │        │
            0xe497fb   │        │
                       ├────────┤
            0xe497fc   │ ?????? │
            0xe497fd   │ ?????? │
            0xe497fe   │ ?????? │
            0xe497ff   │ ?????? │
            0xe49800   │ ?????? │
            0xe49801   │ ?????? │
            0xe49802   │ ?????? │
            0xe49803   │ ?????? │
                       ├────────┤
            0xe49804   │ 3.1415 │  x
            0xe49805   │        │
            0xe49806   │        │
            0xe49807   │        │
                       ├────────┤
            0xe49808   │     10 │  n
            0xe49809   │        │
            0xe4980a   │        │
            0xe4980b   │        │
                       ├────────┤
            0xe4980c   │ ?????? │
            0xe4980d   │ ?????? │
                       ├────────┤
            0xe4980e   │    '!' │  d
                       ├────────┤
            0xe4980f   │   '\n' │  c
                       └────────┘

.. TODO: explicar los rellenos.
.. Explicación plausible: http://www.tenouk.com/Bufferoverflowc/Bufferoverflow3.html
.. Ver también http://en.wikipedia.org/wiki/Data_structure_alignment

.. Otro enlace interesante: http://eli.thegreenplace.net/2011/02/04/where-the-top-of-the-stack-is-on-x86/

