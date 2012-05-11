anotaciones = raw_input('Anotaciones: ')
n = len(anotaciones)
puntos = 0
total = 0
periodo = 1
for i in range(n):
    a = anotaciones[i]
    if a == 'T':
        puntos += 3
    elif a == 'D':
        puntos += 2
    elif a == 'L':
        puntos += 1
    elif a == ' ':
        print puntos, 'puntos en el periodo', periodo
        total += puntos
        puntos = 0
        periodo += 1

total += puntos
print puntos, 'puntos en el periodo', periodo
print 'Total:', total, 'puntos'


