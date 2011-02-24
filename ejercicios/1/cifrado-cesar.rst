Cifrado César
-------------

El `cifrado César`_ consiste en aumentar cada letra
(del mensaje que se desea cifrar) en un número determinado (llave),
por ejemplo, si el mensaje fuese::

    "abcdef"

y se codificara usando cifrado Cesar con ``llave = 1``,
el mensaje quedaría::

    "bcdefg"

Como se aprecia, cada letra fue cambiada por la letra siguiente
del alfabeto, ya que ``llave = 1`` significa que se corre una letra.

.. _cifrado César: http://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar

En caso de trabajar con números,
la llave indica el valor a sumar a cada dígito.

Por ejemplo, si se quiere codificar el número 12345
usando cifrado Cesar con ``llave = 2``,
el número quedaría::

    "34567"

El conjunto se considera circular,
por lo que al codificar el número 6789
con ``llave = 2`` se obtiene 8901.

Escriba un programa para poder utilizar el
cifrado César para cualquier mensaje ingresado,
ya sean números o un string, requiriendo también
señalar una llave a utilizar.

.. testcase::

    Ingrese mensaje: `9112`
    Ingrese llave: `3`
    2445
