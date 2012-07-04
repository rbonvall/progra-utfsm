'''
# CASO 1
>>> crear_reporte(controles, 2012, 1)

# FIN CASO 1

# CASO 2
>>> promedio_semestral('notas-2012-1.txt')
56

# FIN CASO 2
'''

from numpy import array

alumnos = ['Prisciliano', 'Edelmiro', 'Froilana']

controles = array([[100,  30,  50,   0,   0],
                   [ 25, 100,  35,  50,  90],
                   [ 90,  25,  50,  90, 100]])

def crear_reporte(notas, anno, semestre):
    m, n = notas.shape
    nombre_archivo = 'notas-{0}-{1}.txt'.format(anno, semestre)

    archivo = open(nombre_archivo, 'w')
    for i in range(m):
        archivo.write(alumnos[i])
        archivo.write(': ')
        archivo.write(' '.join(map(str, notas[i, :])))
        archivo.write('\n')
    archivo.close()


def promedio_semestral(nombre_archivo):
    s = 0.0
    n = 0
    archivo = open(nombre_archivo)
    for linea in archivo:
        notas = linea.split()[1:]
        s += sum(map(int, notas))
        n += len(notas)
    archivo.close()
    return int(round(s / n))


def resumen_promedios():
    promedios = []
    for anno in range(1995, 2013):
        for semestre in [1, 2]:
            if anno == 2012 and semestre == 2:
                continue
            n = 'notas-{0}-{1}.txt'.format(anno, semestre)
            p = promedio_semestral(n)
            promedios.append(p)
    return promedios


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

