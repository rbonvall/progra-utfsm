alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
asistencia = [
    [True,  True,  True,  False, False, False, False],
    [True,  True,  True,  False, True,  False, True ],
    [True,  True,  True,  True,  True,  True,  True ],
    [True,  True,  True,  False, True,  True,  True ]
]


# version 1
def total_por_alumno(tabla):
    t = []
    for fila in tabla:
        c = 0
        for asistio in fila:
            if asistio:
                c += 1
        t.append(c)
    return t

# version 2
def total_por_alumno(tabla):
    t = []
    for fila in tabla:
        c = fila.count(True)
        t.append(c)
    return t

# version 3
def total_por_alumno(tabla):
    t = []
    for fila in tabla:
        t.append(sum(fila))
    return t

# version 4
def total_por_alumno(tabla):
    return map(sum, tabla)


def total_por_clase(tabla):
    nr_alumnos = len(tabla)
    nr_clases = len(tabla[0])
    t = [0] * nr_clases
    for i in range(nr_alumnos):
        for j in range(nr_clases):
            if tabla[i][j]:
                t[j] = t[j] + 1
    return t


def alumno_estrella(tabla):
    totales = total_por_alumno(tabla)
    x = max(totales)
    i = totales.index(x)
    return alumnos[i]
