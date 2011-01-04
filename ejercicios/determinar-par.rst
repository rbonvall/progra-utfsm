Determinar par
--------------

Realizar un programa que permita determinar
si un número ingresado es par o no.

* **Entrada**

  Un número cualquiera

* **Salida**

  Si el número es par o impar.

* Comportamiento::

    Ingrese un número: 4
    Su número es par

    Ingrese un número: 3
    Su número es impar


* Solución::

    num = input("Ingrese un número")
    if num%2 == 0:
        print ("Su número es par)
    else:
        print ("Su número es impar)
