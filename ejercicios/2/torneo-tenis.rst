Torneo de tenis
===============

Escriba un programa para simular un campeonato de tenis.

Primero,
debe pedir al usuario que ingrese los nombres de ocho tenistas.
A continuación,
debe pedir los resultados de los partidos
juntando los jugadores de dos en dos.
El ganador de cada partido avanza a la ronda siguiente.

El programa debe continuar preguntando ganadores de partidos
hasta que quede un único jugador, que es el campeón del torneo.

El programa en ejecución debe verse así:

.. testcase::

    Jugador 1: `Nadal`
    Jugador 2: `Melzer`
    Jugador 3: `Murray`
    Jugador 4: `Soderling`
    Jugador 5: `Djokovic`
    Jugador 6: `Berdych`
    Jugador 7: `Federer`
    Jugador 8: `Ferrer`

    Ronda 1
    a.Nadal - b.Melzer: `a`
    a.Murray - b.Soderling: `b`
    a.Djokovic - b.Berdych: `a`
    a.Federer - b.Ferrer: `a`

    Ronda 2
    a.Nadal - b.Soderling: `a`
    a.Djokovic - b.Federer: `a`

    Ronda 3
    a.Nadal - b.Djokovic: `b`

    Campeon: Djokovic

