Triángulos
==========

Los tres lados *a*, *b* y *c* de un triángulo
deben satisfacer la `desigualdad triangular`_:
cada uno de los lados no puede ser más largo
que la suma de los otros dos.

.. _desigualdad triangular: http://es.wikipedia.org/wiki/Desigualdad_triangular

Escriba un programa
que reciba como entrada los tres lados de un triángulo,
e indique:

* si acaso el triángulo es inválido; y
* si no lo es, qué tipo de triángulo es.

.. testcase::

    Ingrese a: `3.9`
    Ingrese b: `6.0`
    Ingrese c: `1.2`
    No es un triangulo valido.

.. testcase::

    Ingrese a: `1.9`
    Ingrese b: `2`
    Ingrese c: `2`
    El triangulo es isoceles.

.. testcase::

    Ingrese a: `3.0`
    Ingrese b: `5.0`
    Ingrese c: `4.0`
    El triangulo es escaleno.

