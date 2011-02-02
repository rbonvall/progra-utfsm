Campeonato de fútbol
--------------------

Desarrolle un programa para manipular
la información de un campeonato de 
fútbol.

Los resultados pueden ser almacenados
en un arreglo bidimensional de registro
donde los índices representan los equipos
involucrados y los elementos del arreglo,
los registros, contienen dos campos: uno 
con los goles convertidos en el partido por
el equipo local y otro con los goles 
convertidos por el equipo visitante.

Por ejemplo:


+--------------------+-----------+--------------------+----------+-------------+
|                    | Colo-Colo | Santiago Wanderers | Cobreloa | U. de Chile |
+--------------------+-----------+--------------------+----------+-------------+
| Colo-Colo          |     -     |        2-0         |   3-1    |     1-0     |
+--------------------+-----------+--------------------+----------+-------------+
| Santiago Wanderers |    0-3    |         -          |   1-1    |     2-1     |
+--------------------+-----------+--------------------+----------+-------------+
| Cobreloa           |    1-1    |        2-2         |    -     |     1-2     |
+--------------------+-----------+--------------------+----------+-------------+
| U. de Chile        |    1-2    |        1-0         |   3-3    |      -      |
+--------------------+-----------+--------------------+----------+-------------+

El programa debe:

* Pedirle al usuario que ingrese los resultados
  de los partidos.
* Calcular los goles a favor y en contra, de local,
  de visita y en general, para cada equipo.
* Calcular partidos ganados, empatados y perdidos,
  de local, de visita y en general.
* Determinar el campeón considerando que cada partido
  ganado otorga 3 puntos para el ganador y cero para
  el perdedor, y los partidos empatados otorgan 1 punto
  para cada equipo.
* Se debe generar la tabla de posiciones donde los
  equipos estan ordenados según puntaje.
