ca = 0
cb = 0
while ca < 3 and cb < 3:
    a = raw_input('A: ')
    b = raw_input('B: ')

    if   ((a == 'tijera' and b == 'papel')  or
          (a == 'papel'  and b == 'piedra') or
          (a == 'piedra' and b == 'tijera')):
        ca += 1
    elif ((b == 'tijera' and a == 'papel')  or
          (b == 'papel'  and a == 'piedra') or
          (b == 'piedra' and a == 'tijera')):
        cb += 1
    print ca, '-', cb
    print

if ca > cb:
    print 'La ganadora es A'
else:
    print 'La ganadora es B'
