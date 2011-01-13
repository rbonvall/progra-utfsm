Adivinar el número
------------------

Realice un programa que permita generar
un número aleatorio *n* entre 0 y 100,
para poder jugar a adivinar dicho número,
ingresando números por entrada estándar.

El programa debe darle *pistas* del número
a adivinar, diciendo si el que usted va ingresando
es mayor o menor que *n*.

Una vez encontrado el número,
el programa debe decir cuantos intentos
utilizaste para poder adivinar el número *n*.

Para generar un número aleatorio puede utilizar
el siguiente código

::

   import random
   # guardamos el número aleatorio en n
   n = random.randint(0,100)

* Comportamiento

::

   Generando número aletorio...
   Ingrese un número: 45
   mayor
   Ingrese un número: 68
   mayor
   Ingrese un número: 73
   menor
   Ingrese un número: 70
   Adivinaste!
   Lo intentaste 4 veces
