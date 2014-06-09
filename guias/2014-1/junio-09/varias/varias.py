def contar_palabras(oracion):
    palabras = oracion.lower().split()
    cuenta = {}
    for palabra in palabras:
        if palabra not in cuenta:
            cuenta[palabra] = 0
        cuenta[palabra] += 1
    return cuenta

def complementaria(adn):
    return (adn.replace('g', 'x')
               .replace('c', 'g')
               .replace('x', 'c')
               .replace('a', 'x')
               .replace('t', 'a')
               .replace('x', 't'))

def tipo_de_correo(email):
    usuario, dominio = email.split('@')
    return dominio.split('.')[0]

def textualizar(tuplas):
    strings = []
    for t in tuplas:
        s = '-'.join(map(str, t))
        strings.append(s)
    return ', '.join(strings)

def destextualizar(string):
    tuplas = []
    for par in string.split(', '):
        tuplas.append(tuple(map(int, par.split('-'))))
    return tuplas










