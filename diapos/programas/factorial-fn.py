def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod = prod * i
    return prod

n = int(raw_input())
f = factorial(n)
print f
