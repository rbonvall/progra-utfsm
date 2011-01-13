Determinar par
--------------

Realizar un programa que permita determinar
si un número *n* cualquiera,
ingresado por el usuario es par o no.

* Comportamiento

::

    Ingrese un número: 4
    Su número es par

::

    Ingrese un número: 3
    Su número es impar


* Solución

::

    num = input("Ingrese un número")
    if num%2 == 0:
        print ("Su número es par)
    else:
        print ("Su número es impar)
