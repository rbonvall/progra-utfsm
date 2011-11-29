n = int(raw_input('Cuantos valores ingresara? '))

minimo =  float('inf')
maximo = -float('inf')
for i in range(n):
    x = float(raw_input('Valor ' + str(i + 1) + ': '))
    if x < minimo:
        minimo = x
    if x > maximo:
        maximo = x

rango = maximo - minimo
print 'El rango es', rango

