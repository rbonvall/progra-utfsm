inv = int(raw_input('Inversion inicial: '))
tasa = int(raw_input('% tasa de descuento: '))

van = -inv
mes = 1
while van < 0:
    flujo = int(raw_input('Flujo mes ' + str(mes) + ': '))
    van = van + flujo / (1 + tasa/100.0) ** mes
    print 'VAN:', int(van)
    mes = mes + 1
