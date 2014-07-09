def llaves(d):
    l = []
    for k in d:
        l.append(k)
    return l

def valores(d):
    v = []
    for k in d:
        v.append(d[k])
    return v

def invertir(d):
    di = {}
    for k in d:
        di[d[k]] = k
    return di

def unir(da, db):
    d = {}
    for k in da:
        d[k] = da[k]
    for k in db:
        d[k] = db[k]
    return d

def contar_letras(palabra):
    d = {}
    for letra in palabra:
        if letra not in d:
            d[letra] = 0
        d[letra] += 1
    return d

