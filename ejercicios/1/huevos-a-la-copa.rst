Huevos a la copa
================

*Ejercicio sacado de* [Lang09]_.

Cuando un huevo es hervido en agua,
las proteínas comienzan a coagularse
cuando la temperatura sobrepasa un punto crítico.
A medida que la temperatura aumenta,
las reacciones se aceleran.

En la clara, las proteínas comienzan a coagularse
para temperaturas sobre 63°C,
mientras que en la yema lo hacen
para temperaturas sobre 70°C.
Para hacer un huevo a la copa,
la clara debe haber sido calentada lo suficiente
para coagularse a más de 63°C,
pero la yema no debe sobrepasar los 70°C
para evitar obtener un huevo duro.

El tiempo en segundos que toma al centro de la yema
alcanzar `T_y` °C está dado por la fórmula:

.. math::

    t = \frac{M^{2/3} c \rho^{1/3}}
             {K\pi^2(4\pi/3)^{2/3}}
        \ln\left[
            0.76\frac{T_o - T_w}
                     {T_y - T_w}
        \right],

donde `M` es la masa del huevo,
`\rho` su densidad,
`c` su capacidad calorífica específica
y `K` su conductividad térmica.
Algunos valores típicos son:

* `M = 47\,[\text{g}]` para un huevo pequeño y
  `M = 67\,[\text{g}]` para uno grande,
* `\rho = 1.038\,[\text{g}\,\text{cm}^{-3}]`,
* `c = 3.7\,[\text{J}\,\text{g}^{-1} \text{K}^{-1}]`, y
* `K = 5.4\cdot 10^{-3}\,[\text{W}\,\text{cm}^{-1} \text{K}^{-1}`].

`T_w` es la temperatura de ebullición del agua
y `T_o` la temperatura original del huevo
antes de meterlo al agua,
ambos en grados Celsius.

Escriba un programa que reciba como entrada
la temperatura original del huevo
y muestre como salida
el tiempo en segundos que le toma
alcanzar la temperatura máxima
para prepararlo a la copa.

.. [Lang09] Hans Petter Langtangen.
           *A Primer on Scientific Programming with Python*.
           Springer-Verlag, 2009.

