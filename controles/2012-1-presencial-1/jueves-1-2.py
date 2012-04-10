print 'Jugadora M'
m1 = raw_input('Carta 1: ')
m2 = raw_input('Carta 2: ')

print 'Jugadora N'
n1 = raw_input('Carta 1: ')
n2 = raw_input('Carta 2: ')

if m1 == m2 and n1 != n2:
    print 'Gana M'
elif n1 == n2 and m1 != m2:
    print 'Gana N'
elif (m1 == 'c' or m2 == 'c') and (n1 != 'c' or n2 != 'c'):
    print 'Gana M'
elif (n1 == 'c' or n2 == 'c') and (m1 != 'c' or m2 != 'c'):
    print 'Gana N'
else:
    print 'Empate'
