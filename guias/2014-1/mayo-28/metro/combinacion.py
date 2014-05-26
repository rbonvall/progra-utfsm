'''
# SALIDA
San Pablo es combinacion entre 1 y 5
Baquedano es combinacion entre 1 y 5
La Cisterna es combinacion entre 2 y 4A
...
# FIN SALIDA
'''

from metro import estaciones

for a in estaciones:
    for b in estaciones:
        if a >= b:
            continue
        en_comun = set(estaciones[a]) & set(estaciones[b])
        for estacion in en_comun:
            print estacion, 'es combinacion entre', a, 'y', b
