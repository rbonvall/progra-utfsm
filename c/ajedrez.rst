El peor ajedrez del mundo
=========================

.. highlight:: c

El programa que analizaremos ahora es un sencillo juego de ajedrez.
Este código es más largo que los que hemos visto hasta ahora,
así que cópielo y péguelo en vez de tipearlo.

.. literalinclude:: programas/ajedrez.c

Cada pieza del ajedrez la representaremos con una letra:

* P es el peón,
* T es la torre,
* C es el caballo,
* A es el alfil,
* D es la dama, y
* R es el rey.

Las piezas blancas serán letras mayúsculas,
y las negras, minúsculas.

En cada turno,
el programa mostrará la disposición del tablero,
y pedirá a uno de los jugadores que ingrese su jugada:

.. code-block:: none

       0 1 2 3 4 5 6 7
      +---------------+
    a |t c . d r a . t|
    b |p p p . p p p p|
    c |. . . . . c . .|
    d |. . . p . . . .|
    e |. . A . P . a .|
    f |. . . . . D . .|
    g |P P P P . P P P|
    h |T C A . R . C T|
      +---------------+
    Juega blanco: 

La jugada se ingresa indicando la casilla donde está la pieza que se moverá,
y la casilla a la que se moverá.
Cada casilla se ingresa como sus coordenadas (una letra y un número),
y ambas casillas van separadas por un espacio.
Por ejemplo:

.. code-block:: none

    Juega blanco: f5 e6

Nuestro juego de ajedrez es realmente malo.
No hace cumplir las reglas,
por lo que se puede mover las piezas como a uno se le dé la gana.
¡Incluso el jugador blanco puede mover las piezas negras!

Si uno ingresa jugadas que no tengan sentido,
el programa puede fallar de maneras inesperadas.
¡Inténtelo!


Tipos enumerados
----------------
Un **tipo enumerado** es un tipo de datos
que puede respresentar sólo una lista de valores discretos
indicados por el programador.

Para crear un tipo enumerado,
en C se usa la sentencia ``enum``,
en la que se enumera cuáles son los valores posibles.
Por ejemplo::

    enum sexo {MASCULINO, FEMENINO};
    enum semaforo {ROJO, AMARILLO, VERDE};
    enum palo {CORAZON, PICA, TREBOL, DIAMANTE};

Al principio de nuestro programa,
creamos un tipo enumerado llamado ``enum color``,
que podemos usar cuando necesitemos guardar algún color::

    enum color {BLANCO, NEGRO, VACIO};

El valor ``VACIO`` nos permite usar variables ``enum color``,
por ejemplo, para almacenar el color que tiene la pieza
que está en una casilla,
siendo que podría no haber ninguna pieza en ella.

La verdad es que en C los tipos enumerados son una farsa.
Al declarar una variable de tipo ``enum color``,
realmente estamos declarando una variable entera,
y los valores ``BLANCO``, ``NEGRO`` y ``VACIO``
son en realidad los enteros 0, 1, y 2.

Al compilador le da lo mismo si uno mezcla los valores enumerados
con los enteros, y no descubrirá ningún error que podamos haber cometido.
Al final, usar un tipo enumerado sirve sólo
para hacer que el código sea más fácil de comprender.
Pero si cometemos alguna barbaridad como  ``color = -9000``,
que probablemente es un error lógico de nuestro programa,
el compilador hará oídos sordos.

En nuestro programa,
nosotros nos aprovechamos de la dualidad enum-entero
para cambiar el turno después de cada jugada.
Lo lógico habría sido hacerlo de este modo::

    if (turno == BLANCO)
        turno = NEGRO;
    else if (turno == NEGRO)
        turno = BLANCO;

Pero nosotros sabemos que ``BLANCO`` y ``NEGRO`` son 0 y 1,
por lo que podemos abreviarlo ingeniosamente
(pero no más claramente)::

    turno = 1 - turno;


Arreglos bidimensionales
------------------------
No debería ser ningún misterio que
un **arreglo bidimensional** es un arreglo
cuyos elementos están numerados por dos índices
en lugar de uno.

Es bastante evidente que,
dada la forma que escogimos para representar las piezas,
la mejor manera de representar un tablero de ajedrez en nuestro programa
es usar un arreglo bidimensional de 8 × 8 caracteres::

    char tablero[8][8];

Esto hace que tengamos 64 variables de tipo ``char`` a nuestra disposición,
indexadas desde ``tablero[0][0]`` hasta ``tablero[7][7]``.

La manera de indexar correctamente un elemento del tablero
es usar la sintaxis ``tablero[fila][columna]``.
Es incorrecto usar la sintaxis ``tablero[fila, columna]``
que se usa en otros lenguajes de programación.

Por supuesto,
se pueden crear arreglos de todas las dimensiones que uno quiera,
que no necesariamente deben ser de los mismos tamaños::

    int milimetros_lluvia[100][12][31][24];
                      /* anno mes dia hora */


Variables globales
------------------
Las variables ``tablero`` y ``turno``
no fueron declaradas dentro de ninguna función,
sino al principio del programa.
Ambas son, pues, **variables globales**,
y por lo mismo pueden ser usadas
desde cualquier parte del programa.

Las variables globales existen desde que el programa comienza hasta que termina.
Jamás son destruidas ni borradas durante la ejecución.

En contraste,
las variables declaradas dentro de una función
son **variables locales**:
sólo pueden ser usadas dentro de la función,
son creadas al llamar la función
y destruidas cuando la función retorna.

