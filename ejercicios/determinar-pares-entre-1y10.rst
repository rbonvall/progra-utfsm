Determinar pares
----------------

#. Determinar los números pares entre 0 y 10

 * **Entrada**

  Nada

 * **Salida**

  Los números pares entre 0 y 10.

 * Comportamiento::

    Los números son:
    0
    2
    4
    6
    8

 * Solución::

    print ("Los números son:"),
    for num in range(0,10):
        if num%2 == 0:
            print (num) 
