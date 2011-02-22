Cifrado César
-------------

El cifrado César consiste en aumentar cada letra
(del mensaje que se desea cifrar) en un número determinado (llave),
por ejemplo, si el mensaje fuese::

    "abcdef"

y se codificara mediante cifrado Cesar con::

    llave = 1

el mensaje quedaría::

    "bcdefg"

como se aprecia, cada letra fue cambiada por la letra siguiente
del alfabeto, ya que *llave=1* (se corre 1 letra).

En caso de trabajar con números la *llave* indica el valor
a sumar a cada dígito.

Por ejemplo, si se quiere codificar el número::

    "12345"

con cifrado Cesar, y::

    llave = 2

el número quedaría::

    "34567"

Cabe señalar que el conjunto se considera circular,
o sea, si por ejemplo se quisiera codificar el número *6789* con 
cifrado César, *llave=2*, el número quedaría *8901*.

Se pide entonces realizar un programa para poder utilizar el
cifrado César para cualquier mensaje ingresado,
ya sean números o un string, requiriendo también
señalar una *llave* a utilizar.

El programa nos entregará el *mensaje* ingresado,
de una manera codificada.

.. testcase::

    Ingrese mensaje: `abcdef`
    Ingrese llave: `2`
    cdefgh

.. testcase::

    Ingrese mensaje: `9112`
    Ingrese llave: `3`
    2445
