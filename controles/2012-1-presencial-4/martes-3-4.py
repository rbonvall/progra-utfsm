'''
# CASO 1
>>> resultados_encuesta(respuestas)
{'A': 13, 'C': 8, 'B': 9}

# FIN CASO 1

# CASO 2
>>> porcentaje_respuesta_ciudad(respuestas, 'B', 'La Serena')
20.0

# FIN CASO 2

'''

# EJEMPLO RESPUESTAS
respuestas = { 'Santiago':  'ABBCAABBCAC',
               'Rancagua':  'CABBCAABA',
               'La Serena': 'ACCAABACAB'  }
# FIN EJEMPLO RESPUESTAS


def resultados_encuesta(respuestas):
    c = {'A': 0, 'B': 0, 'C': 0}
    for ciudad in respuestas:
        for r in respuestas[ciudad]:
            c[r] += 1
    return c

def porcentaje_respuesta_ciudad(respuestas, r, c):
    total = 0
    for respuesta in respuestas[c]:
        if respuesta == r:
            total += 1
    return 100.0 * total / len(respuestas[c])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

