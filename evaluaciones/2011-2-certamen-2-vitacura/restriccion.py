def esta_con_restriccion(digitos, dia, patente):
    d = int(patente[4])
    return d in digitos[dia]

def dias_con_restriccion(digitos, patente):
    dias = []
    for dia in digitos:
        if esta_con_restriccion(digitos, dia, patente):
            dias.append(dia)
    return dias

def dias_sin_restriccion(digitos, patente):
    dias = set()
    for dia in digitos:
        if not esta_con_restriccion(digitos, dia, patente):
            dias.add(dia)
    return dias

'''
# CASOS
>>> digitos = {'lunes': (3, 4, 5, 6), 'martes': (7, 8, 9, 0),
...            'miercoles': (1, 2, 3, 4), 'jueves': (5, 6, 7, 8),
...            'viernes': (9, 0, 1, 2)}
>>> esta_con_restriccion(digitos, 'lunes', 'BBDT35')
True
>>> dias_con_restriccion(digitos, 'BBDT35')
['lunes', 'miercoles']
>>> dias_sin_restriccion(digitos, 'BBDT35')
set(['jueves', 'martes', 'viernes'])
# FIN CASOS '''

