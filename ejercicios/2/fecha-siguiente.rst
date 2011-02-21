Fecha siguiente
---------------
Escriba una función que reciba como parámetro una fecha,
y entregue como resultado la fecha siguiente::

    fecha_siguiente(fecha(5, 11, 2010))   # → fecha(6, 11, 2010)
    fecha_siguiente(fecha(30, 4, 1995))   # → fecha(1,  5, 1995)
    fecha_siguiente(fecha(31, 12, 2005))  # → fecha(1,  1, 2006)

En casi todos los casos,
para obtener la fecha siguiente basta con sumar uno al día.

Los casos especiales ocurren a fin de mes y a fin de año.
Para detectarlos, basta con revisar qué pasó después de sumar uno al día:

* si el campo ``dia`` queda con un valor mayor al número de días del mes,
  hay que pasar al primer día del mes siguiente;
* si el campo ``mes`` queda con un valor mayor a 12,
  hay que pasar al primero de enero del año siguiente.


No es necesario que considere los años bisiestos.
