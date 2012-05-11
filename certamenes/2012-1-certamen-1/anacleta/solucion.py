destino = raw_input('Destino: ')
autonomia = int(raw_input('Autonomia: '))
km = 0
llegado = False

while not llegado:

    km += autonomia
    if km == 5 or (destino == 'C' and km == 14):
        km -= 1

    if ((destino == 'B' and km >= 16) or
        (destino == 'C' and km >= 21)):
        llegado = True
    else:
        print 'Acampa en km', km

print 'Llega a', destino
