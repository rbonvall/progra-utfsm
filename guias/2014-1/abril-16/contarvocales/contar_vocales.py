# Escriba aqui la funcion.



oracion = str(raw_input('Ingrese oracion'))
vocales = 'aeiou'
for i in range(5):
    v = vocales[i]
    c = contar(v, oracion)
    print v, 'aparece', c, 'veces'
