resultados = {
   ('Honduras', 'Chile'):    (0, 1),
   ('Espana',   'Suiza'):    (0, 1),
   ('Suiza',    'Chile'):    (0, 1),
   ('Espana',   'Honduras'): (3, 0),
   ('Suiza',    'Honduras'): (0, 0),
   ('Espana',   'Chile'):    (2, 1),
}

def obtener_lista_equipos():
    equipos = set()
    for e1, e2 in resultados:
        equipos.add(e1)
        equipos.add(e2)
    return list(equipos)

def calcular_puntos(equipo):
    p = 0
    for (e1, e2), (g1, g2) in resultados.items():
        if equipo == e1:
            if g1 > g2:
                p = p + 3
            elif g1 == g2:
                p = p + 1
        elif equipo == e2:
            if g1 < g2:
                p = p + 3
            elif g1 == g2:
                p = p + 1
    return p

def calcular_diferencia(equipo):
    dif = 0
    for (e1, e2), (g1, g2) in resultados.items():
        if equipo == e1:
            dif = dif + g1 - g2
        elif equipo == e2:
            dif = dif + g2 - g1
    return dif
