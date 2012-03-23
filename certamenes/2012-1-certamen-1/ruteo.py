m = 5
n = 1
y = ''
for i in range(5):
    m -= 1
    if i % 4 != 0:
        x = 'o' * m
        y += 'o'
        print x + 'x' + y

