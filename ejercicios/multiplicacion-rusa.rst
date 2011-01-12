Multiplicación Rusa
-------------------

La multiplicación rusa consiste en multiplicar sucesivamente
por *2* el multiplicando y dividir por *2* el multiplicador hasta
que el multiplicador tome el valor *1*. Luego, se suman todos los
multiplicando correspondientes a los multiplicadores impares.

Dicha suma es el resultado del producto de los dos números.
La siguiente tabla muestra el cálculo realizado para multiplicar
*37* por *12*, cuyo resultado final es *12 + 48 + 384 = 444*.

+--------------+-------------+-------------------+----+
| Multiplicador|Multiplicando|Multiplicador impar|Suma|
+==============+=============+===================+====+
| 37           | 12          | si                | 12 |                
+--------------+-------------+-------------------+----+
| 18           | 24          | no                |    |
+--------------+-------------+-------------------+----+
| 9            | 48          | si                | 60 |
+--------------+-------------+-------------------+----+
| 4            | 96          | no                |    |
+--------------+-------------+-------------------+----+
| 2            | 192         | no                |    |  
+--------------+-------------+-------------------+----+
| 1            | 384         | si                | 444|
+--------------+-------------+-------------------+----+

Desarrolle un programa que permita realizar la multiplicación rusa
de dos números. Considere que ambos elementos, el multiplicador y
el multiplicando, son ingresados por el usuario.

* Comportamiento

::

   Ingrese multiplicador: 37
   Ingrese multiplicando: 12
   Resultado: 444
