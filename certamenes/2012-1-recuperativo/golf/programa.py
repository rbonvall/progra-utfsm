'''
# CASO 1
>>> leer_valores('pares.txt')
array([5, 3, 3, 4, 3, 5, 3, 3, 5, 4, 3, 3, 4, 4, 3, 5, 4, 4])

# FIN CASO 1

# CASO 2
>>> obtener_marcador()
{'Jack Nicolas': -1, 'Arnoldo Palmeras': 2, 'Tiguerio Gutierrez': 0}

# FIN CASO 2

'''


from numpy import zeros

def leer_valores(nombre_archivo):
    valores = zeros(18).astype(int)
    archivo = open(nombre_archivo)
    i = 0
    for linea in archivo:
        valores[i] = int(linea)
        i += 1
    archivo.close()
    return valores


def obtener_marcador():
    marcador = {}
    archivo_jugadores = open('jugadores.txt')
    pares = leer_valores('pares.txt')
    for jugador in archivo_jugadores:
        jugador = jugador.strip()
        n = jugador.lower().replace(' ', '-')
        nombre_archivo =  'golpes-{0}.txt'.format(n)
        golpes = leer_valores(nombre_archivo)
        marcador[jugador] = (golpes - pares).sum()
    archivo_jugadores.close()
    return marcador


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,
                    optionflags=doctest.NORMALIZE_WHITESPACE)

