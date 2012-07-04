'''
# CASO
Hora actual? `10:00`
Paradero? `3`
Paso hace 90 minutos
Paso hace 55 minutos
Paso hace 2 minutos
Va a pasar en 57 minutos
Va a pasar en 100 minutos
# FIN CASO
'''

actual = raw_input('Hora actual? ')
p = int(raw_input('Paradero? '))

h_actual, m_actual = map(int, actual.split(':'))

archivo = open('paradas.txt')
for linea in archivo:
    paradas = linea.split('--')
    h_parada, m_parada = map(int, paradas[p - 1].split(':'))
    diferencia = ((60 * h_actual + m_actual) -
                  (60 * h_parada + m_parada))
    if diferencia > 0:
        print 'Paso hace {0} minutos'.format(diferencia)
    else:
        print 'Va a pasar en {0} minutos'.format(-diferencia)

archivo.close()

