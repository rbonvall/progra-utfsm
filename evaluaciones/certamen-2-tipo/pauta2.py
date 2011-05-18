def estadisticas_equipo(nombre_equipo):
    g, e, p = 0, 0, 0

    for anno in range(1990, 2011):
        archivo_resultados = open('{0}.txt'.format(anno))

        for linea in archivo_resultados:
            linea = linea.strip()
            equipos, resultado = linea.split(':')
            equipo1, equipo2 = equipos.split('-')
            goles1, goles2 = map(int, resultado.split('-'))
            if nombre_equipo == equipo1:
            elif nombre_equipo == equipo1:

        archivo_resultados.close()

    return (g, e, p)
