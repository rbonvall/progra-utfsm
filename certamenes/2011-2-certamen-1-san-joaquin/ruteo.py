i = 100
j = 2
g = ''
while i > j:
    i /= 2
    j *= 3
    if j % 2 == 0:
        j += 1
    g += '*'
print g
