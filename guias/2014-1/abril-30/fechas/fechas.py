def es_bisiesto(anno):
    if anno % 400 == 0:
        return True
    if anno % 100 == 0:
        return False
    return anno % 4 == 0


def dia_siguiente(fecha):
    a, m, d = fecha

    dias = [0, 31, 28, 31, 30, 31, 30,
               31, 31, 30, 31, 30, 31]
    if es_bisiesto(a):
        dias[2] = 29

    if d == 31 and m == 12:
        return (a + 1, 1, 1)
    elif d == dias[m]:
        return (a,  m + 1, 1)
    else:
        return (a, m, d + 1)


def dias_entre(f1, f2):
    c = 0
    while f1 < f2:
        f1 = dia_siguiente(f1)
        c += 1
    return c

