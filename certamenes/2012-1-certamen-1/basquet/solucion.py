anotaciones = raw_input('Anotaciones: ')
n = len(anotaciones)
puntos = 0
for i in range(n):
    a = anotaciones[i]
    if a == 'T':
        puntos += 3
    elif a == 'D':
        puntos += 2
    elif a == 'L':
        puntos += 1

print puntos, 'puntos'

