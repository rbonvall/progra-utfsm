Números amistosos
-----------------

Un par de números *m* y *n* son llamados **amistosos**
(o se conocen como un **par amigable**), si la suma de
todos los divisores de *m* (excluyendo a *m*) es igual al
número *n*, y la suma de todos los divisores del número *n*
(excluyendo a *n*) es igual a *m* (con *m* ≠ *n*).

Por ejemplo, los números 220 y 284 son un par amigable
porque los únicos números que dividen de forma exacta
220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, y

   1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284

Por lo tanto, 220 es un número amistoso. Los únicos números
que dividen exactamente 284 son 1, 2, 4, 71 y 142 y

   1 + 2 + 4 + 71 + 142 = 220

Por lo tanto, 284 es un número amistoso.

Muchos pares de números amigables son conocidos;
sin embargo, sólo uno de los pares (220, 284)
tiene valores menores que 1000.
El siguiente par está en el rango [1000, 1500].

Desarrolle un programa que permita encontrar dicho par.
