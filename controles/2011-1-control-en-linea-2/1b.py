equipo = raw_input('Equipo: ')
ganados = int(raw_input('Ganados: '))
empatados = int(raw_input('Empatados: '))
perdidos = int(raw_input('Perdidos: '))
puntos = 3 * ganados + empatados
print equipo, 'tiene', puntos, 'puntos'
