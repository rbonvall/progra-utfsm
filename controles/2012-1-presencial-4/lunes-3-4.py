'''
# CASO 1
>>> producto_mas_caro(precios)
'arroz'

# FIN CASO 1

# CASO 2
>>> monto_total(precios, {'arroz': 2, 'cafe': 1})
5500

# FIN CASO 2
'''

def producto_mas_caro(precios):
    precio_mayor = -1
    for producto in precios:
        if precios[producto] > precio_mayor:
            precio_mayor = precios[producto]
            mas_caro = producto
    return mas_caro


def monto_total(precios, compra):
    s = 0
    for p in compra:
        s += precios[p] * compra[p]
    return s

# EJEMPLO PRECIOS
precios = { 'aceite': 500,  'arroz': 2000,
            'cafe':  1500,  'te':     300 }
# FIN EJEMPLO PRECIOS


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

