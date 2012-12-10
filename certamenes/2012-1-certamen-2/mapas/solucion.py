'''
# CASO 1
>>> son_vecinas(mapa, 'A', 'B')
True
>>> son_vecinas(mapa, 'C', 'G')
False

# FIN CASO 1

# CASO 2
>>> tienen_vecino_en_comun(mapa, 'C', 'E')
True
>>> tienen_vecino_en_comun(mapa, 'A', 'F')
False

# FIN CASO 2

# CASO 3
>>> existe_ruta(mapa, ['E', 'D', 'G', 'B', 'A'])
True
>>> existe_ruta(mapa, ['A', 'B', 'C', 'D', 'E'])
False

# FIN CASO 3
'''


# EJEMPLO
mapa = {
  'A': {'B', 'C'},
  'B': {'A', 'D', 'E', 'G'},
  'C': {'A', 'D'},
  'D': {'B', 'C', 'E', 'G', 'F'},
  'E': {'B', 'D', 'G'},
  'F': {'D'},
  'G': {'E', 'B', 'D'},
}
# FIN EJEMPLO


def son_vecinas(mapa, p, q):
    return p in mapa[q]

def tienen_vecino_en_comun(mapa, p, q):
    for ciudad in mapa:
        if son_vecinas(mapa, p, ciudad) and son_vecinas(mapa, ciudad, q):
            return True
    return False

def existe_ruta(mapa, ruta):
    n = len(ruta)
    for i in range(n - 1):
        if not son_vecinas(mapa, ruta[i], ruta[i + 1]):
            return False
    return True



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

