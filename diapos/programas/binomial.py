def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod = prod * i
    return prod

def coef_binomial(n, k):
    fn = factorial(n)
    fk = factorial(k)
    fnk = factorial(n - k)
    return fn / (fnk * fk)

n = int(raw_input('n: '))
k = int(raw_input('k: '))
print '(n k) =', coef_binomial(n, k)
