'''
# CASOS
>>> rango_en('Valparaiso', temp)
14
>>> mayor_temperatura(temp)
30
>>> ciudad_mas_fria(temp)
'Olmue'
# FIN CASOS
'''

# EJEMPLO
temp = { 'Vina del Mar':  ( 9, 26),
         'Valparaiso':    (10, 24),
         'Quilpue' :      ( 7, 30),
         'Olmue':         ( 5, 29),
         'Limache':       ( 9, 23),
         'Villa Alemana': ( 9, 22)  }
# FIN EJEMPLO

def rango_en(ciudad, temp):
    minima, maxima = temp[ciudad]
    return maxima - minima

def mayor_temperatura(temp):
    mayor = -float('inf')
    for ciudad in temp:
        _, maxima = temp[ciudad]
        if maxima > mayor:
            mayor = maxima
    return mayor

def ciudad_mas_fria(temp):
    menor = float('inf')
    for ciudad in temp:
        minima, _ = temp[ciudad]
        if minima < menor:
            menor = minima
            c = ciudad
    return ciudad

