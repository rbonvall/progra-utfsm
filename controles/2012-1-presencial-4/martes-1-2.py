'''
# CASO 1
>>> calcular_promedios(notas)
{'Jaimita': 5.3, 'Pepito': 3.6, 'Fulanita': 3.4}

# FIN CASO 1

# CASO 2
>>> clasificar_ninos(notas)
{'Reprobados': 2, 'Aprobados': 1}

# FIN CASO 2

'''

def calcular_promedios(notas):
    promedios = {}
    for nino in notas:
        n = notas[nino]
        p = sum(n) / len(n)
        promedios[nino] = round(p, 1)
    return promedios

def clasificar_ninos(notas):
    c = {'Aprobados': 0, 'Reprobados': 0}
    p = calcular_promedios(notas)
    for nino in p:
        if p[nino] >= 4.0:
            c['Aprobados'] += 1
        else:
            c['Reprobados'] += 1
    return c


# EJEMPLO NOTAS
notas = {
  'Pepito':   [4.1, 3.7, 2.9],
  'Jaimita':  [6.1, 4.3, 5.6],
  'Fulanita': [3.1, 4.5, 2.7],
}
# FIN EJEMPLO NOTAS


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

