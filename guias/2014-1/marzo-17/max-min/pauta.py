a = float(raw_input('Primero: '))
b = float(raw_input('Segundo: '))
c = float(raw_input('Tercero: '))

mayor = max(a, b, c)
menor = min(a, b, c)
medio = a + b + c - mayor - menor

print 'En orden:'
print menor
print medio
print mayor

