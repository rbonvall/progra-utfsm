from random import random

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

