n = int(raw_input('n: '))
n_productos = int(raw_input('Cantidad productos: '))

total = 0
total_parcial = 0
descuento = 0
tasa = 0.2

for i in range(1, n_productos + 1):
    p = int(raw_input('Precio producto ' + str(i) + ': '))

    total += p
    total_parcial += p

    if i % n == 0:
        descuento += int(tasa * total_parcial)
        total_parcial = 0
        tasa = tasa / 2.0

print 'Total:', total
print 'Descuento:', descuento
print 'Por pagar:', total - descuento
