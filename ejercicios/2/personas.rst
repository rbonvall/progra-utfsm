Personas
--------

Para realizar estos ejercicios ,
usted debe descargar `el módulo con los datos`_
que vamos a utilizar.

.. _el módulo con los datos: ../../_static/personas.py

Para usar el módulo
hay que descargarlo en la misma carpeta
en la que se guardará el programa
e importar los datos de esta forma::

    from personas import *

Este módulo contiene una lista llamada ``personas``
que contiene tuplas que representan los datos de una persona.
Cada tupla tiene tres valores: el nombre, el apellido y la fecha de nacimiento.

El nombre y el apellido son strings,
y la fecha de nacimiento es una tupla de tres valores:
el día, el mes y el año.

Por ejemplo,
podemos ver los datos de la primera persona::

    >>> personas[0]
    ('Martín', 'Soto', (24, 8, 1990))

#. Escriba una función que imprima el nombre de todas las personas.
   Para eso, recorra la lista con un ``for``,
   obtenga el nombre de la persona
   e imprímalo usando ``print``.
   La función no tiene que retornar nada::

     >>> imprimir_nombres(personas)
     Martín
     Gabriel
     Humberto
     Sebastián
     Víctor
     ...
     Horacio
     Ignacio
     Nicolás
     Pablo
     Rolando
     Ricardo

#. Escriba una función que imprima la fecha de nacimiento
   de todas las personas::

     >>> imprimir_fechas(personas)
     24 de agosto de 1990
     2 de junio de 1974
     14 de noviembre de 1973
     18 de septiembre de 1973
     12 de agosto de 1992
     ...
     18 de agosto de 1981
     24 de abril de 1972
     17 de mayo de 1977
     4 de febrero de 1972
     29 de enero de 1976

   Para hacerlo más fácil,
   construya un diccionario con los nombres de los meses::

     meses = {
         1: 'enero',
         2: 'febrero',
         # ...
         12: 'diciembre',
     }

#. Escriba una función llamada ``cuantas_personas(personas)``
   que retorne la cantidad de personas en la lista.

#. Escriba una función que retorne la lista de las personas
   que tienen cumpleaños el mismo día que usted.
   Por ejemplo::

     >>> mi_cumple(personas)
     ['Jonathan Sepulveda']

#. Escriba una función llamada ``cumples_repetidos(personas)``
   que pueda determinar las personas en la lista que
   tienen su cumpleaños el mismo día.

#. Escriba una función llamada ``nombre_mas_comun(personas)``
   que entregue el nombre que más se repite.

