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
