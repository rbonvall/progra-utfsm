def tiene_siameses(n):
    anterior = n % 10
    n /= 10
    while n > 0:
        ultimo = n % 10
        if anterior == ultimo:
            return True
        n /= 10
        anterior = ultimo
    return False

def cuenta_siameses(m):
    c = 0
    for i in range(m):
        if tiene_siameses(i):
            c += 1
    return c

