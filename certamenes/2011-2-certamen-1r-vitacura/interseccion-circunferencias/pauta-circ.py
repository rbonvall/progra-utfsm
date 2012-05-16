x1 = float(raw_input('x1: '))
y1 = float(raw_input('y1: '))
r1 = float(raw_input('r1: '))
x2 = float(raw_input('x2: '))
y2 = float(raw_input('y2: '))
r2 = float(raw_input('r2: '))

d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if d <= r1 + r2 and d >= abs(r1 - r2):
    print 'Se intersectan'
else:
    print 'No se intersectan'

