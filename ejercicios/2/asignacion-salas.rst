Asignación de salas
-------------------

El edificio de una escuela secundaria tiene
tres pisos, cada uno con cinco salas de clases
de tamaños diversos como se muestra en la
siguiente tabla:

+------+------------------------+
|      | Número de sala         |
+======+========================+
| Piso | 01 | 02 | 03 | 04 | 05 |
+------+------------------------+
|  1   | 30 | 30 | 15 | 30 | 40 |
+------+------------------------+
|  2   | 25 | 30 | 25 | 10 | 110|
+------+------------------------+
|  3   | 62 | 30 | 40 | 40 | 30 |
+------+------------------------+

Cada semestre, la escuela imparte 15 cursos
que deben distribuirse en las salas.

Desarrolle un programa que intente hacer
una asignación de salas satisfactoria
que acomode 15 clases, teniendo ya
los datos de las capacidaddes de salas
y tambien el tamaño de cada grupo de los
cursos.

Para los grupos que no puedan ser adecuadamente
ubicados, el programa mostrará el mensaje:

::

	No hay sala disponible

además, el programa indicará el número de asientos
vacíos en cada sala y en todo el edificio.

Para realiar la asignación utilice la estrategia
del *mejor ajuste*: para una demanda dada se asigna la
sala disponible cuyo exceso de capacidad sea mínimo.
