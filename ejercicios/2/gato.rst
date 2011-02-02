Gato
----

Desarrolle un programa para jugar al gato
determinando *la mejor* jugada del jugador
que juega con las *X*.

Considere que todas las celdas están vacías
y evalúe las jugadas potenciales en ellas
utilizando la siguiente estrategia:

* Si la jugada ocupa el tercer cuadro en una
  fila, columna o diagonal que tenga ya dos X,
  sume 50 al marcador.
* Si la jugada ocupa el tercer cuadro de una
  fila, columna o diagonal con dos O, sume 25
  al marcador.
* Si tras la jugada una fila, columna o diagonal
  contiene dos X y un blanco, sume 10.
* Sume 8 si una fila, columna o diagonal queda,
  después de la jugada, con una O, una X o un
  blanco.
* Sume 4 por cada fila, columna o diagonal que
  quede con una X y el resto blancos.

Seleccione la jugada de mayor marcador.

Considerando el siguiente tablero:

.. image:: ../../diagramas/gato.png
    :alt: gato
    :align: center

Las posibles jugadas y sus marcadores son
los siguientes:

+----------+------------+
| Posición | Marcador   |
+==========+============+
|    1     | 10+8=18    |
+----------+------------+
|    2     | 10+8=18    |
+----------+------------+
|    3     | 10+10=20   |
+----------+------------+
|    4     |   8=8      |
+----------+------------+
|    5     | 10+10+8=28 |
+----------+------------+

En este caso se elige la jugada 5.
