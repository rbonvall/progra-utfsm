dist = float(raw_input('Distancia: '))
angulo = float(raw_input('Angulo: '))

sector = int(angulo * 8.0 / 360.0)

if dist > 47:
    print 'FUERA DE LA PLAZA'
elif dist < 7:
    print 'PILETA'
elif 45 < angulo < 90:
    print 'PUBLICO'
elif 20 < dist < 35 and sector % 2 == 0:
    print 'AREA VERDE'
else:
    print 'CEMENTO'
