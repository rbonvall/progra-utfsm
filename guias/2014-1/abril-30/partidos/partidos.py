# PARTIDOS
partidos = [
    (('Honduras', 'Chile'),  (0, 1)),
    (('Espana', 'Suiza'),    (0, 1)),
    (('Suiza', 'Chile'),     (0, 1)),
    (('Espana', 'Honduras'), (2, 0)),
    (('Espana', 'Chile'),    (2, 1)),
    (('Suiza', 'Honduras'),  (0, 0)),
]
# FIN PARTIDOS

def ganador(partido):
    equipos, resultado = partido
    l, v = equipos
    gl, gv = resultado
    if gl > gv:
        return l
    elif gl == gv:
        return 'Empate'
    else:
        return v

def jugo(equipo, partido):
    equipos, _ = partido
    return equipo in equipos

def puntos(equipo, partidos):
    pts = 0
    for partido in partidos:
        if jugo(equipo, partido):
            g = ganador(partido)
            if g == equipo:
                pts += 3
            elif g == 'Empate':
                pts += 1
    return pts
