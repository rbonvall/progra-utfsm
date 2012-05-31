'''
# CASO 1
>>> contar_valores([5, 1, 5, 2, 3, 3, 5])
[1, 1, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
# FIN CASO 1

# CASO 2
>>> tiene_trio([5, 1, 5, 2, 3, 3, 5])
True
# FIN CASO 2
'''

def contar_valores(cartas):
    cuentas = []
    for numero in range(1, 14):
        c = 0
        for carta in cartas:
            if carta == numero:
                c += 1
        cuentas.append(c)
    return cuentas

def tiene_trio(cartas):
    return 3 in cartas or 4 in cartas

