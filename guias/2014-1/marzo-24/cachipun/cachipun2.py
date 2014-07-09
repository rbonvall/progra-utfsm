# inicializo a y b con valores iguales
# para asegurarme que se entre al ciclo
a = ''
b = ''

while a == b:
    a = raw_input('A: ')
    b = raw_input('B: ')
    if a == b:
        print 'Empate'


if   ((a == 'tijera' and b == 'papel')  or
      (a == 'papel'  and b == 'piedra') or
      (a == 'piedra' and b == 'tijera')):
    print 'La ganadora es A'
elif ((b == 'tijera' and a == 'papel')  or
      (b == 'papel'  and a == 'piedra') or
      (b == 'piedra' and a == 'tijera')):
    print 'El ganador es B'
else:
    print 'Algo raro pasa aca'

