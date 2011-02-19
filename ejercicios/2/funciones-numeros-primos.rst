Funciones de números primos
===========================
En los ejercicios para la materia del primer certamen,
usted debió `desarrollar programas sobre números primos
<../1/numeros-primos.html>`_.

Muchos de estos programas sólo tenían pequeñas diferencias entre ellos,
por lo que había que repetir mucho código al escribirlos.
En este ejercicio,
usted deberá implementar algunos de esos programas como funciones,
reutilizando componentes para evitar escribir código repetido.

#. Escriba una función ``es_primo(n)``
   que determine si un número es primo o no::

       >>> es_primo(17)
       True
       >>> es_primo(221)
       False

#. Usando la función ``es_primo``,
   escriba la función ``i_esimo_primo(i)``
   que entregue el `i`-ésimo número primo.

       >>> i_esimo_primo(1)
       2
       >>> i_esimo_primo(20)
       71

#. Usando las funciones anteriores,
   escriba la función ``primeros_primos(m)``
   que entregue una lista
   de los primeros `m` números primos::

       >>> primeros_primos(10)
       [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#. Usando las funciones anteriores,
   escriba la función ``primos_hasta(m)``
   que entregue una lista
   de los primos menores o iguales que `m`::

       >>> primos_hasta(19)
       [2, 3, 5, 7, 11, 13, 17, 19]

