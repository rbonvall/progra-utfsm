print 'Jugadora P'
p1 = raw_input('Carta 1: ')
p2 = raw_input('Carta 2: ')

print 'Jugadora Q'
q1 = raw_input('Carta 1: ')
q2 = raw_input('Carta 2: ')

tp = 0
if p1 == 't':
  tp = tp + 1
if p2 == 't':
  tp = tp + 1

tq = 0
if q1 == 't':
  tq = tq + 1
if q2 == 't':
  tq = tq + 1

if tp > tq:
  print 'Gana P'
elif tp < tq:
  print 'Gana Q'
else:
  print 'Empate'

