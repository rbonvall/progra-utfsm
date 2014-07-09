def es_navidad(fecha):
    anno, mes, dia = fecha
    return mes == 12 and dia == 25

def nombre_completo(persona):
    nombre, apellido, _ = persona
    return nombre + ' ' + apellido

def edad(persona):
    _, _, fecha = persona
    anno, _, _ = fecha
    return 2014 - anno


def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x1 - x2
    dy = y1 - y2
    return (dx ** 2 + dy ** 2) ** 0.5


def punto_medio(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xm = 0.5 * (x1 + x2)
    ym = 0.5 * (y1 + y2)
    return (xm, ym)


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
