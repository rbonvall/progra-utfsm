numeros = '0123456789'
mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras = mayusculas + minusculas
simbolos = '!#$@%&'

es_valida = False
while not es_valida:
    contrasena = raw_input('Contrasena: ')
    
    tiene_diez = len(contrasena) >= 10
    tiene_letras = False
    tiene_numeros = False
    tiene_simbolos = False
    tiene_seguidos = False
    tiene_minuscula_antes_de_mayuscula = False

    aparecio_mayuscula = False

    for i in range(len(contrasena)):
        c = contrasena[i]

        if c in letras:     tiene_letras = True
        elif c in numeros:  tiene_numeros = True
        elif c in simbolos: tiene_simbolos = True

        if c in mayusculas:
            aparecio_mayuscula = True
        elif c in minusculas and not aparecio_mayuscula:
            tiene_minuscula_antes_de_mayuscula = True

        if i > 0 and c == contrasena[i - 1]:
            tiene_seguidos = True

    es_valida = True

    if not tiene_diez:
        es_valida = False
        print 'Tiene menos de diez caracteres'
    if not tiene_letras:
        es_valida = False
        print 'No tiene letras'
    if not tiene_simbolos:
        es_valida = False
        print 'No tiene simbolos'
    if not tiene_numeros:
        es_valida = False
        print 'No tiene numeros'
    if tiene_seguidos:
        es_valida = False
        print 'Tiene caracteres repetidos seguidos'
    if tiene_minuscula_antes_de_mayuscula and aparecio_mayuscula:
        es_valida = False
        print 'Tiene minuscula antes de primera mayuscula'

print 'Contrasena valida'

