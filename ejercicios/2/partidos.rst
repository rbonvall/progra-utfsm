Partidos
--------
Un partido de fútbol entre dos equipos
puede ser representado como una tupla de dos equipos::

    >>> partido = ('Chile', 'España')

El resultado del partido
puede ser representado como una tupla con los goles
marcados por cada equipo::

    >>> resultado = (4, 1)

Todos los partidos de un campeonato
pueden ser representados como un diccionario
que asocia a cada partido un resultado::

    >>> campeonato = {
    ...     ('Honduras', 'Chile'):    (1, 4),
    ...     ('España',   'Suiza'):    (1, 1),
    ...     ('Chile',    'Suiza'):    (2, 0),
    ...     ('España',   'Honduras'): (1, 0),
    ...     ('Chile',    'España'):   (5, 5),
    ...     ('Suiza',    'Honduras'): (1, 2);
    ... }

#. Escriba una función ``equipos(campeonato)``
   que entregue el conjunto de los equipos
   que participaron del campeonato::

    >>> equipos(campeonato)
    {'Chile', 'Honduras', 'Suiza', 'España'}

#. Escriba una función ``nro_empates(campeonato)``
   que cuente cuántos partidos del campeonato
   terminaron en empate::

    >>> nro_empates(campeonato)
    2

#. Cuando un equipo gana un partido, recibe 3 puntos;
   cuando empata, recibe 1 punto, y cuando pierde, no recibe ninguno.
   Escriba una función ``puntos(equipo, campeonato)``
   que entregue cuántos puntos obtuvo el equipo
   en el campeonato::

    >>> puntos('Chile', campeonato)
    7
    >>> puntos('Honduras', campeonato)
    3

#. La diferencia de goles de un equipo
   es la suma de los goles que hizo
   menos la suma de los goles que le hicieron.
   Escriba una función ``dg(equipo, campeonato)``
   que entregue la diferencia de goles
   del equipo en el campeonato::

    >>> dg('Chile', campeonato)
    5
    >>> dg('Honduras', campeonato)
    -3

#. Escriba una función ``mejor_partido(campeonato)``
   que entregue cuál fue el partido con más goles::

    >>> mejor_partido(campeonato)
    ('Chile', 'España')

#. Escriba una función ``tabla_de_posiciones(campeonato)``
   que retorne una lista de tuplas
   ``(equipo, puntaje, diferencia_de_goles)``
   ordenada por puntaje de mayor a menor.
   Los equipos con el mismo puntaje
   deben estar ordenados por diferencia de goles
   de mayor a menor::

    >>> tabla_de_posiciones(campeonato)
    [('España', 6, 2), ('Chile', 6, 1), ('Suiza', 4, 0), ('Honduras', 1, -3)]

