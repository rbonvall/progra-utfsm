j = 2
c = 1
p = True
while j > 0:
    j = j - c
    if p:
        c = c + 1
    p = not p
print j < 0 and p
