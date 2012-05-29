'''
# CASO
>>> calcular_puntaje(['T', 'D', 'L', 'D'])
8
>>> ganador_partido(['T', 'T'], ['D', 'L', 'L'])
'A'
# FIN CASO
'''

def calcular_puntaje(anotaciones):
    s = 0
    for a in anotaciones:
        if a == 'T':
            s += 3
        elif a == 'D':
            s += 2
        else:
            s += 1
    return s

def ganador_partido(anotaciones_a, anotaciones_b):
    pa = calcular_puntaje(anotaciones_a)
    pb = calcular_puntaje(anotaciones_b)
    if pa > pb:
        return 'A'
    elif pb > pa:
        return 'B'
    return 'Empate'

