capitales = {
    'Chile': 'Santiago',
    'Peru': 'Lima',
    'Ecuador': 'Quito',
}

for pais in capitales:
    print 'La capital de', pais, 'es', capitales[pais]

for capital in capitales.values():
    print capital, 'es una linda ciudad'

for p, c in capitales.items():
    print c, 'es la capital de', p
