total = 0
i = 1
mayor_donacion = 0
while total < 20000:
    donacion = int(raw_input('Donacion: '))
    total += donacion
    if donacion > mayor_donacion:
        mayor_donacion = donacion
        donante = i
    i += 1

print 'Se logro la meta!'
print 'Gracias al donante', donante,
print 'por aportar', mayor_donacion




