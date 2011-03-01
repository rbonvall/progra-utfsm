anno = int(raw_input('Ingrese un anno: '))

if anno % 400 == 0:
    print anno, 'es bisiesto'
elif anno % 100 == 0:
    print anno, 'no es bisiesto'
elif anno % 4 == 0:
    print anno, 'es bisiesto'
else:
    print anno, 'no es bisiesto'
