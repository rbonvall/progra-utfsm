from numpy import arange, exp, sum

# extremos del intervalo
a = 0.0
b = 4.9

# cantidad de rectangulos
n = 9

# largo de la base
base = (b - a) / n

# Dos maneras de obtener el arreglo
# con las coordenadas x
# de los lados izquierdos.
x = arange(a, b, base)
x = a + base * arange(n)

# (la segunda manera es mas segura
# desde el punto de vista numerico,
# ya que por errores de redondeo
# la primera forma podria incluir
# un valor de mas o de menos).


alturas = exp(x)
areas = alturas * base
area_total = sum(areas)

print area_total
