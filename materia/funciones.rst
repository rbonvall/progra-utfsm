Funciones
=========
Supongamos que necesitamos escribir un programa
que calcule el `número combinatorio`_ `C(m, n)`,
definido como:

.. math::

    C(m, n) = \frac{m!}{(m - n)! n!},

donde `n!` (el factorial_ de `n`)
es el producto de los números enteros desde 1 hasta `n`:

.. math::

    n! = 1\cdot 2\cdot\cdots\cdot(n - 1)\cdot n = \prod_{i=1}^n i

.. _número combinatorio: http://es.wikipedia.org/wiki/Número_combinatorio
.. _factorial: http://es.wikipedia.org/wiki/Factorial

El código para calcular el factorial de un número entero `n`
es sencillo::

    f = 1
    for i in range(1, n + 1):
        f *= i

Sin embargo,
para calcular el número combinatorio,
hay que hacer lo mismo tres veces::

    comb = 1

    # multiplicar por m!
    f = 1
    for i in range(1, m + 1):
        f = f * i
    comb = comb * f

    # dividir por (m - n)!
    f = 1
    for i in range(1, m - n + 1):
        f = f * i
    comb = comb / f

    # dividir por n!
    f = 1
    for i in range(1, n + 1):
        f = f * i
    comb = comb / f

La única diferencia entre los tres cálculos de factoriales
es el valor de término de cada ciclo ``for``
(``m``, ``m - n`` y ``n``, respectivamente).

Escribir el mismo código varias veces es tedioso y propenso a errores.
Además, el código resultante es mucho más dificil de entender,
pues no es evidente a simple vista qué es lo que hace.

Lo ideal sería que existiera una función llamada ``factorial``
que hiciera el trabajo sucio, y que podamos usar de la siguiente manera::

    factorial(m) / (factorial(m - n) * factorial(n))

Ya vimos anteriormente que Python ofrece «de fábrica»
algunas funciones, como ``int``, ``min`` y ``abs``.
Ahora veremos cómo crear nuestras propias funciones.

Funciones
---------
.. index:: función

En programación,
una **función** es una sección de un programa
que calcula un valor
de manera independiente al resto del programa.

.. index:: parámetro (de una función), resultado (de una función), valor de retorno

Una función tiene tres componentes importantes:

* los **parámetros**,
  que son los valores que recibe la función como entrada;
* el **código de la función**,
  que son las operaciones que hace la función; y
* el **resultado** (o **valor de retorno**),
  que es el valor final que entrega la función.

En escencia, una función es un mini programa.
Sus tres componentes son análogos a
la entrada, el proceso y la salida de un programa.

En el ejemplo del factorial,
el parámetro es el entero al que queremos calcularle el factorial,
el código es el ciclo que hace las multiplicaciones,
y el resultado es el valor calculado.

Definición de funciones
~~~~~~~~~~~~~~~~~~~~~~~
Las funciones en Python son creadas mediante la sentencia ``def``::

    def nombre(parámetros):
        # código de la función

Los parámetros son variables
en las que quedan almacenados los valores de entrada.

La función contiene código igual al de cualquier programa.
La diferencia es que, al terminar,
debe entregar su resultado
usando la sentencia ``return``.

Por ejemplo,
la función para calcular el factorial
puede ser definida de la siguiente manera::

    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

En este ejemplo,
el resultado que entrega una llamada a la función
es el valor que tiene la variable ``f``
al llegar a la última línea de la función.

Una vez creada,
la función puede ser usada como cualquier otra,
todas las veces que sea necesario::

    >>> factorial(0)
    1
    >>> factorial(12) + factorial(10)
    482630400
    >>> factorial(factorial(3))
    720
    >>> n = 3
    >>> factorial(n ** 2)
    362880

Las variables que son creadas dentro de la función
(incluyendo los parámetros y el resultado)
se llaman **variables locales**,
y sólo son visibles dentro de la función,
no desde el resto del programa.

En el ejemplo, las variables locales son ``n``, ``f`` e ``i``.
Una vez que la llamada a la función termina,
estas variables dejan de existir::

    >>> factorial(5)
    120
    >>> f
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    NameError: name 'f' is not defined


