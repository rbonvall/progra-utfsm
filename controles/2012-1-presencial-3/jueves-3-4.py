'''
# CASO 1
>>> distancia_recorrida([40, -70, -20, 100, -50])
280
# FIN CASO 1

# CASO 2
>>> llego_de_regreso([40, -70, -20, 100, -50])
True
# FIN CASO 2
'''

def distancia_recorrida(viajes):
    distancia = 0
    for viaje in viajes:
        distancia += abs(viaje)
    return distancia

def llego_de_regreso(viajes):
    return sum(viajes) == 0
