Máximo común divisor
====================

Escriba la función ``mcd(a, b)``
que entrege el `máximo común divisor`_
de los enteros ``a`` y ``b``:

.. testcase::

    >>> mcd(20, 50)
    10

    >>> mcd(31, 19)
    1

.. _máximo común divisor: http://es.wikipedia.org/wiki/Máximo_común_divisor

La manera obvia de implementar este programa
es literalmente buscando el mayor de los divisores comunes.
Existe una técnica más eficiente,
que es conocida como el `algoritmo de Euclides`_.
Este método tiene importancia histórica,
ya que es uno de los algoritmos más antiguos
que aún sigue siendo utilizado.

.. _algoritmo de Euclides: http://es.wikipedia.org/wiki/Algoritmo_de_Euclides#Descripci.C3.B3n_formal

Resuelva este problema de las dos maneras.
