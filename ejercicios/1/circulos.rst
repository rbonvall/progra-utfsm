Círculos
--------

Escriba un programa que reciba como entrada el radio de un círculo
y entregue como salida su perímetro y su área,
dados por las siguientes fórmulas:

* `\text{perímetro} = 2\pi r`
* `\text{área} = \pi r^{2}`

.. testcase::

    Ingrese el radio: `5`
    Perímetro: 31.4
    Área: 78.5

Solución::

    from math import pi

    radio = float(input("Ingrese el radio:"))
    print "Perímetro":, 2 * pi * radio
    print "Área":, pi * radio ** 2
