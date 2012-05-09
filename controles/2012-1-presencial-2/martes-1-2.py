norte = 0
sur = 0
km = 0
distancia = 0
regresado = False
while not regresado:
    viaje = int(raw_input('Viaje: '))
    km += viaje
    distancia += abs(viaje)
    if km == 0:
        regresado = True
    if viaje > 0:
        norte += 1
    elif viaje < 0:
        sur += 1

print 'De regreso en Santiago!'
print 'Distancia recorrida:', distancia
print 'Viajes al norte:', norte
print 'Viajes al sur:', sur


