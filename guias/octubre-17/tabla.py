from eliminatoria import partidos
from torneos import *

equipos = ordenar_equipos(partidos)

for i, equipo in enumerate(equipos, 1):
    pts = calcular_puntos(partidos, equipo)
    dif = calcular_diferencia(partidos, equipo)
    print '{0}. {1:10} {2:>4} {3:>4}'.format(i, equipo, pts, dif)


