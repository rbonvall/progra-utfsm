alumnos = {
  '201199001-3': ('Esteban', 'Aguila',   (1990, 10,  5)),
  '201199003-k': ('Monica',  'Barrios',  (1989, 11, 27)),
  '201199004-8': ('Victor',  'Delgado',  (1990,  3, 18)),
  '201099077-k': ('Felipe',  'Galdames', (1991,  2, 12)),
  '201188501-5': ('Romina',  'Munoz',    (1992,  5, 25)),
  '201188502-3': ('Jean',    'Pineda',   (1990,  8, 23)),
  '201188503-1': ('Cinthia', 'Sotelo',   (1990, 10,  9)),
  '201088510-0': ('Amparo',  'Zambrano', (1991, 11, 22)),
}

inscritos = {
  'Progra':  {'201199003-k', '201199004-8', '201188503-1', '201088510-0'},
  'Mate':    {'201199001-3', '201199003-k', '201199004-8', '201099077-k'},
  'Fisica':  {'201199001-3', '201199003-k', '201099077-k', '201188502-3', '201088510-0'},
  'Quimica': {'201199001-3', '201199004-8', '201188502-3', '201188503-1', '201088510-0'},
}

def ramos_alumno(rol):
    r = []
    for ramo in inscritos:
        if rol in inscritos[ramo]:
            r.append(ramo)
    return r

# version 1
def alumno_mas_joven():
    rol_mas_joven = ''
    cumple_mas_joven = (0, 0, 0)
    for rol in alumnos:
        n, a, cumple = alumnos[rol]
        if cumple > cumple_mas_joven:
            rol_mas_joven = rol
            cumple_mas_joven = cumple
    n, a, c = alumnos[rol_mas_joven]
    return n + ' ' + a

# version 2
def alumno_mas_joven():
    cumples = []
    for n, a, c in alumnos.values():
        cumples.append(c)
    cumple_mas_joven = max(cumples)
    for n, a, c in alumnos.values():
        if c == cumple_mas_joven:
            return n + ' ' + a


