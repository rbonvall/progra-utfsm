def sumar_palitos(a, b):
    return (len(a) + len(b)) * 'i'

def es_primo(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def contar_primos_menores_que(m):
    c = 0
    for n in range(2, m):
        if es_primo(n):
            c += 1
    return c

def reflejar(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n /= 10
    return r

def es_palindromo(n):
    return reflejar(n) == n
