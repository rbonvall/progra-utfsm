'''
# CASO 1
>>> calcular_puntos('DLLDTL')
10

# FIN CASO 1

>>> leer_partidos('partidos.txt')
# CASO 2
{('Bribones', 'Zopencos'): (43, 33),
 ('Zoquetes', 'Alcornoques'): (34, 10),
 ('Bellacos', 'Canallas'): (39, 25),
 ('Mentecatos', 'Tarugos'): (39, 27)}

# FIN CASO 2
'''


def calcular_puntos(anotaciones):
    return (anotaciones.count('L') +
            anotaciones.count('D') * 2 +
            anotaciones.count('T') * 3)


def leer_partidos(nombre_archivo):
    archivo = open(nombre_archivo)
    partidos = {}
    i = 0
    for linea in archivo:
        if i % 3 == 0:
            equipo_a, anotaciones_a = linea.split(': ')
            puntos_a = calcular_puntos(anotaciones_a)
        elif i % 3 == 1:
            equipo_b, anotaciones_b = linea.split(': ')
            puntos_b = calcular_puntos(anotaciones_b)
            partidos[equipo_a, equipo_b] = (puntos_a, puntos_b)
        i += 1
    archivo.close()
    return partidos


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)

