racha = 0
ultimo = 0
while True:

    n = int(raw_input())

    if n == 1:
        print 'Usted perdio'
        break
    elif n == ultimo:
        racha += 1
    else:
        racha = 1
        ultimo = n

    if racha == n:
        print 'Usted gano'
        break

