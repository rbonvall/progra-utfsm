Máquina de alimentos
====================

*Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011 en el campus Vitacura.*

Una máquina de alimentos tiene productos de tres tipos,
``A``, ``B`` y ``C``,
que valen respectivamente $270, $340 y $390.
La máquina acepta y da de vuelto monedas de $10, $50 y $100.

Escriba un programa que pida al usuario elegir el producto
y luego le pida ingresar las monedas hasta alcanzar el monto a pagar.
Si el monto ingresado es mayor que el precio del producto,
el programa debe entregar las monedas de vuelto, una por una.

.. testcase::

    Elija producto: `A`
    Ingrese monedas:
    `100`
    `10`
    `50`
    `100`
    `100`
    Su vuelto:
    `50`
    `10`
    `10`
    `10`
    `10`

.. testcase::

    Elija producto: `B`
    Ingrese monedas:
    `100`
    `100`
    `100`
    `100`
    Su vuelto:
    `50`
    `10`

.. testcase::

    Elija producto: `C`
    Ingrese monedas:
    `100`
    `100`
    `50`
    `10`
    `100`
    `10`
    `10`
    `10`

