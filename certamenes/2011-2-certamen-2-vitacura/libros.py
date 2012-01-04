# coding: utf-8

def obtener_datos_libro(titulo):
    for libro in libros:
        t, autor, anno = libro
        if titulo == t:
            return (t, autor, anno)

def obtener_autor(titulo):
    _, autor, _ = obtener_datos_libro(titulo)
    return autor

def obtener_idioma(titulo):
    _, autor, _ = obtener_datos_libro(titulo)
    _, _, idioma = datos_autores[autor]
    return idioma

def calcular_annos_antes_de_morir(titulo):
    _, autor, anno_publicacion = obtener_datos_libro(titulo)
    _, (anno_defuncion, _, _), _ = datos_autores[autor]
    return (anno_defuncion - anno_publicacion)


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
print 'por', obtener_autor(titulo)
print 'El autor fallecio', calcular_annos_antes_de_morir(titulo), 'años',
print 'después de haber escrito el libro'
# FIN PROGRAMA

