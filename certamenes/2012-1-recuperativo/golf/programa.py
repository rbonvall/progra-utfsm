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


print obtener_marcador()

