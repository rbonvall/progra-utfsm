Determinar relación con 0
-------------------------

Determinar si un número es menor que 0, 0 o mayor que 0.

 * **Entrada**
  
  Un número cualquiera.

 * **Salida**

  Si el número es < 0, 0 o > 0.

 * Comportamiento::

    Ingrese un número: 3
    Su número es mayor que 0

    Ingrese un número: 0
    Su número es 0

    Ingrese un número: -4
    Su número es menor que 0

 * Solución::

    num = input("Ingrese un número:")
    if num < 0:
        print ("Su número es menor que 0")
    elif num > 0:
        print ("Su número es mayor que 0")
    else:
        print ("Su número es 0")

