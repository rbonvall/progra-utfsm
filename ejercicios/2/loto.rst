Cartones de Loto
----------------

Para los siguientes ejercicios,
descarge el archivo juegos.txt_.
Este archivo tiene una lista
de todos los cartones jugados para un sorteo de Loto.
Cada línea del archivo tiene la lista de números
jugados en un cartón.

.. _juegos.txt: ../../_static/juegos.txt

Este archivo se puede abrir con cualquier editor de texto
para ver su contenido,
pero para resolver los problemas,
hay que escribir funciones que analicen los datos.

Todas las funciones deben hacer lo siguiente:

* abrir el archivo con ``archivo = open('juegos.txt')``;
* leer los datos y analizarlos,
* cerrar el archivo con ``archivo.close()``.

Como cada línea del archivo es un string,
hay que convertirlo a un conjunto de números
para poder analizarlos, de la siguiente manera::

    numeros_carton = set()
    for n in linea.split():
        numeros_carton.add(int(n))

También se puede hacer así::

    numeros_carton = set(map(int, linea.split()))

#. ¿Cuántos cartones de Loto fueron jugados?

   (Para responder la pregunta,
   escriba una función ``contar_cartones``
   que cuente los cartones del archivo).

#. De todos los cartones jugados,
   ¿cuántos escogieron el número 7?

   Para responder la pregunta,
   escriba una función ``contar_numero_en_cartones(n)``
   que cuente cuántos cartones tienen el número ``n``.

#. Escriba la función ``hay_ganadores(numeros)``,
   cuyo parámetro ``numeros``
   es el conjunto de los seis números de un sorteo,
   que indique si alguien se ganó el Loto::

     >>> hay_ganadores({13, 33, 5, 38, 1, 19})
     True
     >>> hay_ganadores({14, 21, 1, 36, 9, 17})
     False

#. Escriba la función ``n_aciertos(numeros, n)``,
   que indique cuántas personas tuvieron ``n`` aciertos,
   donde ``numeros`` es el conjunto de los seis números de un sorteo::

     >>> n_aciertos({13, 33, 5, 38, 1, 19}, 4)
     17
     >>> n_aciertos({20, 39, 6, 27, 12, 4}, 3)
     229
     >>> n_aciertos({1, 2, 3, 4, 5, 6}, 5)
     2

