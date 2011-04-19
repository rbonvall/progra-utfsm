Intersección de circunferencias
-------------------------------

En el plano, una circunferencia está determinada
por su centro (*x*, *y*) y por su radio *r*.

En un programa,
podemos representarla como una tupla ``(centro, radio)``,
donde a su vez ``centro`` es una tupla ``(x, y)``::

    c = ((4.0, 5.1), 2.8)

1. Escriba la función ``distancia(p1, p2)``
   que entregue la distancia entre los puntos ``p1`` y ``p2``::

     >>> distancia((2, 2), (7, 14))
     13.0
     >>> distancia((2, 5), (1, 9))
     4.1231056256176606

2. Escriba la función ``se_intersectan(c1, c2)``
   que indique si las circunferencias ``c1`` y ``c2``
   se intersectan:

   .. image:: ../../diagramas/circunferencias.png

   ::

      >>> A = (( 5.0,  4.0), 3.0)
      >>> B = (( 8.0,  6.0), 2.0)
      >>> C = (( 8.4, 12.7), 3.0)
      >>> D = (( 8.0, 12.0), 2.0)
      >>> E = ((16.0,  7.8), 2.7)
      >>> F = ((15.5,  2.7), 2.1)
      >>> se_intersectan(A, B)
      True
      >>> se_intersectan(C, D)
      False
      >>> se_intersectan(E, F)
      False

