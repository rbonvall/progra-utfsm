# constante de gravitacion universal
G = 6.67428e-11

m1 = float(raw_input('m1: '))
m2 = float(raw_input('m2: '))
r = float(raw_input('Distancia: '))

print 'La fuerza de atraccion es',
print G * m1 * m2 / (r ** 2)

