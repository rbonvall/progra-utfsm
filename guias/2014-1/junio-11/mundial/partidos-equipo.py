equipo = raw_input('Equipo: ')
print 'Los partidos de', equipo, 'son:'

archivo = open('mundial.txt')
for linea in archivo:
    datos = linea.strip().split(',')
    eq1 = datos[1]
    eq2 = datos[2]
    ciudad = datos[-1]
    a, m, d = map(int, datos[3].split('/'))
    if equipo == datos[1] or equipo == datos[2]:
        print '{0}-{1} ({2}, {3} de junio)'.format(eq1, eq2, ciudad, d)
archivo.close()
