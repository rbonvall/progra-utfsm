e = int(raw_input('Edad de Edelmiro: '))
f = int(raw_input('Edad de Froilana: '))
p = int(raw_input('Edad de Prisciliano: '))

if e == f == p:
    print 'Los tres tienen la misma edad'
elif e == f:
    print 'Edelmiro y Froilana tienen la misma edad'
elif e == p:
    print 'Edelmiro y Prisciliano tienen la misma edad'
elif f == p:
    print 'Froilana y Prisciliano tienen la misma edad'
else:
    print 'Todos tienen edades distintas'
