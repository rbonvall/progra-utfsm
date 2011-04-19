def cuenta_digito(d, n):
    c = 0
    while n > 0:
        ultimo = n % 10
        if ultimo == d:
            c += 1
        n /= 10
    return c

def siguiente_con_digitos(d, c, m):
    n = m + 1
    while cuenta_digito(d, n) < c:
         n += 1
    return n
