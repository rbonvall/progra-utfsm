Cálculo del interés
-------------------

Desarrolle un programa que
calcule el interés
de una cierta cantidad de dinero,
en un tiempo determinado,
mostrando en cada paso
el año y el monto recaudado hasta
el momento.

Recuerde que la forma de poder
calcular el *interés simple*,
es la siguiente:

* Contamos con un *monto inicial*.
* Tenemos una cierta *tasa de interés*.
* Se aplica a una cierta cantidad de *años*.

Entonces, para poder calcular
el interés en el primer año sólo debemos
tener en cuenta la siguiente ecuación:

.. math::

	\text{Monto = Monto \cdot (1 + Tasa de interés)}

Si tenemos un monto de 1000
una tasa de 5% y lo aplicamos
a 5 años, el procedimiento sería el siguiente:

* Primer año:

.. math::

    monto = 1000 \cdot (1 + 0.05)
    monto = 1050

* Segundo año:

.. math::

    monto = 1050 \cdot (1 + 0.05)
    monto = 1102.5

y así sucesivamente,
notar que a medida que vamos avanzando,
el monto que vamos considerando, es el obtenido en el procedimiento
anterior.

La salida del programa para el ejemplo anterior debería ser:

.. testcase::

	1 1050.0
	2 1102.5
	3 1157.625
	4 1215.50625
	4 1276.2815625

