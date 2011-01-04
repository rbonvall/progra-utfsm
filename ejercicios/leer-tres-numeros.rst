Leer tres números
-----------------

Desarrollar un programa que permita
realizar un ciclo que lea 3 números
ingresados por el usuario.

 * **Entrada**

  Un número en cada iteración.

 * **Salida**

  El número ingresado en cada iteración.


 * Comportamiento::

    Ingrese un número: 3
    Ingresado el 3
    Ingrese un número: 2
    Ingresado el 2
    Ingrese un número: 0
    Ingresado el 0
    Fin del programa

 * Solución::

	i = 0
	while i < 3:
	   	num = input("Ingrese un número")
		print ("Ingresado el", num)
		i += 1
	print ("Fin del programa")

