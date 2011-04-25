Estadísticos de localización
============================

Media aritmética
----------------
La **media aritmética** (o promedio) de un conjunto de datos
es la suma de los valores dividida por
la cantidad de datos.

Escriba la función ``media_aritmetica(datos)``,
donde ``datos`` es una lista de números,
que entregue la media aritmética de los datos::

    >>> media_aritmetica([6, 1, 4, 8])
    4.75

Media armónica
--------------
La **media armónica** de un conjunto de datos
es el recíproco de la suma de los recíprocos de los datos,
multiplicada por la cantidad de datos:

.. math::

    H = \frac{n}{
      \frac{1}{x_1} +
      \frac{1}{x_2} +
      \cdots +
      \frac{1}{x_n} +
    }

Escriba la función ``media_armonica(datos)``,
que entregue la media armónica de los datos::

    >>> media_armonica([6, 1, 4, 8])
    2.5945945945945943

Mediana
-------
La **mediana** de un conjunto de datos reales
es el valor para el que el conjunto
tiene tantos datos mayores como menores a él.

Más rigurosamente,
la mediana es definida de la siguiente manera:

* si la cantidad de datos es impar,
  la mediana es el valor que queda en la mitad
  al ordenar los datos de menor a mayor;
* si la cantidad de datos es par,
  la mediana es el promedio de los dos valores que quedan al centro
  al ordenar los datos de menor a mayor.

Escriba la función ``mediana(datos)``,
que entregue la mediana de los datos::

    >>> mediana([5.0, 1.4, 3.2])
    3.2
    >>> mediana([5.0, 1.4, 3.2, 0.1])
    2.3

La función no debe modificar la lista que recibe como argumento::

    >>> x = [5.0, 1.4, 3.2]
    >>> mediana(x)
    3.2
    >>> x
    [5.0, 1.4, 3.2]

Moda
----
La **moda** de un conjunto de datos
es el valor que más se repite.

Escriba la función ``modas(datos)``,
donde ``datos`` es una lista,
que entregue una lista con las modas de los datos::

    >>> modas([5, 4, 1, 4, 3, 3, 4, 5, 0])
    [4]
    >>> modas([5, 4, 1, 4, 3, 3, 4, 5, 3])
    [3, 4]
    >>> modas([5, 4, 5, 4, 3, 3, 4, 5, 3])
    [3, 4, 5]

Estadísticos
------------
Usando las funciones definidas anteriormente,
escriba un programa que:

* pregunte al usuario cuántos datos ingresará,
* le pida que ingrese los datos uno por uno, y
* muestre un reporte con las medias aritmética y armónica,
  la mediana y las modas de los datos ingresados.

Si alguno de los datos es cero,
el reporte no debe mostrar la media armónica.

