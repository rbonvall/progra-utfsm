'''
# SALIDA
San Pablo es combinacion entre 1 y 5
Baquedano es combinacion entre 1 y 5
La Cisterna es combinacion entre 2 y 4A
...
# FIN SALIDA
'''

from metro import lineas

for a in lineas:
    for b in lineas:
        if a != b:
            en_comun = set(lineas[a]) & set(lineas[b])
            for estacion in en_comun:
                print estacion, 'es combinacion entre', a, 'y', b


