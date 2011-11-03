Notas de certamenes
-------------------

Desarrolle un programa para poder manipular
las notas de tres certámenes de los 10
alumnos de un curso:

+----+----+----+
| C1 | C2 | C3 |
+====+====+====+
| 58 | 65 | 53 |
+----+----+----+
| 44 | 84 | 60 |
+----+----+----+
| ...| ...| ...|
+----+----+----+
| 65 | 60 | 80 |
+----+----+----+

Para almacenar la información se puede utilizar
una matriz de 10 filas y 3 columnas, donde en cada
columna para una determinada fila, se almacenará
la nota que el alumno, representado por la fila,
obtuvo en uno de los tres certámenes (la fila *i*
representa al alumno *i* y la nota del certamen 1
está en la columna 1, la nota del certamen 2 en
la columna 2, etc).

Además, utilice un arreglo unidimensional de largo
10 para almacener los nombres de los alumnos.
Así en la posición *i* del arreglo estará el nombre
del alumno *i*. El programa debe:

* Ingresar el nombre y las notas para todos los alumnos
  del curso.
* Calcular el promedio de cada alumno.
* Calcular el promedio del curso en cada certamen.
* Calcular el promedio general del curso.
* Calcular la cantidad de alumnos aprobados
  (promedio >= 55) y reprobados (promedio < 55
* Ordenar alumnos según promedio
* Mostrar el nombre, notas de certámenes y promedio
  final para cada alumno ordenado.

::

	Nombre 1: Manuel Pavez
	C1: 55
	C2: 60
	C3: 75
	Nombre 2: Guillermo Fuenzalida
	C1: 60
	C2: 60
	C3: 20
	...
	Nombre 10: Cristian Perez
	C1: 100
	C2: 0
	C3: 55
	Promedio 1: 63.3
	Promedio 2: 46.6
	...
	Promedio 10: 51.6
	Promedio del curso C1: 56
	Promedio del curso C2: 30
	Promedio del curso C3: 60
	Promedio Final Curso: 55
	Aprobados: 4
	Reprobados: 6
	...
	Guillermo Fuenzalida 46.6
	...
	Cristian Perez 51.6
	...
	Manuel Pavez 63.3
	...
