# PARTIDOS
campeonato = {
  ('Honduras', 'Chile'):  (0, 1),
  ('Espana', 'Suiza'):    (0, 1),
  ('Suiza', 'Chile'):     (0, 1),
  ('Espana', 'Honduras'): (2, 0),
  ('Espana', 'Chile'):    (2, 1),
  ('Suiza', 'Honduras'):  (0, 0),
}
# FIN PARTIDOS

def obtener_equipos(campeonato):
    equipos = []
    for partido in campeonato:
        local, visita = partido
        if local not in equipos:
            equipos.append(local)
        if visita not in equipos:
            equipos.append(visita)
    equipos.sort()
    return equipos

def puntos(equipo, campeonato):
    pts = 0
    for p in campeonato:

        # desempaquetar equipos y goles
        local, visita = p
        gl, gv = campeonato[p]

        if equipo == local:
            if gl > gv:
                pts += 3
            elif gl == gv:
                pts += 1

        elif equipo == visita:
            if gv > gl:
                pts += 3
            elif gv == gl:
                pts += 1

        # No es necesario el else, porque cuando el equipo
        # no es ni el local ni la visita (es decir, no jugo
        # el partido) no hay que hacer nada.

    return pts


# Solucion 1: usar las funciones que definimos arriba.
def calcular_tabla(campeonato):
    tabla = {}
    equipos = obtener_equipos(campeonato)
    for equipo in equipos:
        tabla[equipo] = puntos(equipo, campeonato)
    return tabla

# Solucion 2: recorrer todos los partidos.
def calcular_tabla2(campeonato):
    tabla = {}
    for partido in campeonato:

        # Desempaquetar equipos.
        local, visita = partido

        # Desempaquetar goles del partido.
        gl, gv = campeonato[partido]

        # Agregar al diccionario los equipos de este partido
        # si es que aun no estan en el.
        if local not in tabla:
            tabla[local] = 0
        if visita not in tabla:
            tabla[visita] = 0

        # Sumar los puntos dependiendo del resultado.
        if gl > gv:
            tabla[local] += 3
        elif gl < gv:
            tabla[visita] += 3
        else:
            tabla[local] += 1
            tabla[visita] += 1

    return tabla


def determinar_campeon(campeonato):
    maximo = -1
    tabla = calcular_tabla(campeonato)
    for equipo in tabla:
        pts = tabla[equipo]
        if pts > maximo:
            maximo = pts
            campeon = equipo
    return campeon

