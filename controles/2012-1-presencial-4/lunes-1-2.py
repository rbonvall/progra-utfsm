'''
# CASO 1
>>> contar_valores([5, 1, 5, 2, 3, 3, 5])
{1: 1, 2: 1, 3: 2, 5: 3}

# FIN CASO 1

# CASO 2
>>> tiene_trio([5, 1, 5, 2, 3, 3, 5])
True

# FIN CASO 2
'''

def contar_valores(cartas):
    cuentas = {}
    for c in cartas:
        if c not in cuentas:
            cuentas[c] = 0
        cuentas[c] += 1
    return cuentas

def tiene_trio(cartas):
    cuentas = contar_valores(cartas)
    for carta in cuentas:
        if cuentas[carta] >= 3:
            return True
    return False


cartas = [5, 1, 5, 2, 3, 3, 5]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