Nuestro programa es más bien pequeño,
y por lo tanto las variables globales no entorpecen el entendimiento.
Al contrario:
sabemos que sólo hay un juego en curso
(que tiene un tablero y un jugador de turno),
por lo que tener que pasar explícitamente el tablero y el turno a cada función
haría que el código fuera más engorroso.
En este caso es apropiado usar variables globales.

Sin embargo,
al desarrollar aplicaciones grandes,
uno debe evitar usar las variables globales
como medio de comunicación entre partes del programa.
Idealmente,
cada función debería recibir toda la información que necesita
a través de sus parámetros,
y entregar sus resultados como valor de retorno.

Al usar información global,
el comportamiento de un trozo de código puede ser diferente
dependiendo del estado de variables que son asignadas
en partes bien alejadas del código.
Esto hace que los programas sean más difícil de entender
(porque hay que figurarse en la cabeza cuál es el estado global),
y los errores más difíciles de depurar.

Si usamos sólo información local
(variables locales, parámetros, valores de retorno)
entonces todo el comportamiento de una sección de programa
está determinado por información que se encuentra cercana a ella en el código.


Funciones que no retornan nada
------------------------------
La sintaxis para crear una función en C
exige indicar de qué tipo es su valor de retorno.
Sin embargo, es posible crear una función que no retorne nada.

Para esto, hay que poner que su tipo de retorno es ``void``,
que se puede interpretar como «ningún tipo».

Hay varias razones por la que una función podría no retornar nada:

* la función hace entrada o salida (como ``imprimir_tablero``),
* la función actúa sobre variables globales (como ``mover_pieza``),
* la función debe «retornar» más de un valor,
  por lo que se usan los parámetros para entregar los valores
  (como ``leer_jugada``, explicado más adelante).


Macros con parámetros
---------------------
Ya vimos que una macro es una sustitución textual que se hace en el código
previo a la compilación.
Las macros además pueden recibir parámetros,
lo que las convierte en una especie de plantilla
para hacer sustituciones en el programa.

Como en nuestro programa del ajedrez tenemos que hacer varios ciclos
que vayan de 0 a 7 para recorrer el tablero,
decidimos crear una macro llamada ``FOR``
que sea equivalente a hacer un ciclo ``for`` de 0 a 7 con alguna variable::

    #define FOR(var)  for (var = 0; var < 8; ++var)

Como parámetro, debemos pasarle a ``FOR`` el nombre de la variable
que queremos usar como contador en nuestro ciclo.
Note que no estamos pasando el valor de la variable:
la sustitución es meramente textual.

En esencia estamos modificando la sintaxis del lenguaje.
En general **es una mala práctica hacer cosas como ésta**.
Como la sustitución es puramente textual y nunca se verifica que tenga sentido,
esto puede causar errores muy extraños si no se programa con cuidado.
También estamos haciendo más difícil a otros programadores entender nuestro código,
ya que ellos están familiarizados con la sintaxis del lenguaje
pero no con nuestras construcciones.

Uno puede ponerse muy creativo para crear macros.
Casi nunca es buena idea ceder a la tentación.
Sólo hay que hacerlo cuando en efecto se logra
hacer que el programa resulte más legible.
¿Cree usted que lo conseguimos con este ejemplo?


Declaraciones de funciones
--------------------------
El compilador analiza el código del programa de arriba hacia abajo.
Es necesario que todos los nombres (como variables, tipos y funciones)
ya hayan sido declarados antes de que aparezcan en el código.

Por esto mismo,
cuando creábamos funciones,
lo hacíamos antes de la función ``main``.
De otro modo,
el compilador no sabría que las funciones que llamamos desde ``main`` existen.

En el caso de las funciones,
hay que distinguir entre dos cosas:

* la **declaración** de la función,
  que consiste en especificar su nombre,
  su tipo de retorno y los tipos de los parámetros
  para que el compilador los conozca, y
* la **definición** de la función,
  que es especificar cuál es el código de la función.

En el programa del ajedrez,
las funciones están declaradas pero no definidas al principio del código.
Gracias a esto, las podemos llamar desde ``main``.
El compilador sabrá exactamente a qué nos referimos
cuando decimos ``color_pieza`` o ``juego_terminado``,
y podrá verificar que estos nombres están siendo usados
correctamente.

Aún así, las funciones deben estar definidas
en alguna otra parte (única) del programa
para que la compilación pueda ser completada.

Para declarar las funciones,
no es necesario explicitar los nombres de los parámetros,
pero está permitido hacerlo.
Las siguientes dos declaraciones son válidas::

    float potencia(float, int);
    float potencia(float base, int exponente);

En C, se le llama **prototipo** a la declaración de una función.
Los tipos de retorno y de los parámetros
conforman la **firma** de la función.

Las cabeceras ``.h`` que incluímos siempre en nuestros programas
contienen sólo las declaraciones de las funciones que proveen,
no las definiciones.
Al compilar nuestro código,
al compilador no le importa qué hacen esas funciones,
sino solamente cuáles son sus firmas.
Recién en la fase final de la compilación
(llamada enlazado_)
el compilador se encarga de averiguar
dónde está el código (ya compilado) de esas funciones.

.. _enlazado: http://en.wikipedia.org/wiki/Linker_(computing)

Si una función está definida pero no declarada,
entonces la definición actúa también como declaración.
Si una función está declarada antes de ser definida,
entonces las firmas del prototipo y de la definición
deben coincidir.


Paso de parámetros por referencia
---------------------------------

Conversiones de caracteres
--------------------------
