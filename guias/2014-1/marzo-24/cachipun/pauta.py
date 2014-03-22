a = raw_input('A: ')
b = raw_input('B: ')
while a == b:
    print 'Empate'
    print
    a = raw_input('A: ')
    b = raw_input('B: ')
if   ((a == 'papel'  and b == 'piedra') or
      (a == 'piedra' and b == 'tijera') or
      (a == 'tijera' and b == 'papel')):
    print 'La ganadora es A'
elif ((b == 'papel'  and a == 'piedra') or
      (b == 'piedra' and a == 'tijera') or
      (b == 'tijera' and a == 'papel')):
    print 'El ganador es B'
else:
    print 'Invalido'
