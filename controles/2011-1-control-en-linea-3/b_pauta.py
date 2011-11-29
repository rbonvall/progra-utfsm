def suma_digitos(n):
    s = 0
    while n > 0:
        ultimo = n % 10
        s += ultimo
        n /= 10
    return s

def reducir_a_digito(n):
    s = suma_digitos(n)
    while s >= 10:
        s = suma_digitos(s)
    return s
