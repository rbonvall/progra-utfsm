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

#. Escriba la función ``es_divisible(n, d)``
   que indique si ``n`` es divisible por ``d``::

       >>> es_divisible(15, 5)
       True
       >>> es_divisible(15, 6)
       False

#. Usando la función ``es_divisible``,
   escriba una función ``es_primo(n)``
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

#. Cree un módulo llamado ``primos.py``
   que contenga todas las funciones anteriores.

   Al ejecutar ``primos.py`` como un programa por sí solo,
   debe mostrar, a modo de prueba,
   los veinte primeros números primos.
   Al importarlo como un módulo,
   esto no debe ocurrir.

#. Un `primo de Mersenne`_ es un número primo de la forma `2^p - 1`.
   Una propiedad conocida de los primos de Mersenne es que
   `p` debe ser también un número primo.

   .. _primo de Mersenne: http://es.wikipedia.org/wiki/N%C3%BAmero_primo_de_Mersenne

   Escriba un programa llamado ``mersenne.py``
   que pregunte al usuario un número `n`,
   y muestre como salida
   los primeros `n` primos de Mersenne:

   .. testcase::

       Cuantos primos de Mersenne: `5`
       3
       7
       31
       127
       8191

   Su programa debe importar el módulo ``primos``
   y usar las funciones que éste contiene.

