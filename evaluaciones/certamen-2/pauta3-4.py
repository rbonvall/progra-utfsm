# Casos de prueba con aparencia realista,
# para insertar en el enunciado del certamen.

# USUARIOS
usuarios = {
    522514: ('Jean Dupont',        'Marseille',  (1989, 11, 21)),
    587125: ('Perico Los Palotes', 'Valparaiso', (1990,  4, 12)),
    189471: ('Jan Kowalski',       'Krakow',     (1994,  4, 22)),
    914210: ('Antonio Nobel',      'Valparaiso', (1983,  7,  1)),
    # ...
}
# FIN USUARIOS

'''
# CASO MISMA CIUDAD
>>> misma_ciudad(914210, 587125)
True
>>> misma_ciudad(522514, 189471)
False
# FIN CASO MISMA CIUDAD

# CASO DIFERENCIA EDAD
>>> diferencia_edad(914210, 587125)
7
# FIN CASO DIFERENCIA EDAD
'''

# AMIGOS
amistades = {
    (198471, 289142), (138555, 429900), (349123, 781118), # ...
}
# FIN AMIGOS




# Pregunta 3

def misma_ciudad(u1, u2):
    usuario1 = usuarios[u1]
    usuario2 = usuarios[u2]
    n1, c1, (a1, m1, d1) = usuario1
    n2, c2, (a2, m2, d2) = usuario2
    return c1 == c2

def diferencia_edad(u1, u2):
    usuario1 = usuarios[u1]
    usuario2 = usuarios[u2]
    n1, c1, (a1, m1, d1) = usuario1
    n2, c2, (a2, m2, d2) = usuario2
    return abs(a2 - a1)


# Pregunta 4

def obtener_amigos(u):
    amigos = set()
    for a, b in amistades:
        if u == a:
            amigos.add(b)
        elif u == b:
            amigos.add(a)
    return amigos

def recomendar_amigos(u):
    recomendados = set()
    amigos = obtener_amigos(u)
    for amigo in amigos:
         amigos_del_amigo = obtener_amigos(amigo)
         for aa in amigos_del_amigo:
             if aa not in amigos and misma_ciudad(u, aa) and diferencia_edad(u, aa) < 10:
                 recomendados.add(aa)
    return recomendados





# Caso de prueba mas completo, para probar el programa

usuarios = {
    0: ('Z', 'A', (1990, 1, 1)),
    1: ('Y', 'A', (1979, 1, 1)),
    2: ('X', 'C', (1993, 1, 1)),
    3: ('W', 'B', (1980, 1, 1)),
    4: ('V', 'B', (1992, 1, 1)),
    5: ('U', 'B', (1980, 1, 1)),
    6: ('T', 'A', (1975, 1, 1)),
    7: ('S', 'A', (1983, 1, 1)),
    8: ('R', 'A', (1991, 1, 1)),
    9: ('Q', 'C', (1975, 1, 1)),
}
amistades = {
    (0, 1), (0, 2), (0, 3), (0, 5),
    (1, 3), (1, 6), (1, 8),
    (2, 6),
    (3, 4), (3, 6), (3, 7), (3, 8),
    (4, 7),
    (5, 6), (5, 7),
    (6, 7), (6, 9),
    (8, 9),
}

# El grafo de amistades del caso de prueba es el siguiente:
#
#        1----0----2
#       /|\  / \  /
#      / | \/   \/
#     /  | /\   /\
#    /   |/  \ /  \
#   8----3----6----5
#    \   |\  /|   /
#     \  \ \/ |  /
#      \  \/\ | /
#       \ /\ \|/
#        9  \ 7
#            \|
#             4
#
# Los amigos de 8 son 1, 3 y 9.
# Los candidatos a recomendados de 8 son 0, 6, 7 y 4,
# pero 6 no tiene la diferencia de edad apropiada,
# y 4 vive en otra ciudad.
# Tecnicamente, si seguimos el enunciado al pie de la letra,
# el 8 tambien debe ser un amigo recomendado para si mismo.

if __name__ == '__main__':

    assert not misma_ciudad(1, 2)
    assert misma_ciudad(3, 4)

    assert diferencia_edad(9, 7) == 8
    assert diferencia_edad(7, 9) == 8

    assert obtener_amigos(8) == {1, 3, 9}
    assert recomendar_amigos(8) == {0, 7, 8}

