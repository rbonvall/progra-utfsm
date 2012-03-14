El lenguaje C
=============

.. http://en.wikibooks.org/wiki/C_Programming/Why_learn_C%3F
.. http://c.learncodethehardway.org/book/learn-c-the-hard-wayli3.html
.. http://c2.com/cgi/wiki?CeeLanguage


Compilación y ejecución
-----------------------

Para ejecutar un programa en Python,
hay que pasarle el código
a un programa llamado **intérprete**.
Python es, pues,
un lenguaje interpretado:

.. code-block:: none

                ┌────────────────┐
    ┌─────┐     │                │
    │ .py ├────▸│   Intérprete   │
    └─────┘     │                │
                └────────────────┘

C, por otra parte,
es un lenguaje compilado:

.. code-block:: none

                ┌────────────────┐
    ┌─────┐     │                │     ┌─────┐
    │ .c  ├────▸│   Compilador   ├────▸│ BIN ├────▸ Procesador
    └─────┘     │                │     └─────┘
                └────────────────┘

