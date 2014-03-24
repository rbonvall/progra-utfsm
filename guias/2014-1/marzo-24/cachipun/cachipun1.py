a = raw_input('A: ')
b = raw_input('B: ')

while a == b:
    print 'Empate'
    a = raw_input('A: ')
    b = raw_input('B: ')

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

