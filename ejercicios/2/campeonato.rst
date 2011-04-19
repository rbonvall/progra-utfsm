Campeonato de fútbol
====================

Los resultados de un campeonato de fútbol
están almacenados en un diccionario.
Las llaves son los partidos
y los valores son los resultados.
Cada partido es representado como una tupla con los dos equipos que jugaron,
y el resultado es otra tupla con los goles que hizo cada equipo::

    resultados = {
       ('Honduras', 'Chile'):    (0, 1),
       ('Espana',   'Suiza'):    (0, 1),
       ('Suiza',    'Chile'):    (0, 1),
       ('Espana',   'Honduras'): (3, 0),
       ('Suiza',    'Honduras'): (0, 0),
       ('Espana',   'Chile'):    (2, 1),
    }

#. Escriba la función ``obtener_lista_equipos(resultados)``
   que reciba como parámetro el diccionario de resultados
   y retorne una lista con todos los equipos
   que participaron del campeonato::

     >>> obtener_lista_equipos(resultados)
     ['Honduras', 'Suiza', 'Espana', 'Chile']

#. El equipo que gana un partido recibe tres puntos y el que pierde, cero.
   En caso de empate, ambos equipos reciben un punto.

   Escriba la función ``calcular_puntos(equipo, resultados)``
   que entregue la cantidad de puntos obtenidos por un equipo::

    >>> calcular_puntos('Chile', resultados)
    6
    >>> calcular_puntos('Suiza', resultados)
    4

#. La *diferencia de goles* de un equipo
   es el total de goles que anotó un equipo
   menos el total de goles que recibió.

   Escriba la función ``calcular_diferencia_de_goles(equipo, resultados)``
   que entregue la diferencia de goles de un equipo::

    >>> calcular_diferencia_de_goles('Chile', resultados)
    1
    >>> calcular_diferencia_de_goles('Honduras', resultados)
    -4

#. Escriba la función ``posiciones(resultados)``
   que reciba como parámetro el diccionario de resultados,
   y retorne una lista con los equipos ordenados por puntaje de mayor a menor.
   Los equipos que tienen el mismo puntaje
   deben ser ordenados por diferencia de goles de mayor a menor.
   Si tienen los mismos puntos y la misma diferencia de goles,
   deben ser ordenados por los goles anotados::

     >>> posiciones(resultados)
     ['Espana', 'Chile', 'Suiza', 'Honduras']

   En este ejemplo,
   España queda clasificado en primer lugar porque tiene 6 puntos
   y diferencia de goles de +3,
   mientras que Chile también tiene 6 puntos,
   pero diferencia de goles de +1.

..   Para probar su función,
..   puede descargar el diccionario con los resultados
..   de `la liga alemana de 2009`_.
..   La tabla de posiciones
..   debe quedar así::
..
..     >>> posiciones(bundesliga09)
..
..   .. _la liga alemana de 2009: ../../_static/programas/bundesliga_2009.py
