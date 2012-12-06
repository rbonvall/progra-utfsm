def contar_partidos(partidos):
    return len(partidos)

def obtener_equipos(partidos):
    equipos = set()
    for local, visita in partidos:
        equipos.add(local)
        equipos.add(visita)
    equipos = list(equipos)
    equipos.sort()
    return equipos

def obtener_fechas(partidos):
    fechas = set()
    for p in partidos:
        fecha, _ = partidos[p]
        fechas.add(fecha)
    fechas = list(fechas)
    fechas.sort()
    return fechas


def calcular_puntos(partidos, equipo):
    puntos = 0
    for p in partidos:
        _, resultado = partidos[p]
        if resultado == None:
            continue
        local, visita = p
        gl, gv = resultado
        if equipo == local:
            if gl > gv:
                puntos += 3
            elif gl == gv:
                puntos += 1
        elif equipo == visita:
            if gl < gv:
                puntos += 3
            elif gl == gv:
                puntos += 1
    return puntos

def calcular_diferencia(partidos, equipo):
    diferencia = 0
    for p in partidos:
        _, resultado = partidos[p]
        if resultado == None:
            continue
        gl, gv = resultado
        local, visita = p
        if equipo == local:
            diferencia += (gl - gv)
        elif equipo == visita:
            diferencia += (gv - gl)
    return diferencia

def ordenar_equipos(partidos):
    equipos = obtener_equipos(partidos)
    estadisticas = []
    for equipo in equipos:
        pts = calcular_puntos(partidos, equipo)
        dif = calcular_diferencia(partidos, equipo)
        estadisticas.append((pts, dif, equipo))
    estadisticas.sort()
    estadisticas.reverse()

    equipos_ordenados = []
    for _, _, equipo in estadisticas:
        equipos_ordenados.append(equipo)
    return equipos_ordenados




