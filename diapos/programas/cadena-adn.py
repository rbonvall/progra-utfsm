cadena      = 'cagcccatgaggcagggtg'
complemento = 'gtcgggtactccgtcccac'

from random import choice

def cadena_al_azar(n):
    bases = []
    for i in range(n):
        b = choice('actg')
        bases.append(b)
    cadena = ''.join(bases)
    return cadena

# version incorrecta 1
# (quedan solo a y c)
def complementaria_MALA(cadena):
    c = cadena
    c = c.replace('a', 't')
    c = c.replace('t', 'a')
    c = c.replace('c', 'g')
    c = c.replace('g', 'c')
    return c

# version incorrecta 2
# (el string no se modifica)
def complementaria_MALA(cadena):
    cadena.replace('a', 'x')
    cadena.replace('t', 'a')
    cadena.replace('x', 't')

    cadena.replace('c', 'x')
    cadena.replace('g', 'c')
    cadena.replace('x', 'g')
    return cadena

# version 1
def complementaria(cadena):
    c = cadena

    c = c.replace('a', 'x')
    c = c.replace('t', 'a')
    c = c.replace('x', 't')

    c = c.replace('c', 'x')
    c = c.replace('g', 'c')
    c = c.replace('x', 'g')
    return c

# version 2 (lo mismo, pero mas breve)
def complementaria(cadena):
    return (cadena.replace('a', 'x')
                  .replace('t', 'a')
                  .replace('x', 't')
                  .replace('c', 'x')
                  .replace('g', 'c')
                  .replace('x', 'g'))

# version 3 (construir la nueva cadena base por base)
def complementaria(cadena):
    bases_comp = []
    for base in cadena:
        if base == 'a':
            bases_comp.append('t')
        elif base == 't':
            bases_comp.append('a')
        elif base == 'c':
            bases_comp.append('g')
        elif base == 'g':
            bases_comp.append('c')
    return ''.join(bases_comp)

# version 4 (lo mismo, pero usando un diccionario)
def complementaria(cadena):
    bases_comp = []
    correspondiente = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    for base in cadena:
        b = correspondiente[base]
        bases_comp.append(b)
    return ''.join(bases_comp)

