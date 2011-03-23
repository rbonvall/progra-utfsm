mayor = -float('inf')
while True:
    n = float(raw_input())
    if n == 0:
        break
    mayor = max(mayor, n)

print 'El mayor es', mayor
