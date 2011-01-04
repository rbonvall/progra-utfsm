Que nota necesito
-----------------
Un alumno desea saber que nota necesita en el ultimo certamen (C3),
para aprobar un ramo. 

El promedio del ramo se calcula con la siguiente formula.

.. math::

    Nc= \frac{(C1+C2+C3)}{3}

    Nf= Nc\cdot 0.7 + Nl\cdot 0.3

Donde *Ns* es Nota Certamen, *Nl* nota laboratorio y *Nf* nota final.

Escriba un programa que pregunte al usuario las notas de los dos
primeros certamen y la nota de laboratorio y muestre la nota que necesita el alumno para aprobar el ramo con nota final *60*.

Considere nota con aproximación o nota sin aproximación.

* **Entrada**

    Notas del certamen 1, certamen 2 y laboratorio.

* **Salida**

    La nota que necesita en el certamen 3.

* Comportamiento::

    Ingrese nota Certamen 1: `45`
    Ingrese nota Certamen 2: `55`
    Ingrese nota Laboratorio: `65`
    Necesita nota 74 en el Certamen 3, sin aproximación

    Ingrese nota Certamen 1: `45`
    Ingrese nota Certamen 2: `55`
    Ingrese nota Laboratorio: `65`
    Necesita nota 72 en el Certamen 3, con aproximación
