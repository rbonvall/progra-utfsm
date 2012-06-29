from numpy import array, ones

print '=== P1 ==='
# P1

# FIN P1

print '=== P2 ==='
# P2

# FIN P2

print '=== P3 ==='
# P3

# FIN P3

print '=== P4 ==='
# P4

# FIN P4

print '=== P5 ==='
# P5

# FIN P5

print '=== P6 ==='
# P6

# FIN P6


# PA
am = open('misterio.txt')
ae = open('enigma.txt', 'w')
for x in am:
    xs = x.split()
    ae.write(xs[0] + xs[1])
    ae.write('\n')
am.close()
ae.close()

# FIN PA

print '=== Archivo enigma.txt ==='
print open('enigma.txt').rstrip().read()

