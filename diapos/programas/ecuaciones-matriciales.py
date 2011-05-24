# CALCULAR NUTRIENTES
from numpy import *

a = array([[ 36. ,  51. ,  13. ],
           [ 52. ,  34. ,  74. ],
           [  0. ,   7. ,   1.1]])

x = array([ 0.1,  0.5,  0.3])

b = dot(a, x)

print b
# FIN CALCULAR NUTRIENTES

# CALCULAR ALIMENTOS
from numpy import *
from numpy.linalg import solve

a = array([[ 36. ,  51. ,  13. ],
           [ 52. ,  34. ,  74. ],
           [  0. ,   7. ,   1.1]])

b = array([33, 45, 3])

x = solve(a, b)

print x
# FIN CALCULAR ALIMENTOS
