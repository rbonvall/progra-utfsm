Cachipún
========
En cada ronda del juego del cachipún,
los dos competidores deben elegir
entre jugar tijera, papel o piedra.

Las reglas para decidir quién gana la ronda son:
tijera le gana a papel,
papel le gana a piedra,
piedra le gana a tijera,
y todas las demás combinaciones son empates.

El ganador del juego
es el primero que gane tres rondas.

Escriba un programa que pregunte a cada jugador cuál es su jugada,
muestre cuál es el marcador después de cada ronda,
y termine cuando uno de ellos haya ganado tres rondas.
Los jugadores deben indicar su jugada
escribiendo ``tijera``, ``papel`` o ``piedra``.

.. testcase::

    A: `tijera`
    B: `papel`
    1 - 0

    A: `tijera`
    B: `tijera`
    1 - 0

    A: `piedra`
    B: `papel`
    1 - 1

    A: `piedra`
    B: `tijera`
    2 - 1

    A: `papel`
    B: `papel`
    2 - 1

    A: `papel `
    B: `piedra`
    3 - 1

    A es el ganador

