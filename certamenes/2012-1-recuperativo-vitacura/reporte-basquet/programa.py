'''
# CASO 1
>>> calcular_puntos('DLLDTL')
10

# FIN CASO 1

# CASO 2
>>> leer_partidos('partidos-2012-07-02.txt')
{('Bribones', 'Zopencos'): (43, 33), ('Zoquetes', 'Alcornoques'): (34, 10),
 ('Canallas', 'Bellacos'): (25, 39), ('Mentecatos', 'Tarugos'): (39, 27)}

# FIN CASO 2

# CASO 3
Fecha: `02/07/2012`
Bribones gano a Zopencos por 43-33
Zoquetes gano a Alcornoques por 34-10
Bellacos gano a Canallas por 39-25
Mentecatos gano a Tarugos por 39-27

# FIN CASO 3
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


def programa():
    fecha = raw_input('Fecha: ')
    dia, mes, ano = fecha.split('/')
    nombre_archivo = 'partidos-{0}-{1}-{2}.txt'.format(ano, mes, dia)
    resultados = leer_partidos(nombre_archivo)
    for partido in resultados:
        p1, p2 = resultados[partido]
        e1, e2 = partido
        if p1 < p2:  # hacer que siempre e1 sea el ganador y e2 el perdedor
            e1, e2 = e2, e1
            p1, p2 = p2, p1
        print '{0} gano a {1} por {2}-{3}'.format(e1, e2, p1, p2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)

