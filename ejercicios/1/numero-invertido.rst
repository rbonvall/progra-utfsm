Número invertido
----------------

Realizar un programa que
permita determinar el número
invertido a partir de un número
*n* ingresado por el usuario,
de tres dígitos.


::

    Ingrese número: 345
    543

::

    Ingrese número: 123
    321


* Solución

::

    num = int(input("Ingrese número:"))
    centena = num//100
    decena = num%100//10
    unidad = num%10
    print (unidad*100+decena*10+centena)
