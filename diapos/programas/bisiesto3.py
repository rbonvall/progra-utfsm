anno = int(raw_input('Ingrese un anno: '))

if ((anno % 4 == 0 and anno % 100 != 0) or
                           anno % 400 == 0):
    print anno, 'es bisiesto'
else:
    print anno, 'no es bisiesto'
