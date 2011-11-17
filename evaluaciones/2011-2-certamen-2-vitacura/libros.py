# coding: utf-8

def obtener_autor(titulo):
    for libro in libros:
        t, a, _ = libro
        if titulo == t:
            return a

def obtener_idioma(titulo):
    autor = obtener_autor(titulo)
    _, _, idioma = datos_autores[autor]
    return idioma

def obtener_anno_defuncion_autor(titulo):
    autor = obtener_autor(titulo)
    _, defuncion, _ = datos_autores[autor]
    anno, mes, dia = defuncion
    return anno

def obtener_edad_autor(titulo):
    autor = obtener_autor(titulo)
    nacimiento, defuncion, _ = datos_autores[autor]
    an, _, _ = nacimiento
    ad, _, _ = defuncion
    return ad - an


# PROGRAMA
libros = [
    ('Papelucho programador', 'Marcela Paz', 1983),
    ('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
    ('Raw_input y Julieta', 'William Shakespeare', 1597),
    ('La tuplamorfosis', 'Franz Kafka', 1915),
    # ...
]

datos_autores = {
    # autor: nacimiento, defuncion, idioma
    'William Shakespeare': ((1564,  4, 26), (1616,  5,  3), 'inglés'),
    'Franz Kafka':         ((1883,  7,  3), (1924,  6,  3), 'alemán'),
    'Marcela Paz':         ((1902,  2, 28), (1985,  6, 12), 'español'),
    'Miguel de Cervantes': ((1547,  9, 29), (1616,  4, 22), 'español'),
    # ...
}

titulo = raw_input('Ingrese titulo del libro: ')
print 'El libro fue escrito en', obtener_idioma(titulo),
print 'por', obtener_autor(titulo),
print 'que murió en el año', obtener_anno_defuncion_autor(titulo),
print 'a la edad de', obtener_edad_autor(titulo), 'años.'
# FIN PROGRAMA

