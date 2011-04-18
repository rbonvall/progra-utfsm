def son_amigos(m, n):
    sm = 0
    for i in range(1, m):
        if m % i == 0:
            sm = sm + i
    sn = 0
    for i in range(1, n):
        if n % i == 0:
            sn = sn + i
    return sn == m and sm == n
