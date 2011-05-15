# solucion 1
def diferencias(a):
    n = a.size
    b = a[1:n]
    c = a[0:n - 1]
    return b - c


# solucion 2
def diferencias(a):
    b = a[1:]
    c = a[:-1]
    return b - c

