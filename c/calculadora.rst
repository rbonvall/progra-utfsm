Calculadora simple
==================

El siguiente programa
es una calculadora simple:

.. literalinclude:: programas/calculadora.c
   :language: c

Al ejecutar el programa,
primero uno ingresa la operación que será aplicada,
que puede ser:

======= ===============
Signo   Operación
------- ---------------
``+``   Suma
``-``   Resta
``*``   Multiplicación
``/``   División
``^``   Potencia
======= ===============

La multiplicación también puede ser indicada
con una ``x`` minúscula.

A continuación,
se debe ingresar los dos operandos.
Finalmente,
el programa muestra el resultado de la operación.

Escriba, compile y ejecute este programa.

En este programa
puede ver que es posible asignar un valor inicial a una variable 
al momento de declararla::

    float resultado = 1.0;
    int valido = 1;

También note que
tanto en el ``if`` como en el ``else`` del final
se ha omitido los paréntesis de llave (``{}``)
ya que en ambos casos
se incluye solamente una única sentencia.


Definición de funciones
-----------------------
Al principio del programa,
se ha definido una función llamada ``potencia``.
Ella recibe como parámetros
la base (un número real)
y el exponente (un entero),
y retorna el resultado de elevar la base al exponente.

En C no existe un operador «elevado a»
(como el ``**`` de Python),
por lo que sí es útil definir una función como ésta.

Es necesario especificar explícitamente
cuál será el tipo del valor retornado
(en este caso ``float``)
y los tipos de cada uno de los parámetros
(en el ejemplo, ``float`` e ``int``).

Las variables declaradas dentro de la función
se llaman **variables locales**.
Estas variables comienzan a existir
al momento de llamar a la función,
y desaparecen cuando la función termina.
Son invisibles desde fuera de la función.

En nuestro programa,
las dos funciones ``main`` y ``potencia``
tienen una variable local llamada ``resultado``.
Ambas variables son distintas,
y sus valores respectivos están almacenados
en regiones diferentes de la memoria.

Tipo char
---------
El tipo ``char`` se usa para representar
caracteres (símbolos) solitarios.
La variable ``op`` que almacena la operación
es de este tipo.

Un valor de tipo ``char``
se representa en un programa entre comillas simples.
Por ejemplo,
el signo más está representado como ``'+'``.

Técnicamente,
los valores de tipo ``char`` son números enteros
que están comprendidos entre −128 y 127.
Cada número está asociado a un caracter
a través de la `tabla ASCII`_.
Los enteros y los caracteres asociados son intercambiables;
por ejemplo, la expresión ``'m' == 109``
es evaluada como verdadera.

No hay que confundir un caracter
con un string de largo uno:
``'a'`` y ``"a"`` son dos cosas distintas.

.. _tabla ASCII: http://es.wikipedia.org/wiki/Código_ASCII

Sentencia switch
----------------
El **switch** es una sentencia de control condicional
que permite indicar qué hacer
si el resultado de una expresión
es igual a alguno de ciertos valores constantes indicados

Un ejemplo de uso de ``switch`` es el siguiente::

    switch (expresion) {
        case 1:
            /* que hacer cuando expresion == 1 */

        case 2:
            /* que hacer cuando expresion == 2 */

        default:
            /* que hacer cuando la expresion no es igual
             * a ninguno de los casos anteriores */
    }

Cuando el resultado de la expresión
es igual a alguno de los valores indicados,
la ejecución del programa salta al ``case``
con ese valor.
Si el valor con el resultado no existe,
salta a ``default``.

Hay que tener cuidado con una característica extraña
del ``switch``: cuando se cumple un caso,
los casos que vienen a continuación también se ejecutan.
En este ejemplo:

* si ``expresion == 1``,
  el programa saltará a ``case 1``,
  y luego continuará con ``case 2`` y ``default``;
* si ``expresion == 2``,
  el programa saltará a ``case 2``,
  y luego continuará con ``default``;
* si ``expresion`` no es ni 1 ni 2,
  el programa saltará a ``default``.

Para evitar que los casos siguientes sean ejecutados,
debe ponerse un ``break`` al final de cada caso.
Esto es lo que se hizo en el programa de la calculadora.

Conversión de tipos
-------------------
El segundo parámetro de la función ``potencia`` es entero,
pero los operandos ingresados por el usuario
son almacenados como números reales.

Para convertir el exponente de real a entero,
basta con anteponer al valor
el tipo entre paréntesis.

En este caso particular,
la conversión se hace truncando los decimales
del número real.
Así, si ``y`` vale ``5.9``,
entonces ``(int) y`` vale ``5``.
Para conversiones entre otros tipos,
se siguen otras reglas diferentes.

En inglés,
el nombre de esta operación es *cast*.
Posiblemente usted escuche más de una vez
a alguien refiriéndose a esta operación como «castear».

Ejercicios
----------
Modifique el programa
de modo que soporte una nueva operación:
obtener el `coeficiente binomial`_
entre ``x`` e  ``y``.
Esta operación debe ser indicada
con el símbolo ``b``.

El coeficiente binomial es una operación
entre números enteros.
Tenga cuidado y use conversiones apropiadas.

.. _coeficiente binomial: http://es.wikipedia.org/wiki/Coeficiente_binomial

