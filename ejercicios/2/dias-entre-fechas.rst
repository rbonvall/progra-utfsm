Días entre fechas
-----------------
Escriba una función que reciba como parámetros dos fechas,
y entregue como resultado la cantidad de días que hay entre ambas fechas.

La manera fácil de resolver este problema
es reutilizando la función `dia_siguiente`_.

.. _dia_siguiente: fecha-siguiente.html 

Partiendo del día inicial,
avanzar la fecha día por día hasta llegar al día final,
llevando la cuenta de los días.

Es importante asegurarse que
la fecha inicial ocurra antes de la fecha final.
Si no es así,
el ciclo nunca terminará,
y el programa se quedará pegado.
