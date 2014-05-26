'''
# SALIDA
Mas al norte: Vespucio Norte
Mas al sur: Plaza de Puente Alto
Mas al este: Los Dominicos
Mas al oeste: Santiago Bueras
# FIN SALIDA
'''

from metro import coordenadas

inf = float('inf')
min_lat = +inf
max_lat = -inf
min_lon = +inf
max_lon = -inf

for estacion in coordenadas:
    lat, lon = coordenadas[estacion]
    if lat < min_lat:
        min_lat = lat
        s = estacion
    if lat > max_lat:
        max_lat = lat
        n = estacion
    if lon < min_lon:
        min_lon = lon
        o = estacion
    if lon > max_lon:
        max_lon = lon
        e = estacion

print 'Mas al norte:', n
print 'Mas al sur:', s
print 'Mas al este:', e
print 'Mas al oeste:', o



