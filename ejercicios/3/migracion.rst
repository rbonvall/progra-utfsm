Migración de poblaciones
========================

*Ejercicio sacado de* [Lay97]_.

Estudios demográficos muestran que, cada año,
el 5% de la población de una ciudad
se muda a los suburbios (y el 95% se queda),
mientras que el 3% de la población de los suburbios
se muda a la ciudad (y el 97% se muda).

Estos datos pueden ser representados
en una **matriz de migración**:

.. math::

    M =
    \frac{1}{100}
    \begin{bmatrix}
      95 &  3 \\
       5 & 97 \\
    \end{bmatrix}

#. Escriba un programa que pregunte al usuario
   cuáles son las poblaciones de la ciudad y los suburbios
   en el año 2011,
   y entregue una tabla con las poblaciones proyectadas
   para los siguientes 10 años:

   .. testcase::

       Poblacion ciudad: `600`
       Poblacion suburbios: `400`

       Anno    Ciudad     Suburbios
       ----------------------------
       2012    582.000    418.000
       2013    565.440    434.560
       2014    550.205    449.795
       2015    536.188    463.812
       2016    523.293    476.707
       2017    511.430    488.570
       2018    500.515    499.485
       2019    490.474    509.526
       2020    481.236    518.764
       2021    472.737    527.263

#. Considere ahora la siguiente variación.
   Suponga que
   todos los años
   hay 14000 personas que se mudan a la ciudad
   desde fuera de la región
   (no desde los suburbios)
   y 9000 personas abandonan la región;
   además,
   hay 13000 personas que se mudan anualmente
   a los suburbios desde fuera de la ciudad.

   Modifique el programa anterior
   para resolver este problema.



.. [Lay97] David C. Lay.
           *Linear Algebra and Its Applications*.
           Addison-Wesley, 1997.
