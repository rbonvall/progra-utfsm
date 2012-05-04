deuda = 200
c_estampillas = 0
c_jarrones = 0
c_sombreros = 0
while deuda > 0:
    articulo = raw_input('Articulo: ')
    if articulo == 'estampilla':
        deuda -= 30
        c_estampillas += 1
    elif articulo == 'jarron':
        deuda -= 80
        c_jarrones += 1
    elif articulo == 'sombrero':
        deuda -= 40
        c_sombreros += 1

print 'Deuda saldada.'
print c_estampillas, 'estampillas,',
print c_jarrones,    'jarrones,',
print c_sombreros,   'sombreros.'




