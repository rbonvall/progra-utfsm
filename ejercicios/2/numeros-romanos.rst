Números romanos
---------------

Los números romanos
aún son utilizados para
algunos propósitos.

Los símbolos básicos y sus
equivalencias decimales son:

+---+------+
| M | 1000 |
+---+------+
| D |  500 |
+---+------+
| C |  100 |
+---+------+
| L |   50 |
+---+------+
| X |   10 |
+---+------+
| V |    5 |
+---+------+
| I |    1 |
+---+------+

Los enteros romanos se escriben de acuerdo
a las siguientes reglas:

* Si una letra está seguida inmediatamente
  por una de igual o menor valor, su valor se
  suma al total acumulado. Así, XX = 20, XV = 15 y VI = 6.
* Si una letra está seguida inmediatamente
  por una de mayor valor, su valor se sustrae
  del total acumulado. Así, IV = 4, XL = 40
  y CM = 900.

Escriba la función ``romano_a_arabigo``
que reciba un string con un número en notación romana,
y entregue el entero equivalente::

    >>> romano_a_arabigo('MCMXIV')
    1914
    >>> romano_a_arabigo('XIV')
    14
    >>> romano_a_arabigo('X')
    10
    >>> romano_a_arabigo('IV')
    4
    >>> romano_a_arabigo('DLIV')
    554
    >>> romano_a_arabigo('CCCIII')
    303

