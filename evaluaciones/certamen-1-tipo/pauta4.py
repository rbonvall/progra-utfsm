x = 300.0
y = 400.0
a, b, c, d = 0.03, 0.00004, 0.05, 0.000006

dias = 0
while y >= 1:
    dx =  x * (a - b * y)
    dy = -y * (c - d * x)
    x = x + dx
    y = y + dy
    #print '%d\t%.2f\t%.2f' % (dias, x, y)
    dias += 1

print 'Los conejos se extinguiran en', dias, 'dias'
