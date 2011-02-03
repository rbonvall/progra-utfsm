Introducción a la programación
==============================

Si tuvieramos que resumir el propósito de la programación en una frase,
ésta debería ser:

    que el computador haga el trabajo por nosotros.

Los computadores son buenos para hacer tareas rutinarias.
Idealmente, cualquier problema tedioso y repetitivo
debería ser resuelto por un computador,
y los seres humanos sólo deberíamos encargarnos
de los problemas realmente interesantes:
los que requieren creatividad, pensamiento crítico y subjetividad.

La **programación** es el proceso de
transformar un método para resolver problemas
en uno que pueda ser entendido por el computador.

    *La informática se trata de computadores
    tanto como la astronomía se trata de telescopios*.
    --- `Edsger Dijkstra <http://es.wikipedia.org/wiki/Edsger_Dijkstra>`_.

Al diseñar un programa,
el desafío principal es crear y describir un procedimiento
que esté completamente bien definido,
que no tenga ambigüedades,
y que efectivamente resuelva el problema.

Esto no tiene nada que ver con computadores.

Un procedimiento que resuelve un problema
es llamado un **algoritmo**.

Todo el mundo conoce y utiliza algoritmos a diario,
incluso sin darse cuenta:

* Una receta de cocina es un algoritmo;
  si bien podríamos cuestionar que algunos pasos son ambiguos
  (¿cuánto es «una pizca de sal»? ¿qué significa «agregar a gusto»?),
  en general las instrucciones están lo suficientemente bien definidas
  para que uno las pueda seguir sin problemas.

  La entrada de una receta son los ingredientes
  y algunos datos como: ¿para cuántas personas se cocinará?
  El proceso es la serie de pasos para manipular los ingredientes.
  La salida es el plato terminado.

  En principio,
  si una receta está suficientemente bien explicada,
  podría permitir preparar un plato
  a alguien que no sepa nada de cocina.

* El `método para multiplicar`_ números a mano
  que aprendimos en el colegio es un algoritmo.
  Dado cualquier par de números enteros,
  si seguimos paso a paso el procedimiento
  siempre obtendremos el producto:

  .. image:: ../diagramas/multiplicacion.gif
     :align: center

  La entrada del algoritmo de multiplicación
  son los dos factores.
  El proceso es la secuencia de pasos
  en que los dígitos van siendo multiplicados
  las reservas van siendo sumadas,
  y los productos intermedios son finalmente sumados.
  La salida del algoritmo es el producto obtenido.

.. _método para multiplicar: http://es.wikipedia.org/wiki/Algoritmo_de_multiplicación

No toda secuencia de instrucciones es un algoritmo.
Un algoritmo debe poder ser usado mecánicamente,
sin necesidad de usar inteligencia, intuición ni habilidad.


    *Los computadores son inútiles: sólo pueden darte respuestas*.
    --- `Pablo Picasso <http://es.wikipedia.org/wiki/Pablo_Picasso>`_.

.. .. raw:: html
.. 
..     <iframe
..       title="YouTube video player" class="youtube-player"
..       type="text/html" width="480" height="390"
..       src="http://www.youtube.com/embed/k6U-i4gXkLM?rel=0"
..       frameborder="0"></iframe>

..  *Los computadores son buenos para seguir instrucciones,
..  pero son malos leyéndote la mente*.
..  --- `Donald E. Knuth <http://es.wikipedia.org/wiki/Donald_Knuth>`_.

