def contar_palabras(oracion):
    oracion = oracion.lower().replace('.', '').replace(',', '')
    palabras = oracion.split()
    cuenta = {}
    for palabra in palabras:
        if palabra not in cuenta:
            cuenta[palabra] = 0
        cuenta[palabra] = cuenta[palabra] + 1
    return cuenta
