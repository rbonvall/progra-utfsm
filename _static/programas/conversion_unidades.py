km_por_milla = 1.609344
cm_por_pulgada = 2.54

def millas_a_km(mi):
    return mi * km_por_milla

def km_a_millas(km):
    return km / km_por_milla

def pulgadas_a_cm(p):
    return p * cm_por_pulgada

def cm_a_pulgadas(cm):
    return cm / cm_por_pulgada

if __name__ == '__main__':
    print 'Que conversion desea hacer?'
    print '1) millas a kilometros'
    print '2) kilometros a millas'
    print '3) pulgadas a centimetros'
    print '4) centimetros a pulgadas'
    opcion = int(raw_input('> '))

    if opcion == 1:
        x = float(raw_input('Ingrese millas: '))
        print x, 'millas =', millas_a_km(x), 'km'
    elif opcion == 2:
        x = float(raw_input('Ingrese kilometros: '))
        print x, 'km =', km_a_millas(x), 'millas'
    elif opcion == 3:
        x = float(raw_input('Ingrese pulgadas: '))
        print x, 'in =', pulgadas_a_cm(x), 'cm'
    elif opcion == 4:
        x = float(raw_input('Ingrese centimetros: '))
        print x, 'cm =', cm_a_pulgadas(x), 'in'
    else:
        print 'Opcion incorrecta'
