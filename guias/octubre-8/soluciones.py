def contar(valores):
    d = {}
    for x in valores:
        if x not in d:
            d[x] = 0
        d[x] += 1
    return d

