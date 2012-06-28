'''
# CASO 1
>>> contar_estrellitas(controles)
array([2, 1, 3])

# FIN CASO 1

# CASO 2
>>> notas_finales(controles, 2)
array([ 46.,  60.,  81.])
>>> notas_finales(controles, 3)
array([ 36.,  60.,  81.])

# FIN CASO 2

# CASO 3
>>> alumno_con_mas_estrellitas(controles)
'Froilana'

# FIN CASO 3

'''

from numpy import array

# ALUMNOS
alumnos = ['Prisciliano', 'Edelmiro', 'Froilana']
# FIN ALUMNOS

# CONTROLES
controles = array([[100,  30,  50,   0,   0],
                   [ 25, 100,  35,  50,  90],
                   [ 90,  25,  50,  90, 100]])
# FIN CONTROLES

def contar_estrellitas(controles):
    return (controles == controles.max(0)).sum(1)

def notas_finales(controles, n):
    e = contar_estrellitas(controles)
    return controles.mean(1) + 10 * (e >= n)

def alumno_con_mas_estrellitas(controles):
    e = contar_estrellitas(controles)
    return alumnos[e.argmax()]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

