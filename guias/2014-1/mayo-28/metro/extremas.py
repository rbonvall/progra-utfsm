'''
# SALIDA
Mas al norte: Vespucio Norte
Mas al sur: Plaza de Puente Alto
Mas al este: Los Dominicos
Mas al oeste: Santiago Bueras
# FIN SALIDA
'''

from metro import estaciones

inf = float('inf')
min_lat = +inf
max_lat = -inf
min_lon = +inf
max_lon = -inf

for est in estaciones:
    lat, lon = estaciones[est]
    if lat < min_lat:
        min_lat = lat
        s = est
    if lat > max_lat:
        max_lat = lat
        n = est
    if lon < min_lon:
        min_lon = lon
        o = est
    if lon > max_lon:
        max_lon = lon
        e = est

print 'Mas al norte:', n
print 'Mas al sur:', s
print 'Mas al este:', e
print 'Mas al oeste:', o



