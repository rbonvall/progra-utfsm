.. _patrones:

Patrones comunes
================

Como hemos visto hasta ahora,
los programas son una combinación de asignaciones,
condicionales y ciclos,
organizados de tal manera
que describan el algoritmo que queremos ejecutar.

Existen algunas tareas muy comunes
y que casi siempre se resuelven de la misma manera.
Por lo tanto, es conveniente conocerlas.

En programación,
se llama **patrón** a una solución
que puede ser aplicable a un problema que ocurre a menudo.
A continuación veremos algunos patrones comunes
que ocurren en programación.

Sumar y multiplicar cosas
-------------------------
La suma y la multiplicación son operaciones binarias:
operan sobre dos valores.

Para sumar y multiplicar más valores,
generalmente dentro de un ciclo que los genere,
hay que usar una variable
para ir guardando el resultado parcial de la operación.
Esta variable se llama **acumulador**.

En el caso de la suma,
el acumulador debe partir con el valor cero.
Para la multiplicación, con el valor uno.

Por ejemplo,
el siguiente programa entrega
el producto de los mil primeros números naturales::

    producto = 1
    for i in range(1, 1001):
        producto = producto * i

    print producto

El siguiente programa entrega
la suma de los cubos de los números naturales
cuyo cuadrado es menor que mil::

    i = 1
    suma = 0
    while i ** 2 < 1000:
        valor = i ** 3
        i = i + 1
        suma = suma + valor

    print suma

En todos los casos,
el patrón a seguir es algo como esto::

    acumulador = valor_inicial
    ciclo:
        valor = ...
        ...
        acumulador = acumulador operación valor

El cómo adaptar esta plantilla a cada situación
de modo que entregue el resultado correcto
es responsabilidad del programador.

Contar cosas
------------
Para contar cuántas veces ocurre algo,
hay que usar un acumulador,
al que se le suele llamar **contador**.

Tal como en el caso de la suma,
debe ser inicializado en cero,
y cada vez que aparezca lo que queremos contar,
hay que sumarle uno.

Por ejemplo,
el siguiente programa
cuenta cuántos de los números naturales
menores que mil tienen un cubo terminado en siete::

    c = 0
    for i in range(1000):
        ultimo_digito = i % 10
        if ultimo_digito = 7:
            c = c + 1

    print c

Encontrar el mínimo y el máximo
-------------------------------
Para encontrar el máximo de una secuencia de valores,
hay que usar un acumulador
para recordar cuál es el mayor valor visto hasta el momento.
En cada iteración,
hay que examinar cuál es el valor actual,
y si es mayor que el máximo,
actualizar el acumulador.

El acumulador debe ser inicializado
con un valor que sea menor
a todos los valores que vayan a ser examinados.

Por ejemplo,
el siguiente programa
pide al usuario que ingrese diez números enteros positivos,
e indica cuál es el mayor de ellos::

    print 'Ingrese diez numeros positivos'

    mayor = -1
    for i in range(10):
        n = int(raw_input())
        if n > mayor:
            mayor = n

    print 'El mayor es', mayor

Otra manera de hacerlo es reemplazando esta parte::

    if n > mayor:
        mayor = n

por ésta::

    mayor = max(mayor, n)

En este caso,
como todos los números ingresados son positivos,
inicializamos el acumulador en ``-1``,
que es menor que todos los valores posibles,
por lo que el que sea el mayor
eventualmente lo reemplazará.

¿Qué hacer cuando no exista un valor inicial
que sea menor a todas las entradas posibles?
Una solución es poner un número «muy negativo»,
y rezar para que el usuario no ingrese uno menor que él.
Esta no es la mejor solución,
ya que no cubre todos los casos posibles::

    mayor = -999999999
    for i in range(10):
        n = int(raw_input())
        mayor = max(mayor, n)

Una opción más robusta
es usar el primero de los valores por examinar::

    mayor = int(raw_input())   # preguntar el primer valor
    for i in range(9):         # preguntar los nueve siguientes
        n = int(raw_input())
        mayor = max(mayor, n)

La otra buena solución es usar explícitamente el valor `-\infty`,
que en Python puede representarse usando el tipo ``float``
de la siguiente manera::

    mayor = -float('inf')     # asi se dice "infinito" en Python
    for i in range(10):
        n = int(raw_input())
        mayor = max(mayor, n)

Por supuesto, para obtener el menor valor
se hace de la misma manera,
pero inicializando el acumulador con un número muy grande,
y actualizándolo al encontrar un valor menor.

[Por escribir el resto]

