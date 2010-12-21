Número invertido
----------------

#. Determinar el número invertido de un número ingresado

 * **Entrada**

  Un número entero de tres dígitos.

 * **Salida**

  El número con los dígitos en orden inverso.

 * Comportamiento::

    Ingrese número: 345
    543
 * Solución::

    num = int(input("Ingrese número:"))
    centena = num//100
    decena = num%100//10
    unidad = num%10
    print (unidad*100+decena*10+centena)
