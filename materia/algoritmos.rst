.. _algoritmos:

Algoritmos
==========

.. index:: algoritmo

Un **algoritmo** es una secuencia de pasos
para resolver un problema.

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

Cómo describir un algoritmo
---------------------------
Consideremos un ejemplo sencillo:
un algoritmo para resolver ecuaciones cuadráticas.

.. index:: ecuación cuadrática

Una `ecuación cuadrática`_ es una ecuación de la forma
`ax^2 + bx + c = 0`,
donde `a`, `b` y `c` son datos dados, con `a\ne 0`,
y `x` es la incógnita cuyo valor que se desea determinar.

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

Al estudiar álgebra aprendemos un algoritmo para resolver este problema.
Es lo suficientemente detallado para que pueda usarlo cualquier persona,
incluso sin saber qué es una ecuación cuadrática,
o para que lo pueda hacer un computador.
A continuación veremos algunas maneras de describir el procedimiento.

Lenguaje natural
~~~~~~~~~~~~~~~~
Durante el proceso mental de diseñar un algoritmo,
es común pensar y describir los pasos
en la misma manera en que hablamos a diario.
Por ejemplo:

    Teniendo los valores de `a`, `b` y `c`,
    calcular el discriminante `b^2 - 4ac`.
    Si es discriminante es negativo, entonces la ecuación no tiene soluciones
    reales. Si es discriminante es igual a cero, entonces la ecuación tiene una
    única solución real, que es `x = -b/2a`. Si el discriminante es positivo,
    entonces la ecuación tiene dos soluciones reales, que son
    `x_1 = (-b - \sqrt{D})/2a` y `x_2 = (-b + \sqrt{D})/2a`.
    
Esta manera de expresar un algoritmo no es ideal, ya que el lenguaje natural es:

* impreciso: puede tener ambigüedades;
* no universal: personas distintas describirán el proceso de maneras distintas; y
* no estructurado: la descripción no está expresada en función de componentes simples.

Diagrama de flujo
~~~~~~~~~~~~~~~~~
Un **diagrama de flujo** es una representación gráfica de un algoritmo.
Los pasos son representados por varios tipos de bloques,
y el flujo de ejecución es indicado por flechas que conectan los bloques:

.. image:: ../diagramas/cuadratica.png
   :align: center

El inicio y el final del algoritmo son representados con bloques circulares.
El algoritmo siempre debe ser capaz llegar desde uno hasta el otro,
sin importar por qué camino lo hace.
Un algoritmo no puede «quedarse pegado» en la mitad.

La entrada y la salida de datos son representadas con romboides,
que en la figura de arriba están pintados de verde.

Los diamantes representan condiciones
en las que el algoritmo sigue uno de dos caminos.
que están etiquetados con *sí* o *no*,
dependiendo si la condición es verdadera o falsa.

También puede haber ciclos,
representados por flechas
que regresan a bloques anteriores.

Otras sentencias van dentro de rectángulos,
que en la figura están pintados de azul.

Los diagramas de flujo no son usados en la práctica para programar,
pero son útiles para ilustrar cómo funcionan algoritmos sencillos.

Pseudocódigo
~~~~~~~~~~~~
El **pseudocódigo** es una descripción estructurada de un algoritmo
basada en ciertas convenciones notacionales.
Si bien es muy parecido al código que finalmente se escribirá en el computador,
el pseudocódigo está pensado para ser leído por humanos.

Una manera de escribir el algoritmo para la ecuación cuadrática
en pseudocódigo es la siguiente:

.. code-block:: none

    leer a
    leer b
    leer c

    discriminante ← b² - 4ac
    si discriminante < 0:
        escribir 'La ecuación no tiene soluciones reales'
    o si no, si discriminante == 0:
        x ← -b / 2a
        escribir 'La solución única es', x
    o si no:
        x1 ← (-b - √discriminante) / 2a
        x2 ← (-b + √discriminante) / 2a
        escribir 'Las dos soluciones reales son:'
        escribir x1
        escribir x2

Código
~~~~~~
.. index:: lenguaje de programación

El producto final de la programación
siempre debe ser código que pueda ser ejecutado en el computador.
Esto requiere describir los algoritmos
en un **lenguaje de programación**.
Los lenguajes de programación
definen un conjunto limitado de conceptos básicos,
en función de los cuales uno puede expresar cualquier algoritmo.

En esta asignatura,
usaremos el lenguaje de programación Python_
para escribir nuestros programas.

.. _Python: http://python.org/

El código en Python para resolver la ecuación cuadrática es el siguiente:

.. literalinclude:: programas/cuadratica.py

A partir de ahora, usted aprenderá a entender, escribir y ejecutar
códigos como éste.

