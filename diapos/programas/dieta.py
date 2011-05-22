from numpy import *

alimentos = zeros(3)
print 'Ingrese cantidades de alimento en gramos'
alimentos[0] = float(raw_input('Leche descremada: '))
alimentos[1] = float(raw_input('Harina de soya: '))
alimentos[2] = float(raw_input('Suero de leche: '))


tabla_aportes = array([[36, 51, 13],
                       [52, 34, 74],
                       [ 0,  7,  1.1]])

nutrientes = dot(tabla_aportes, alimentos) / 100.0

print
print 'Aporte nutritivo'
print 'Proteinas: {0} gramos'.format(nutrientes[0])
print 'Carbohidratos: {0} gramos'.format(nutrientes[1])
print 'Grasa: {0} gramos'.format(nutrientes[2])

