Multiplicación rusa
-------------------

El método de `multiplicación rusa`_
consiste en multiplicar sucesivamente
por 2 el multiplicando y dividir por 2 el multiplicador hasta
que el multiplicador tome el valor 1. Luego, se suman todos los
multiplicandos correspondientes a los multiplicadores impares.

.. _multiplicación rusa: http://mathworld.wolfram.com/RussianMultiplication.html

Dicha suma es el producto de los dos números.
La siguiente tabla muestra el cálculo realizado para multiplicar
37 por 12, cuyo resultado final es 12 + 48 + 384 = 444.

============= ============= =================== ====
Multiplicador Multiplicando Multiplicador impar Suma
============= ============= =================== ====
37             12            sí                  12
18             24            no
9              48            sí                  60
4              96            no
2              192           no
1              384           sí                  444
============= ============= =================== ====

Desarrolle un programa que reciba como entrada
el multiplicador y el multiplicando,
y entrege como resultado el producto de ambos,
calculado mediante el método de multiplicación rusa.

.. testcase::

   Ingrese multiplicador: `37`
   Ingrese multiplicando: `12`
   Resultado: 444
