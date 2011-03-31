def contar(letra, oracion):
    c = 0
    n = len(oracion)
    for i in range(n):
        if oracion[i] == letra:
            c = c + 1
    return c

oracion = str(raw_input('Ingrese oracion'))
vocales = 'aeiou'
for i in range(5):
    v = vocales[i]
    c = contar(v, oracion)
    print v, 'aparece', c, 'veces'
