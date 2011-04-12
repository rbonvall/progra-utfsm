Desviación estándar
-------------------

Desarrolle una función llamada ``desviacion_estandar(valores)``
cuyo parámetro ``valores`` sea una lista de números reales.

La función debe retornar
la `desviación estándar`_ de los valores:

.. math::

   \sigma = \sqrt{\sum_{i} \frac{(x_i - \bar{x})^2}{n - 1}}

.. _desviación estándar: http://es.wikipedia.org/wiki/Desviaci%C3%B3n_est%C3%A1ndar

donde `n` es la cantidad de valores,
`\bar{x}` es el promedio de los valores, y
los `x_i` son cada uno de los valores.

Esto significa que hay que hacerlo siguiendo estos pasos:

* calcular el promedio de los valores;
* a cada valor hay que restarle el promedio,
  y el resultado elevarlo al cuadrado;
* sumar todos los valores obtenidos;
* dividir la suma por la cantidad de valores; y
* sacar la raíz cuadrada del resultado.

::

    >>> desviacion_estandar([1.3, 1.3, 1.3])
    0.0
    >>> desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0])
    4.88535225615
    >>> desviacion_estandar([1.5, 9.5])
    5.65685424949
