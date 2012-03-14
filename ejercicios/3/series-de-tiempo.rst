Series de tiempo
================

*Este problema apareció en el certamen 3 del primer semestre de 2011.*

Una **serie de tiempo**
es una secuencia de valores numéricos
obtenidos al medir algún fenómeno cada cierto tiempo.
Algunos ejemplos de series de tiempo son:
el precio del dólar en cada segundo,
el nivel medio mensual de concentración de `CO_2` en el aire y
las temperaturas máximas anuales de una ciudad.
En un programa, los valores de una serie de tiempo se pueden guardar en un arreglo.

Las **medias móviles** con retardo *p*  de una serie de tiempo
son la secuencia de todos los promedios de *p* valores consecutivos de la serie.

Por ejemplo,
si los valores de la serie son `\{5, 2, 2, 8, -4, -1, 2\}`
entonces las medias móviles con retardo 3 son:
`\frac{5 + 2 + 2}{3}`,
`\frac{2 + 2 + 8}{3}`,
`\frac{2 + 8 - 4}{3}`,
`\frac{8 - 4 - 1}{3}` y
`\frac{-4 -1 + 2}{3}`.

#. Escriba la función ``medias_moviles(serie, p)``
   que retorne el arreglo de las medias móviles con retardo *p* de la serie::

      >>> s = array([5, 2, 2, 8, -4, -1, 2])
      >>> medias_moviles(s, 3)
      array([ 3,  4,  2,  1, -1])

#. Las **diferencias finitas** de una serie de tiempo
   son la secuencia de todas las diferencias entre un valor y el anterior.

   Por ejemplo,
   si los valores de la serie son `\{5, 2, 2, 8, -4, -1, 2\}`
   entonces las diferencias finitas son:
   `(2  - 5)`,
   `(2  - 2)`,
   `(8  - 2)`,
   `(-4 - 8)`,
   `(-1 + 4)` y
   `(2  + 1)`.

   Escriba la función ``diferencias_finitas(serie)``
   que retorne el arreglo de las diferencias finitas de la serie::

      >>> s = array([5, 2, 2, 8, -4, -1, 2])
      >>> diferencias_finitas(s)
      array([ -3,   0,   6, -12,   3,   3])


