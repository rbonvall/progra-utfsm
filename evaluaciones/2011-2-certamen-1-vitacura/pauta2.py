n1 = float(raw_input('C1: '))
n2 = float(raw_input('C2: '))

if n1 < 2.0 and n2 < 2.0:
    print 'Reprobado'
elif n1 > 9.0 and n2 > 9.0:
    print 'Aprobado'
else:
    n3 = float(raw_input('C3: '))
    promedio = (n1 + n2 + n3) / 3.0

    if promedio < 3.0:
        print 'Reprobado'
    elif promedio >= 7.0:
        print 'Aprobado'
    else:
        n_examen = float(raw_input('Examen: '))
        if n_examen >= 5.0:
            print 'Aprobado'
        else:
            print 'Reprobado'

