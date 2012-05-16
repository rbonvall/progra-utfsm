from numpy import *

# USUARIOS
usuarios = [
    ('Jean Dupont',        'Marseille',  (1989, 11, 21)),
    ('Perico Los Palotes', 'Valparaiso', (1990,  4, 12)),
    ('Jan Kowalski',       'Krakow',     (1994,  4, 22)),
    ('Antonio Nobel',      'Valparaiso', (1983,  7,  1)),
    ('John Doe',           'Bristol',    (1977, 12, 28)),
    ('Wang Dawei',         'Shanghai',   (1981,  9, 13)),
]
# FIN USUARIOS

# AMISTADES
amistades = array([[0, 0, 1, 0, 0, 0],
                   [0, 0, 1, 1, 0, 0],
                   [1, 1, 0, 1, 1, 1], # Jan es amigo de todo el mundo
                   [0, 1, 1, 0, 1, 0],
                   [0, 0, 1, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0]])
# FIN AMISTADES

'''
# CASO
>>> obtener_amigos(4)
set([2, 3])
>>> tienen_amigos_en_comun(0, 1)
True
>>> recomendar_amigos(3)
set([0, 5])
# FIN CASO
'''
