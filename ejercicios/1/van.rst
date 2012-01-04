Valor actual neto
=================

*Este problema apareció en el certamen 1 del primer semestre de 2011.*

En finanzas,
el *valor actual neto* es un indicador
de cuán rentable será un proyecto.

Se calcula sumando
los flujos de dinero de cada mes
divididos por `(1 + r)^n`,
donde `n` es el número del mes
y `r` es la tasa de descuento mensual,
y restando la inversión inicial.

Por ejemplo,
en un proyecto en que la inversión inicial es $900,
los flujos de dinero estimados para los primeros cuatro meses son
$550, $230, $341 y $190,
y la tasa de descuento mensual es de 4%,
el valor actual neto es:

.. math::

    \text{VAN} = -900 +
                 \frac{550}{(1 + 0.04)^1} +
                 \frac{230}{(1 + 0.04)^2} +
                 \frac{341}{(1 + 0.04)^3} +
                 \frac{190}{(1 + 0.04)^4}.

Si el VAN da negativo, entonces no es conveniente comenzar el proyecto.

Escriba un programa que pida al usuario ingresar la inversión inicial
y el porcentaje de tasa de descuento.
A continuación,
debe preguntar el flujo de dinero estimado para cada mes
y mostrar cuál es la parte entera del VAN hasta ese momento.

El programa debe terminar apenas el VAN comience a dar positivo.

.. testcase::

    Inversion inicial: `900`
    % tasa de descuento: `4`
    Flujo mes 1: `550`
    VAN: -371
    Flujo mes 2: `230`
    VAN: -158
    Flujo mes 3: `341`
    VAN: 144

Suponga que todos los datos ingresados son válidos.