.. El programa completo para calcular el número combinatorio `C(m, n)`
.. sería el siguiente:
.. 
.. .. literalinclude:: programas/comb-con-funcion.f95
.. 
.. En este programa,
.. han sido definidas dos funciones:
.. 
.. * ``factorial`` recibe como parámetro un entero ``p``
..   y entrega como resultado un entero ``f``.
..   Además , tiene una tercera variable local ``i``.
.. * ``comb`` recibe como parámetros dos enteros, ``m`` y ``n``,
..   y entrega como resultado un entero ``c``.
.. 
.. Note que, gracias al uso de las funciones,
.. el código del programa ahora tiene sólo tres líneas.
.. 
.. 
.. Llamadas a funciones
.. ~~~~~~~~~~~~~~~~~~~~
.. .. index:: llamada a función
.. 
.. La operación de usar una función para obtener un valor
.. se denomina **llamar a la función**.
.. Se representa pasando los parámetros entre paréntesis
.. a continuación del nombre de la función::
.. 
..     comb(5, 2)
.. 
.. Ya que la llamada entrega un valor como resultado,
.. puede ser usada en cualquier parte de un programa
.. en la que pueda ir una expresión::
.. 
..     print *, factorial(5)
..     x = factorial(10)
..     y = 2 * factorial(3)
..     z = factorial(2 * x) + factorial(factorial(4))
.. 
.. Todas las siguientes llamadas tienen errores
.. o están usadas en el contexto equivocado::
.. 
..     read *, factorial(x)    ! read requiere variable, no expresión
..     x = factorial(2, 3)     ! factorial tiene un parámetro, no dos
..     x = factorial('perro')  ! el parámetro debe ser entero, no string
..     x = trim(factorial(5))  ! el resultado es entero, no string
..     factorial(x)            ! llamadas no son sentencias
.. 
.. Subrutinas
.. ----------
.. .. index:: subrutina
.. 
.. Una **subrutina** es una sección de un programa
.. que realiza varias sentencias
.. de manera independiente al resto del programa.
.. La diferencia con las funciones
.. es que las subrutinas no entregan ningún valor como resultado.
.. 
.. Las subrutinas son útiles
.. para agrupar secuencias de sentencias
.. que deben ser ejecutadas en conjunto.
.. Usar subrutinas suele hacer
.. que los programas sean más fáciles de leer.
.. 
.. Definición de subrutinas
.. ~~~~~~~~~~~~~~~~~~~~~~~~
.. Al igual que las funciones,
.. las subrutinas deben ser definidas
.. en la sección ``contains`` del programa.
.. 
.. La sintaxis para definir una subrutina es::
.. 
..     subroutine nombre(parámetros)
..         ! declaración de variables locales
.. 
..         ! código de la función
..     end subroutine nombre
.. 
.. Por ejemplo,
.. podemos definir una subrutina que pida al usuario
.. llenar los elementos de un arreglo::
.. 
..     subroutine leer_datos(nr_datos):
..         integer :: nr_datos, i
.. 
..         print *, 'Ingrese', nr_datos, 'datos'
..         do i = 1, nr_datos
..             read *, datos(i)
..         end do
..     end subroutine leer_datos
.. 
.. La subrutina guarda los valores
.. en un arreglo llamado ``datos``,
.. que debe haber sido declarado en el programa.
.. La subrutina recibe como parámetro
.. la cantidad de elementos del arreglo que serán llenadas.
.. 
.. Llamadas a subrutinas
.. ~~~~~~~~~~~~~~~~~~~~~
.. .. index:: llamada a subrutina, call
.. 
.. Al igual que las funciones,
.. las subrutinas son llamadas
.. pasando los parámetros entre paréntesis
.. a continuación del nombre.
.. 
.. A diferencia de las funciones,
.. las subrutinas no pueden ser usadas en una expresión,
.. ya que no entregan un resultado.
.. 
.. La manera de llamar una subrutina en un programa
.. es usando la sentencia **call** (en inglés: «llamar»).
.. Por ejemplo,
.. para usar la subrutina ``llenar_datos``,
.. debe ser llamada de la siguiente manera::
.. 
..     call llenar_datos(10)
.. 
.. En el siguiente programa usamos la subrutina ``llenar_datos``
.. para leer los valores, y además definimos otra subrutina
.. llamada ``mostrar_datos`` que imprime los valores del arreglo.
.. El programa como tal tiene tres líneas,
.. que describen exactamente lo que hace:
.. lee los datos a un arreglo, lo eleva al cuadrado y lo muestra en la pantalla.
.. 
.. .. literalinclude:: programas/cuadrado-arreglo.f95
.. 
.. .. include:: disqus.rst
.. 
