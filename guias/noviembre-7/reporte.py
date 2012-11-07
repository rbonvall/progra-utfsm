archivo = open('curso.txt')

nr_aprobados = 0
nr_reprobados = 0
promedios_certamenes = [0.0] * 5
for linea in archivo:
    datos = linea.split(':')
    nombre, apellido = datos[0:2]
    anno, mes, dia = map(int, datos[2].split('/'))
    notas = map(float, datos[3:])

    promedio = int(round(sum(notas) / len(notas)))
    if promedio < 55:
        nr_reprobados += 1
    else:
        nr_aprobados += 1

    for i in range(len(notas)):
        promedios_certamenes[i] += notas[i]

archivo.close()

total =  nr_reprobados + nr_aprobados
for i in range(len(promedios_certamenes)):
    promedios_certamenes[i] = round(promedios_certamenes[i] / total, 1)

print 'Cantidad de aprobados:', nr_aprobados
print 'Cantidad de reprobados:', nr_reprobados
print
for i in range(len(promedios_certamenes)):
    print 'Promedio certamen {}: {}'.format(i + 1, promedios_certamenes[i])

