Números primos
==============

.. highlight:: c

El siguiente programa
muestra la cantidad de números primos
indicada por el usuario:

.. literalinclude:: programas/primos.c

En este programa,
vemos que es posible declarar varias variables del mismo tipo
en una única sentencia
(``primos_por_mostrar``, ``n`` y ``d``).

También aprovechamos de presentar
cómo se hacen los comentarios en C:
comienzan con ``/*`` y terminan con ``*/``.

Escriba, compile y ejecute este programa.

Sentencias de control: while, for e if
--------------------------------------

Este programa muestra tres de las sentencias de control de C,
que son equivalentes a sus tocayos de Python:
``while``, ``for`` e ``if``.

El ``while`` y el ``if`` son sencillos.
Hay que tener en cuenta que la condición
debe ir necesariamente entre paréntesis.
El contenido no se indica usando indentación,
sino que encerrándolo entre paréntesis de llave::

    while (condicion) {
        /* ... */
    }

    if (condicion) {
        /* ... */
    }

Al igual que en Python,
el ``if`` puede ir seguido de un ``else``.
El ``elif`` de Python no existe en C,
pero puede escribirse como ``else if``.

El ciclo ``for`` es un poco diferente.
Entre los paréntesis tiene tres partes
separadas por punto y coma::

    for (inicializacion; condicion; actualizacion) {
        /* ... */
    }

La inicialización se ejecuta una vez,
antes de iniciar el ciclo.
Aquí se suele asignar un valor inicial a un contador.

La actualización es la parte
donde se modifica el valor del contador
al final de cada iteración.

La condición es evaluada después de cada actualización,
para decidir si se continúa o no ejecutando el ciclo.

Algunos ejemplos de ciclos ``for`` en C,
junto con sus equivalentes en Python::

    for (i = 0; i < N; ++i)       /* for i in range(N):         */
    for (i = 5; i < 10; ++i)      /* for i in range(5, 10):     */
    for (i = 2; i < 30; i += 2)   /* for i in range(2, 30, 2):  */
    for (i = 40; i > 0; --i)      /* for i in range(40, 0, -1): */
    for (i = 1; i <= N; ++i)      /* for i in range(1, N + 1):  */

Las sentencias ``break`` y ``continue`` de Python
también funcionan en C.

Operadores de incremento y decremento
-------------------------------------
La expresión ``n++``
incrementa en uno el valor de ``n``.
Es decir, si ``n`` tiene el valor 15,
después de hacer ``n++`` tendrá el valor 16.

De manera similar,
``primos_por_mostrar--``
reduce en uno el valor de ``primos_por_mostrar``.
Inicialmente esta variable tiene el valor
ingresado por el usuario,
y luego va decreciendo hasta llegar a cero.
Cuando esto ocurre, el ciclo ``while`` se termina.

Ambos operadores pueden ir antes o después de la variable::

    n++;
    ++n;

Ambas modifican el valor de ``n`` de la misma manera.
Más adelante veremos cuál es la diferencia
entre estas dos formas.

Valores lógicos
---------------
En C no existe un tipo de datos
para representar valores lógicos,
como el tipo ``bool`` de Python.
En C, **los valores lógicos son enteros**.
El valor cero es interpretado como falso,
y cualquier otro valor como verdadero.

Como ilustración,
nuestro programa usa la variable ``es_primo``
para recordar si el número ``n``
que se está analizando en cada iteración
es o no primo.
Esta variable es entera,
y su valor es cambiado a cero
apenas se encuentra un divisor.

Como los enteros pueden ser interpretados como valores lógicos,
el ciclo ``while`` de nuestro programa
también podría haber sido escrito así::

    while (primos_por_mostrar) {
        /* ... */
    }

ya que esto también haría que el ciclo terminara
cuando la variable llega a cero,
porque en este caso sería interpretado
como una condición falsa.
Haga la prueba,
y convénzase de que funciona.

Los operadores lógicos en C son:

* ``&&`` (y),
* ``||`` (o),
* ``!`` (negación).

Por ejemplo,
si uno quisiera modificar el programa
para que mostrara sólo los números compuestos
que terminan en 7,
habría que cambiar la condición del último ``if``
por la siguiente::

    if (!es_primo && n % 10 == 7) {
        /* ... */
    }

Los operadores ``==``, ``!=``, ``<``, ``>``, ``<=`` y ``>=``
funcionan de la misma manera que en Python.

Uno de los errores más comunes en C
es confundir el operador de igualdad ``==``
con la asignación ``=``.
En C es legal poner una asignación
dentro de la condición de un ``if`` o de un ``while``,
por lo que un programa como éste::

    if (x = 2) {
        /* ... */
    }

compilará y se ejecutará sin errores,
pero probablemente no hará lo que nosotros esperamos:
en vez de verificar que ``x`` vale 2,
¡modificará ``x`` para que lo valga!

Ejercicios
----------
Modifique el programa de arriba para que,
en vez de mostrar una cierta cantidad de números primos,
muestre todos los números primos menores que *m*.

A continuación,
modifíquelo para que
en lugar de mostrar sólo los números primos
los muestre todos,
indicando para cada uno de ellos
si es primo o compuesto:

.. testcase::

    2 primo
    3 primo
    4 compuesto
    5 primo
    6 compuesto
    ...

