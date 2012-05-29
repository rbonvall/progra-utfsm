n_ues = int(raw_input('Numero de universidades: '))
print

u_aceptan = 0
u_rechazan = 0
u_empates = 0

for i in range(n_ues):
    nombre = raw_input('Universidad: ')
    voto = ''

    aceptar = 0
    rechazar = 0
    nulos = 0
    blancos = 0

    while voto != 'X':

        voto = raw_input('Voto: ')
        if voto == 'A':
            aceptar = aceptar + 1
        elif voto == 'R':
            rechazar = rechazar + 1
        elif voto == 'N':
            nulos = nulos + 1
        elif voto == 'B':
            blancos = blancos + 1

    print nombre + ':',
    print aceptar, 'aceptan,',
    print rechazar, 'rechazan,',
    print blancos, 'blancos,',
    print nulos, 'nulos.'
    print

    if aceptar > rechazar:
        u_aceptan += 1
    elif aceptar == rechazar:
        u_empates += 1
    else:
        u_rechazan += 1

print 'Universidades que aceptan:', u_aceptan
print 'Universidades que rechazan:', u_rechazan
print 'Universidades con empate:', u_empates
