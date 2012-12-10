'''
# CASO 1
>>> destruye(bomba, (5, 3))
True
>>> destruye(bomba, (9, 9))
False

# FIN CASO 1

# CASO 2
>>> obtener_impactos(bomba, objetivos)
array([1, 0, 0, 0, 1, 1, 0, 0, 0])

# FIN CASO 2

'''


from random import random
from numpy import zeros, any
from math import sqrt

# MAPA
objetivos = [
  (3.9, 2.1), (8.7, 0.3), (9.1, 8.2),
  (0.9, 9.5), (5.5, 5.5), (4.5, 4.5),
  (1.4, 6.2), (7.7, 8.4), (9.1, 3.1),
]
bomba = (5.1, 3.7, 3.0)
# FIN MAPA

def bomba_aleatoria():
    x = 10 * random()
    y = 10 * random()
    return (x, y, 0.5)

def destruye(bomba, objetivo):
    xb, yb, r = bomba
    x, y = objetivo
    dx = x - xb
    dy = y - yb
    return sqrt(dx ** 2 + dy ** 2) < r

def obtener_impactos(bomba, objetivos):
    n = len(objetivos)
    impactos = zeros(n).astype(int)
    for i in range(n):
        if destruye(bomba, objetivos[i]):
            impactos[i] = 1
    return impactos

def bombardear(objetivos):
    n = len(objetivos)
    impactos = zeros(n).astype(int)
    bombas = []
    while any(impactos == 0):
        b = bomba_aleatoria()
        i = obtener_impactos(b, objetivos)
        impactos = impactos + i
        bombas.append(b)
    return bombas

