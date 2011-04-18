def es_oblongo(n):
    for i in range(n):
        if i * (i + 1) == n:
            return True
    return False
