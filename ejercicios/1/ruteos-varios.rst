Ruteos varios
=============
Solácese ruteando los siguientes programas.

::

    j = 2
    c = 1
    p = True
    while j > 0:
        j = j - c
        if p:
            c = c + 1
        p = not p
    print j < 0 and p

::

    a = 10
    c = 1
    x = 0
    y = x + 1
    z = y

    while z <= y:
        z = z + c
        y = 2 * x + z
        if y < 4:
            y = y + 1
        x = x - 1

    print x, y, z

::

    a = 11
    b = a / 3
    c = a / 2
    n = 0

    while a == b + c:
        n += 1
        b += c
        c = b - c
        if n % 2 == 0:
            a = 2 * a - 3
        print 100 * b + c

::

    a = True
    b = '1'
    c = 2
    while b[-1] not in '378':
        a = 0 == len(b) % 2
        if a:
            c = c * 7
        b = b + str(c)
    print c

