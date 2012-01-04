Calcular la edad del usuario
============================

.. highlight:: c

El siguiente programa
le pide al usuario ingresar su año de nacimiento
y el año actual.
A continuación,
le muestra cuál es su edad:

.. literalinclude:: programas/edad.c

Como siempre,
el código del programa debe estar incluído
dentro de una función llamada ``main``,
y la última sentencia del programa
debe ser ``return 0``.

Escriba, compile y ejecute este programa.

Declaración de variables
------------------------

Este programa utiliza tres variables,
llamadas ``nacimiento``, ``actual`` y ``edad``.

En Python, las variables eran creadas automáticamente
al momento de asignarlas por primera vez:

.. code-block:: python

    nacimiento = int(raw_input("Ingrese su anno de nacimiento: "))
    actual = int(raw_input("Ingrese el anno actual: "))
    edad = actual - nacimiento

En C no es así.
Las variables deben ser **declaradas** antes de ser usadas.
Además,
uno debe indicar de qué tipo serán los datos
que se almacenarán en cada variable.
Una variable sólo puede almacenar valores de un único tipo.

Las tres primeras sentencias del programa
declaran las variables ``nacimiento``, ``actual`` y ``edad``
para almacenar valores de tipo ``int`` (entero).

En C, todas las declaraciones tienen la estructura ``tipo variable;``.

¿Por qué es necesario declarar las variables?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Una característica del lenguaje C
es que entrega al programador el poder (y la responsabilidad)
de decidir muy de cerca cómo usar la memoria del computador.
En Python, al contrario,
el intérprete decide por uno
cuándo, cómo y cuánta memoria el programa utilizará,
lo que es muy conveniente a la hora de programar
pero que puede conducir a un uso ineficiente de los recursos disponibles
en ciertas ocasiones.

En nuestro programa de ejemplo,
el compilador analizará el código
y sabrá que el programa sólo almacenará tres valores,
y que cada uno sólo necesitará el espacio suficiente
para guardar un número entero.
¡Todo esto ocurre antes de que el programa sea siquiera ejecutado por primera vez!


Entrada con scanf
-----------------

Ya conocimos la función ``printf``,
que sirve para imprimir un (único) string por pantalla.

Para recibir la entrada del programa
se utiliza la función **scanf**,
cuyo uso puede parecer un poco extraño al principio.

El primer parámetro de la función ``scanf``
es un string que describe cuál es el formato
en el que estará representado el valor a ingresar.
En este ejemplo, el string ``"%d"``
indica que el valor a ser leído
debe ser interpretado como un número entero
en representación decimal
(dígitos del 0 al 9, posiblemente con un signo al principio).
Por supuesto,
hay muchos otros indicadores de formato.

El segundo parámetro debe indicar
**en qué lugar de la memoria del computador
se debe guardar el valor ingresado**.
Note que aquí no se pone la variable a secas,
sino que antecedida de un signo ``&``.
La distinción es importante:

* ``nacimiento`` es el valor que tiene la variable ``nacimiento``,
* ``&nacimiento`` es la ubicación en la memoria de la variable ``nacimiento``.

El operador ``&`` se lee como «la dirección de».
Más adelante veremos qué significa esto.

En resumen, la sentencia::

    scanf("%d", &nacimiento);

es equivalente a la siguiente sentencia en Python:

.. code-block:: python

    nacimiento = int(raw_input())


Salida
------
La función ``printf`` imprime sólo strings, no enteros.
Sin embargo,
es posible insertar enteros dentro del string
usando descriptores de formato idénticos a los de la función ``scanf``.

En las posiciones del string en las que se desea mostrar un número entero,
debe insertarse el texto ``%d``.
Luego, cada uno de los valores enteros por imprimir
deben ser pasados como parámetros adicionales a la función.

Los siguientes ejemplos
muestran usos correctos e incorrectos de ``printf``.
Haga el ejercicio de darse cuenta de los errores::

    /* Correctos */
    printf("Hola mundo\n");
    printf("Usted tiene %d annos.", edad);
    printf("Usted tiene %d annos.\n", edad);
    printf("Usted tiene 18 annos.");
    printf("Usted tiene %d annos.", 18);
    printf("Usted tiene %d annos y %d meses.", edad, meses);

    /* Incorrectos */
    printf("Usted tiene %d annos.");
    printf("Usted tiene annos.", 18);
    printf("Usted tiene annos.", 18);
    printf("Usted tiene", edad, "annos.");
    printf("Usted tiene edad annos.");
    printf("Usted tiene"); printf(edad); printf("annos.");


Ejercicio
---------
Escriba un programa
que pregunte al usuario las notas de sus cuatro certámenes,
y le muestre cuál es su promedio, con decimales:

.. testcase::

    Nota 1: `37`
    Nota 2: `95`
    Nota 3: `77`
    Nota 4: `50`
    Su promedio es 64.75

Para declarar una variable de tipo real,
se debe indicar que el tipo es ``float``.

Para mostrar un número real con decimales,
se usa el descriptor de formato ``%f``.

