def crear_reporte(fecha, temperaturas):
    a, m, d = fecha
    archivo = open('reporte-{0}-{1}-{2}.txt'.format(a, m, d), 'w')

    for ciudad in temperaturas:
        minima, maxima = temperaturas[ciudad]

        if maxima > 25:
            ciudad = ciudad.upper()
        archivo.write('{0}: max {1}, min {2}\n'.format(ciudad, maxima, minima))

    archivo.close()

# CASO
temp = {
  'Vina del Mar':  ( 9, 26),
  'Valparaiso':    (10, 24),
  'Quilpue' :      ( 7, 30),
  'Olmue':         ( 5, 29),
  'Limache':       ( 9, 23),
  'Villa Alemana': ( 9, 22),
}
crear_reporte((2011, 5, 14), temp)
