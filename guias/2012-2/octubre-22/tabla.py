from eliminatoria import partidos
from torneos import ordenar_equipos, calcular_puntos, calcular_diferencia

def linea(c, n=23):
    print c * n

equipos = ordenar_equipos(partidos)

linea('=')
print '   {:10} {:>4} {:>4}'.format('Equipo', 'Pts', 'Dif')
linea('-')
for i, equipo in enumerate(equipos, 1):
    pts = calcular_puntos(partidos, equipo)
    dif = calcular_diferencia(partidos, equipo)
    print '{}. {:10} {:>4} {:>+4}'.format(i, equipo, pts, dif)
linea('=')


