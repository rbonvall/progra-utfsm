antenas = [('A1', (1, 7)), ('A2', (5, 2)), ('A3', (4, 8))]
clientes = [('C1', (1, 2)), ('C2', (4, 1)), ('C3', (3, 5)),
            ('C4', (3, 9)), ('C5', (5, 7))]

from math import sqrt

def mejor_antena(antenas, clientes, c):

    cobertura = 3

    for id, pos in clientes:
        if id == c:
            cx, cy = pos
            break

    dist_min = float('inf')
    mejor_antena = None
    for nombre, pos in antenas:
        ax, ay = pos
        distancia = sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
        if distancia < cobertura and distancia < dist_min:
            dist_min = distancia
            mejor_antena = nombre

    return mejor_antena

#for c, _ in clientes:
#    print '{0}:'.format(c),
#    print mejor_antena(antenas, clientes, c)

'''
# CASO
>>> antenas = [('A1', (1, 7)), ('A2', (5, 2)), ('A3', (4, 8))]
>>> clientes = [('C1', (1, 2)), ('C2', (4, 1)), ('C3', (3, 5)),
...             ('C4', (3, 9)), ('C5', (5, 7))]
>>> mejor_antena(antenas, clientes, 'C4')
'A3'
>>> mejor_antena(antenas, clientes, 'C1')
None
# FIN CASO
'''
