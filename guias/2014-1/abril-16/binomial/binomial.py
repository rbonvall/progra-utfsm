def factorial(n):
    producto = 1
    for i in range(1, n + 1):
        producto *= i
    return producto

def binomial(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


n = int(raw_input('n: '))
k = int(raw_input('k: '))
print '(n k) =', binomial(n, k)
