.. _algoritmos:

Algoritmos
==========

.. index:: algoritmo

Un **algoritmo** es una secuencia de pasos para resolver un problema.

Los pasos deben estar muy bien definidos,
y tienen que describir sin ambigüedades
cómo llegar desde el inicio hasta el final.

Un algoritmo tiene tres componentes:

.. index:: entrada, proceso, salida

1. la **entrada**: son los datos que necesita un algoritmo
   para poder ser ejecutado;
2. el **proceso**: son los pasos que hay que seguir,
   utilizando la entrada;
3. la **salida**: es el resultado que entrega el algoritmo.

.. index:: problema computacional

Los algoritmos son una herramienta para resolver
**problemas computacionales**.
La definición de un problema computacional
especifica en términos generales
la relación deseada entre la entrada y la salida.
El algoritmo especifica
cómo la entrada se transforma en la salida.

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
Un algoritmo debe poder seguirse
sin necesidad de usar inteligencia, intuición ni habilidad.
Un criterio para saber si un algoritmo está bien descrito
puede ser: ¿podría un robot seguir estas instrucciones sin equivocarse?

Un ejemplo sencillo: resolver una ecuación cuadrática
-----------------------------------------------------

.. index:: ecuación cuadrática

Una `ecuación cuadrática`_
es una ecuación de la forma
`ax^2 + bx + c = 0`,
donde `a`, `b` y `c` son datos dados
y `x` es la incógnita que se desea determinar.

.. _ecuación cuadrática: http://es.wikipedia.org/wiki/Ecuaci%C3%B3n_de_segundo_grado

Por ejemplo, `2x^2 - 5x + 2 = 0` es una ecuación cuadrática
con `a = 2`, `b = -5` y `c = 2`.
Sus soluciones son `x_1 = 1/2` y `x_2 = 2`,
como se puede comprobar fácilmente
al reemplazar estos valores en la ecuación.
El problema es cómo obtener estos valores en primer lugar.

El problema computacional de resolver una ecuación cuadrática
puede ser planteado así:

  Dados `a`, `b` y `c`,
  entontrar los valores de `x`
  que satisfacen `ax^2 + bx + c = 0`.

En álgebra aprendemos un algoritmo para resolver este problema.
Es lo suficientemente detallado para que pueda usarlo cualquier persona,
incluso sin saber qué es una ecuación cuadrática,
o para que lo pueda hacer un computador:

1. Obtener los valores de
   `a`, `b` y `c`.
2. Calcular el discriminante `b^2 - 4ac`, y llamarlo `Δ`.
3. Si `Δ < 0`, entonces la ecuación no tiene soluciones reales.
4. Si `Δ = 0`, entonces la ecuación tiene una solución real,
   que es `x = -b/2a`.
5. Si `Δ > 0`, entonces
   la ecuación tiene dos soluciones reales,
   que son `x = (-b ± \sqrt{Δ})/2a`.
6. Entregar las soluciones `x` obtenidas.

La entrada es el paso 1, la salida es el paso 6,
y el resto de los pasos son parte del proceso.

Cómo describir un algoritmo
---------------------------
El lenguaje natural (la manera en que hablamos a diario)
no es el más apropiado para describir un algoritmo:
es complejo, ambiguo e impreciso.

Un algoritmo debe ser descrito mediante un lenguaje
cuyo significado sea universal.
Primero veremos
cuáles son los elementos básicos
mediante los que un algoritmo es descrito.
y durante el ramo aprenderemos
a implementarlos en el computador
usando el lenguaje Python.

