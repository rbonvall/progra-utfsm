def tiene_digito(d, n):
    while n > 0:
        ultimo = n % 10
        if ultimo == d:
            return True
        n /= 10
    return False

def digitos_en_comun(m, n):
    while n > 0:
        ultimo = n % 10
        if tiene_digito(ultimo, m):
            return True
        n /= 10
    return False

