Determinar pares
----------------

Realizar un programa que determine
los números *pares* entre 0 y 10.

* Comportamiento

::

    Los números son:
    0
    2
    4
    6
    8

* Solución

::

    print ("Los números son:"),
    for num in range(0,10):
        if num%2 == 0:
            print (num) 
