n = int(raw_input('Numero de alumnos: '))
print

alumnos = []
promedios = []
for i in range(n):
    nombre_c = raw_input('Nombre alumno {0}: '.format(i+1))
    nombre = nombre_c.split()[0]
    string_notas = raw_input('Ingrese las notas de {0}: '.format(nombre))

    notas = map(float, string_notas.split())
    promedio = sum(notas) / len(notas)

    alumnos.append(nombre)
    promedios.append(promedio)
    print

for i in range(n):
    print 'El promedio de {0} es {1:.2f}'.format(alumnos[i], promedios[i])


