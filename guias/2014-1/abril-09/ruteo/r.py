s = 0; print 's:', s
c = 0; print 'c:', c
for i in range(2, 5):
    print 'i:', i
    for j in range(i):
        print 'j:', j
        s = s + i * j; print 's:', s
    c = c + 1; print 'c:', c
print s, c


