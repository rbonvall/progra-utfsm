Qué nota necesito
-----------------
Un alumno desea saber que nota necesita en el tercer certamen
para aprobar un ramo.

El promedio del ramo se calcula con la siguiente formula.

.. math::

    N_C = \frac{(C1+C2+C3)}{3}

    N_F = N_C\cdot 0.7 + N_L\cdot 0.3

Donde `N_C` es el promedio de certámenes,
`N_L` el promedio de laboratorio
y `N_F` la nota final.

Escriba un programa que pregunte al usuario las notas de los dos
primeros certamen y la nota de laboratorio,
y muestre la nota que necesita el alumno
para aprobar el ramo con nota final 60.

.. testcase::

    Ingrese nota certamen 1: `45`
    Ingrese nota certamen 2: `55`
    Ingrese nota laboratorio: `65`
    Necesita nota 72 en el certamen 3
