cuenta_intercalado = 0
cuenta_repetido = 0
ultimo = ''

while cuenta_intercalado < 4 and cuenta_repetido < 4:

    r = raw_input()

    if r != ultimo:
        cuenta_repetido = 1
        cuenta_intercalado += 1
    else:
        cuenta_repetido += 1
        cuenta_intercalado = 1

    ultimo = r

if cuenta_intercalado == 4:
    print 'Usted gano'
else:
    print 'Usted perdio'
