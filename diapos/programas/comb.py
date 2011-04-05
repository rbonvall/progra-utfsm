def factorial(n):
    p = 1
    for i in range(1, n + 1):
        p = p * i
    return p

def coef_bin(n, k):
    fn = factorial(n)
    fk = factorial(k)
    fnk = factorial(n - k)
    return fn / (fk * fnk)

if __name__ == '__main__':
    n = int(raw_input('n: '))
    k = int(raw_input('k: '))
    print '(n k) =', coef_bin(n, k)

