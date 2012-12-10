.. _programas:

Desarrollo de programas
=======================

.. index:: programa, intérprete

Un **programa** es un archivo de texto
que contiene código para ser ejecutado por el computador.

En el caso del lenguaje Python,
el programa es ejecutado por un **intérprete**.
El intérprete es un programa que ejecuta programas.

Los programas escritos en Python
deben estar contenidos en un archivo
que tenga la extensión ``.py``.
En Windows, el programa puede ser ejecutado
haciendo doble clic sobre el ícono del archivo.

Para probar cómo hacerlo,
descargue el programa cuadratica.py_
que sirve para resolver ecuaciones cuadráticas.

.. _cuadratica.py: ../_static/programas/cuadratica.py

Edición de programas
--------------------
.. index:: editor de texto

Un programa es un `archivo de texto`_.
Por lo tanto, puede ser creado y editado
usando cualquier `editor de texto`_,
como el Bloc de Notas.

Lo que no se puede usar
es un procesador de texto,
como Microsoft Word.

Haga la prueba:
abra el programa ``cuadratica.py``
con el Bloc de Notas (u otro editor)
y verá su contenido.

.. _archivo de texto: http://es.wikipedia.org/wiki/Archivo_de_texto
.. _editor de texto: http://es.wikipedia.org/wiki/Editor_de_texto

.. index:: editor de texto (lista)

Otros editores de texto
(mucho mejores que el Bloc de Notas)
que usted puede instalar son:

* en Windows:
  `Notepad++ <http://notepad-plus-plus.org/>`_,
  `Textpad <http://www.textpad.com/>`_;
* en Mac:
  `TextWrangler <http://www.barebones.com/products/textwrangler/>`_,
  `TextMate <http://macromates.com/>`_;
* en Linux:
  `Gedit <http://projects.gnome.org/gedit/>`_,
  `Kate <http://kate-editor.org/>`_.


Instalación del intérprete de Python
------------------------------------
.. index:: intérprete (instalación)

Una cosa es editar el programa, y otra es ejecutarlo.
Para poder ejecutar un programa en Python
hay que instalar el **intérprete**.

En la `página de descargas de Python`_
está la lista de instaladores.
Debe descargar el indicado para su computador
y su sistema operativo.

.. _página de descargas de Python: http://www.python.org/download/
..

La versión que debe instalar es la **2.7.3**, no la 3.2.3.

No use los instaladores que dicen ``x86-64``
a no ser que esté seguro que su computador
tiene una arquitectura de 64 bits
(lo más probable es que no sea así).

Ejecución de un programa
------------------------
Una vez escrito el programa e instalado el intérprete,
es posible ejecutar los programas.
Para hacerlo,
haga doble clic en el ícono del programa.

Uso de la consola
-----------------
.. index:: intérprete (interactivo), consola

La ejecución de programas
no es la única manera de ejecutar el intérprete.
Si uno ejecuta Python sin pasarle ningún programa,
se abre la **consola** (o **intérprete interactivo**).

La consola permite ingresar un programa línea por línea.
Además,
sirve para evaluar expresiones y ver su resultado inmediatamente.
Esto permite usarla como si fuera una calculadora.

La consola interactiva
siempre muestra el símbolo ``>>>``,
para indicar que ahí se puede ingresar código.
En todos los libros sobre Python,
y a lo largo de este apunte,
cada vez que aparezca un ejemplo en el que aparezca este símbolo,
significa que debe ejecutarse en la consola,
y no en un programa. Por ejemplo::

    >>> a = 5
    >>> a > 10
    False
    >>> a ** 2
    25

En este ejemplo, al ingresar las expresiones ``a > 10`` y ``a ** 2``,
el intérprete interactivo entrega los resultados ``False`` y ``25``.

No hay ningún motivo para tipear el símbolo ``>>>``
ni en un programa ni en un certamen,
pues no es parte de la sintaxis del lenguaje.


Entornos de desarollo
---------------------
.. index:: entorno de desarrollo, IDE

En general,
usar un simple editor de texto para escribir programas
no es la manera más eficiente de trabajar.

Los **entornos de desarrollo**
(también llamados *IDE*, por sus siglas en inglés)
son aplicaciones que hacen más fácil la tarea
de escribir programas.

Python viene con su propio entorno de desarrollo llamado **IDLE**.
IDLE viene con una consola y un editor de texto.

Además, hay otros buenos entornos de desarrollo más avanzados para Python:

* `PyScripter <http://code.google.com/p/pyscripter/downloads/list>`_,
* `WingIDE 101 <http://www.wingware.com/downloads/wingide-101/3.2.12-1/binaries>`_

Usted puede probar éstos y usar el que más le acomode durante el semestre.

El siguiente video muestra cómo usar IDLE para desarrollar un programa
y para usar la consola interactiva:

.. raw:: html

    <iframe width="640" height="360" src="http://www.youtube.com/embed/Fz5pk0K54dE?rel=0&amp;hd=1" frameborder="0" allowfullscreen></iframe>

Si desea trabajar con PyScripter en vez de IDLE,
puede ver `este otro video`_
con una demostración de cómo usarlo.

.. _este otro video: http://www.youtube.com/watch?v=bzF5rDtQLS4

