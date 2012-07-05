'''
# CASO 1
>>> calcular_notas(ponderaciones, totales, puntajes)
array([ 88,  75,  79,  68, 100,  68,  21,  80])

# FIN CASO 1
'''

from numpy import array

# PLANILLA
ponderaciones = array([30, 35, 35])
totales       = array([ 8, 14, 14])

puntajes = array([[ 8, 12, 11],
                  [ 8,  9,  9],
                  [ 7, 12,  9],
                  [ 6,  9,  9],
                  [ 8, 14, 14],
                  [ 6,  8, 10],
                  [ 5,  0,  1],
                  [ 6, 14,  9]])
# FIN PLANILLA


def calcular_notas(ponderaciones, totales, puntajes):
    subtotales = ponderaciones * puntajes / totales.astype(float)
    return subtotales.sum(1).round().astype(int)

    # Si no convierte a int, tambien considerelo correcto.


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
