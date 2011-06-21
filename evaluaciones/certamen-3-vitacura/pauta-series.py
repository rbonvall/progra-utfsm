from numpy import *

def medias_moviles(serie, p):
    n = serie.size - p + 1
    mm = zeros(n)
    for i in range(n):
        mm[i] = serie[i : i + p].mean()
    return mm

def diferencias_finitas(serie):
    return serie[1:] - serie[:-1]


if __name__ == '__main__':
    s = array([5, 2, 2, 8, -4, -1, 2])
    print s
    print medias_moviles(s, 3).astype(int)
    print diferencias_finitas(s)
