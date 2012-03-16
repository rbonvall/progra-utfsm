El lenguaje C
=============

.. http://en.wikibooks.org/wiki/C_Programming/Why_learn_C%3F
.. http://c.learncodethehardway.org/book/learn-c-the-hard-wayli3.html
.. http://c2.com/cgi/wiki?CeeLanguage


Esta sección es el único «bla bla» de este apunte.


Compilación versus interpretación
---------------------------------
Cuando programamos en Python,
en cierto modo estamos haciendo trampa.
El código Python no es ejecutado físicamente por el computador,
sino por un **intérprete**, que es el programa que ejecuta los programas.
El lenguaje C permite hacer «menos trampa»,
ya que sí es un medio para dar instrucciones al procesador del computador.

El **procesador** es el componente del computador
que ejecuta las instrucciones de un programa.

Las instrucciones que el procesador recibe
no están en un lenguaje de programación como Python o C,
sino en un `lenguaje de máquina`_, que es mucho más básico.
Cada procesador viene diseñado «de fábrica»
para entender su propio lenguaje de máquina,
que se compone de instrucciones_ muy básicas,
como leer un dato, aplicar una operación sobre un par de datos
o saltar a otra parte de la memoria para leer una nueva instrucción.

.. _lenguaje de máquina: http://en.wikipedia.org/wiki/Machine_code
.. _instrucciones: http://en.wikipedia.org/wiki/Instruction_set

Si bien es posible programar directamente en el lenguaje de la máquina,
esto es extremadamente engorroso,
y lo más probable es que usted nunca tenga la necesidad de hacerlo.
Decimos que el lenguaje de máquina es `de bajo nivel`_,
que en computación no es un término peyorativo,
sino que significa que está tan ligado al hardware
que no es lo suficientemente expresivo para describir algoritmos
de manera abstracta.

.. _de bajo nivel: http://en.wikipedia.org/wiki/Low-level_programming_language

Es más razonable programar en un lenguaje de programación de alto nivel,
que nos ofrezca abstracciones como:
variables, condicionales, ciclos, funciones, tipos de datos, etc.,
que permiten describir algoritmos en términos más humanos y menos «ferreteros».

C y Python son lenguajes tales,
pero difieren en la forma en que son ejecutados.




Un programa llamado **compilador** recibe como entrada el código C
y genera como salida código **binario**
que el procesador es capaz de entender.
El binario puede ser un programa ejecutable,
o una biblioteca con funciones que pueden ser llamadas desde un programa.

.. code-block:: none

                ┌────────────────┐                 ┌────────────────┐
    ┌─────┐     │                │     ┌─────┐     │                │
    │ .c  ├────▸│   Compilador   ├────▸│ BIN ├────▸│   Procesador   │
    └─────┘     │                │     └─────┘     │                │
                └────────────────┘                 └────────────────┘

A pesar de que el compilador actúa de intermediario
entre nuestro código y el procesador,
el lenguaje C sigue siendo de más bajo nivel que Python.
Al programar en C
tenemos acceso a detalles de la máquina
que son transparentes desde Python.


Python es un lenguaje de más alto nivel que C.
Un programa en C no es 



Lecturas adicionales
--------------------
Para profundizar acerca de la relevancia del lenguaje C
y las razones para estudiarlo,
le sugerimos leer los siguientes enlaces.


* `The Cartesian Dream of C <http://c.learncodethehardway.org/book/learn-c-the-hard-wayli3.html>`_.
* `Why learn C <http://en.wikibooks.org/wiki/C_Programming/Why_learn_C%3F>`_ en el wikibook de C.
* `C Language <http://c2.com/cgi/wiki?CeeLanguage>`_ en WikiWikiWeb.
