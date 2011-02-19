Problema de Josefo
==================
El `problema de Josefo`_ es el siguiente:
`m` personas están en un círculo,
y son ejecutadas en orden contando cada `n` personas;
el que queda solo al final es el sobreviviente.

.. _problema de Josefo: http://es.wikipedia.org/wiki/Problema_de_Flavio_Josefo

Por ejemplo,
con `m = 12` y `n = 3`,
el sobreviviente es la persona 10:

.. image:: http://img.thedailywtf.com/images/200907/Josephus.gif

Escriba una función que reciba los parámetros ``m`` y ``n``,
e indique quién es el sobreviviente:

.. code-block:: none

    >>> sobreviviente(12, 3)
    10

