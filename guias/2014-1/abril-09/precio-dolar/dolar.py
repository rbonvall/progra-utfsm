n = int(raw_input('Cuantos dias? '))
suma = 0.0
alzas = 0
altos = 0
anterior = None
mayor = 0
for i in range(n):
    x = float(raw_input('Dia ' + str(i + 1) + ': '))
    suma += x

    if x > 490:
        altos += 1

    if i > 0:
        if x > anterior:
            alzas += 1

    if x > mayor:
        mayor = x

    anterior = x

promedio = suma / n
print 'El promedio fue', round(promedio, 1)
print 'Hubo', altos, 'precios mayores que 490'
if alzas == 0:
    print 'No hubo alzas'
else:
    print 'Hubo', alzas, 'alzas'
print 'El precio mayor fue', mayor
