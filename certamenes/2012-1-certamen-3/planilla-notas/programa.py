'''
# CASO 1
>>> calcular_notas(ponderaciones, totales, puntajes)
array([ 88,  75,  79,  68, 100,  68,  21,  80])

# FIN CASO 1

# CASO 2
>>> inflar(puntajes, totales, 3, 0.8)
>>> puntajes
array([[ 8, 12, 11],
       [ 8,  9, 10],
       [ 7, 12, 10],
       [ 6,  9, 10],
       [ 8, 14, 14],
       [ 6,  8, 10],
       [ 5,  0,  3],
       [ 6, 14, 10]])

# FIN CASO 2

# EJEMPLO ROUND
>>> a = array([54.8, 91.1, 54.2])
>>> a.round()
array([ 55.,  91.,  54.])

# FIN EJEMPLO ROUND

# CASO 3
>>> contar_puntajes_completos(ponderaciones, totales, puntajes)
array([3, 2, 1])

# FIN CASO 3
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


def inflar(puntajes, totales, pregunta, f):
    j = pregunta - 1
    puntajes[:, j] = f  * puntajes[:, j] + (1 - f) * totales[j]


def contar_puntajes_completos(ponderaciones, totales, puntajes):
    return (puntajes == totales).sum(0)



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
