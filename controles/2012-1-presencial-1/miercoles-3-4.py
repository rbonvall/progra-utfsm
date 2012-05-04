print 'Jugador A'
a1 = int(raw_input('Carta 1: '))
a2 = int(raw_input('Carta 2: '))

print 'Jugador B'
b1 = int(raw_input('Carta 1: '))
b2 = int(raw_input('Carta 2: '))

if abs(a1 - a2) == 1 and abs(b1 - b2) == 1:
    print 'Empate'
elif abs(a1 - a2) == 1:
    print 'Gana A'
elif abs(b1 - b2) == 1:
    print 'Gana B'
elif min(a1, a2) < min(b1, b2):
    print 'Gana A'
elif min(a1, a2) > min(b1, b2):
    print 'Gana B'
else:
    print 'Empate'

