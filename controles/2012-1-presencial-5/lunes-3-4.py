'''
# CASO
Duracion maxima? `44`
Vuelta 3 (9:30): 50 minutos
Vuelta 5 (11:15): 45 minutos
# FIN CASO
'''

archivo = open('paradas.txt')
duracion_maxima = int(raw_input('Duracion maxima? '))

mensaje = 'Vuelta {0} ({1}:{2}): {3} minutos'

i = 1
for linea in archivo:
    paradas = linea.split('--')
    h_inicio, m_inicio = map(int, paradas[0].split(':'))
    h_termino, m_termino = map(int, paradas[-1].split(':'))
    duracion = ((60 * h_termino + m_termino) -
                (60 * h_inicio  + m_inicio))
    if duracion > duracion_maxima:
        print mensaje.format(i, h_inicio, m_inicio, duracion)
    i += 1

archivo.close()

