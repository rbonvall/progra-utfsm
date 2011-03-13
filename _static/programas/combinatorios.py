def factorial(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p


def comb(m, n):
    return factorial(m) / (factorial(n) * factorial(m - n))


m = int(raw_input('Ingrese m: '))
n = int(raw_input('Ingrese n: '))
c = comb(m, n)
print '(m n) =', c

