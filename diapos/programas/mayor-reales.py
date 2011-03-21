mayor = -float('inf')
while True:
    n = int(raw_input())
    if n == 0:
        break
    mayor = max(mayor, n)
