def abundante(m):
    s = 0
    for i in range(1, m):
        if m % i == 0:
            s = s + i
    return s > m
