# Algunas manos para que pruebe sus funciones.

# Nada
nada = {(12, 'D'), (7, 'P'), (5, 'C'), (3, 'T'), (10, 'P')}

# Parejas
par1 = {(13, 'T'), (13, 'D'), (7, 'T'), (2, 'P'), (11, 'C')}
par2 = {(13, 'T'), (13, 'D'), (7, 'T'), (2, 'P'), (11, 'C')}

# Dobles parejas
dp1 = {(12, 'D'), (12, 'P'), (5, 'C'), (2, 'T'), (5, 'P')}
dp2 = {(9, 'C'), (4, 'T'), (11, 'C'), (11, 'T'), (4, 'P')}

# Trios
trio1 = {(8, 'C'), (8, 'P'), (8, 'T'), (2, 'T'), (10, 'D')}
trio2 = {(3, 'T'), (12, 'P'), (3, 'C'), (2, 'P'), (3, 'D')}

# Escaleras
esc1 = {(9, 'P'), (8, 'D'), (7, 'P'), (6, 'C'), (5, 'T')}
esc2 = {(4, 'T'), (6, 'P'), (5, 'D'), (7, 'C'), (3, 'D')}
esc3 = {(10, 'T'), (11, 'P'), (12, 'D'), (13, 'T'), (1, 'D')}

# Colores
col1 = {(1, 'C'), (12, 'C'), (3, 'C'), (9, 'C'), (8, 'C')}
col2 = {(4, 'T'), (9, 'T'), (2, 'T'), (13, 'T'), (11, 'T')}

# Fulls
full1 = {(2, 'C'), (3, 'T'), (2, 'P'), (3, 'P'), (3, 'D')}
full2 = {(12, 'T'), (12, 'C'), (12, 'D'), (1, 'C'), (1, 'D')}

# Poquers
pk1 = {(1, 'C'), (1, 'T'), (7, 'D'), (1, 'P'), (1, 'D')}
pk2 = {(12, 'C'), (7, 'T'), (7, 'D'), (7, 'C'), (7, 'P')}

# Escaleras de color
ec1 = {(9, 'D'), (10, 'D'), (7, 'D'), (8, 'D'), (11, 'D')}
ec2 = {(4, 'T'), (2, 'T'), (5, 'T'), (6, 'T'), (3, 'T')}

# Escaleras reales
er1 = {(12, 'T'), (1, 'T'), (10, 'T'), (13, 'T'), (11, 'T')}
er2 = {(1, 'C'), (12, 'C'), (11, 'C'), (13, 'C'), (10, 'C')}


# Funciones auxiliares
def valores(mano):
    v = []
    for pinta, _ in mano:
        v.append(pinta)
    return v

def palos(mano):
    p = []
    for _, palo in mano:
        p.append(palo)
    return p

def contar(valores):
    c = {}
    for x in valores:
        if x not in c:
            c[x] = 0
        c[x] += 1
    return c

def valores_diccionario(d):
    v = []
    for x in d:
        v.append(d[x])
    return v

def cuentas_valores(mano):
    v = valores(mano)
    c = contar(v)
    vd = valores_diccionario(c)
    vd.sort()
    return vd


def es_pareja(mano):
    return len(set(valores(mano))) == 4

def es_doble_pareja(mano):
    return cuentas_valores(mano) == [1, 2, 2]

def es_trio(mano):
    return cuentas_valores(mano) == [1, 1, 3]

def es_escalera(mano):
    v = set(valores(mano))
    return len(v) == 5 and max(v) - min(v) == 4

def es_color(mano):
    return len(set(palos(mano))) == 1

def es_full(mano):
    return cuentas_valores(mano) == [2, 3]

def es_poquer(mano):
    return cuentas_valores(mano) == [1, 4]

def es_escalera_de_color(mano):
    return es_escalera(mano) and es_color(mano)

def es_escalera_real(mano):
    return es_color(mano) and set(valores(mano)) == {10, 11, 12, 13, 1}


assert map(es_pareja,        [par1,  par2,  nada]) == [True, True, False]
assert map(es_doble_pareja,  [dp1,   dp2,   nada]) == [True, True, False]
assert map(es_trio,          [trio1, trio2, nada]) == [True, True, False]
assert map(es_escalera,      [esc1,  esc2,  nada]) == [True, True, False]
assert map(es_color,         [col1,  col2,  nada]) == [True, True, False]
assert map(es_full,          [full1, full2, nada]) == [True, True, False]
assert map(es_poquer,        [pk1,   pk2,   nada]) == [True, True, False]
assert map(es_escalera_de_color, [ec1, ec2, nada]) == [True, True, False]
assert map(es_escalera_real, [er1,   er2,   nada]) == [True, True, False]

