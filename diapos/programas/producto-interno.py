# DOT
>>> a
array([-2.8 , -0.88,  2.76,  1.3 ,  4.43])
>>> b
array([ 0.25, -1.58,  1.32, -0.34, -4.22])

>>> dot(a, b)
-14.803

>>> sum(a * b)
-14.803
# FIN DOT

# EJERCICIO 1
>>> a = array([6, 1, 4])
>>> b = array([2, 7, 2])
>>> dot(a, b)
?

>>> c = array([2, 3, 4, 5])
>>> d = array([0, 1, 0, 1])
>>> dot(c, d)
?
# FIN EJERCICIO 1

# EJEMPLOS PRODUCTO INTERNO
precios = array([678, 2500, 12400, 2310])
unidades = array([2, 0, 0, 1])
total = dot(precios, unidades)

ponderaciones = array([20, 25, 25, 30]) * .01
notas = array([55, 48, 39, 71])
promedio = dot(ponderaciones, notas)

x = linspace(0, 5, 101)
alturas = exp(x[:100])
bases = (5.0 / 100) * ones(100)
area = dot(alturas, bases)
# FIN EJEMPLOS PRODUCTO INTERNO

# MATRIZ VECTOR
>>> a
array([[-0.6,  4.8, -1.2],
       [-2.0, -3.6, -2.1],
       [ 1.7,  4.9,  0.0]])

>>> x
array([-0.6, -2.0,  1.7])

>>> dot(a, x)
array([-11.28,   4.83, -10.82])
# FIN MATRIZ VECTOR

# EJERCICIO 2
>>> a = array([[0, 1],
...            [1, 0]])
>>> x = array([31, 49])
>>> dot(a, x)
?

>>> a = array([[1, 2],
...            [1, 0]])
>>> x = array([2, 3])
>>> dot(a, x)
?
# FIN EJERCICIO 2

# MATRIZ MATRIZ
>>> a = array([[ 2,  8],
               [-3,  7],
               [-8, -5]])

>>> b = array([[-3, -5, -6, -3],
               [-9, -2,  3, -3]])

>>> dot(a, b)
array([[-78, -26,  12, -30],
       [-54,   1,  39, -12],
       [ 69,  50,  33,  39]])

# FIN MATRIZ MATRIZ
