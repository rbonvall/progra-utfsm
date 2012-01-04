Intersección de circunferencias
===============================

*Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011 en el campus Vitacura.*

Una circunferencia en el plano está definida por tres valores:
las coordenadas (*x*, *y*) de su centro, y su radio *r*.

Escriba un programa que determine si dos circunferencias se intersectan o no.

.. image:: ../../diagramas/circunferencias-cert.png

.. testcase::

    x1: `5`
    y1: `6`
    r1: `3.5`
    x2: `10`
    y2: `5`
    r2: `3`
    Se intersectan

.. testcase::

    x1: `3.5`
    y1: `5`
    r1: `2`
    x2: `10`
    y2: `4`
    r2: `3`
    No se intersectan

.. testcase::

    x1: `5`
    y1: `4.5`
    r1: `3`
    x2: `6`
    y2: `5`
    r2: `4.5`
    No se intersectan
