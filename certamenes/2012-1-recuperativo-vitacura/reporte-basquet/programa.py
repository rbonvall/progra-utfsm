'''
>>> calcular_puntos('DLLDTL')
10
'''


def calcular_puntos(anotaciones):
    return (anotaciones.count('L') +
            anotaciones.count('D') * 2 +
            anotaciones.count('T') * 3)

