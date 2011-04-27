Procesamiento de texto
======================

.. index:: procesamiento de texto

Hasta ahora, hemos visto cómo
los tipos de datos básicos (strings, enteros, reales, booleanos)
y las estructuras de datos permiten
representar y manipular información compleja y abstracta en un programa.

Sin embargo, en muchos casos
la información no suele estar disponible ya organizada
en estructuras de datos convenientes de usar,
sino en documentos de texto.

Por ejemplo,
las páginas webs son archivos de puro texto,
que describen la estructura de un documento
en un lenguaje llamado HTML.
Usted puede ver el texto de una página web
buscando una instrucción «Ver código fuente»
(o algo parecido) en el navegador.
A partir de este texto,
el navegador extrae la información necesaria
para reconstruir la página que finalmente usted ve.

Un texto siempre es un string,
que puede ser tan largo y complejo como se desee.
El procesamiento de texto consiste en manipular strings,
ya sea para extraer información del string,
para convertir un texto en otro,
o para codificar información en un string.

En Python,
el tipo ``str`` provee muchos métodos convenientes
para hacer procesamiento de texto,
además de las operaciones más simples que ya aprendimos
(como ``s + t``, ``s[i]`` y ``s in t``).

Saltos de línea
---------------
.. index:: salto de línea

Un string puede contener caracteres de **salto de línea**,
que tienen el efecto equivalente al de presionar la tecla Enter.
El caracter de salto de línea se representa con ``\n``::

    >>> a = 'piano\nviolin\noboe'
    >>> print a
    piano
    violin
    oboe

Los saltos de línea sólo son visibles al imprimir el string
mediante la sentencia ``print``.
Si uno quiere ver el valor del string en la consola,
el salto de línea aparecerá representado como ``\n``::

    >>> a
    'piano\nviolin\noboe'
    >>> print a
    piano
    violin
    oboe

Aunque dentro del string se representa como una secuencia de dos símbolos,
el salto de línea es un único caracter::

    >>> len('a\nb')
    3

.. index:: \

En general,
hay varios caracteres especiales que se representan
comenzando con una barra invertida (``\``)
seguida de una letra.
Experimente, y determine qué significan los caracteres especiales
``\t`` y ``\b``::

    print 'abcde\tefg\thi\tjklm'
    print 'abcde\befg\bhi\bjklm'

Para incluir una barra invertida dentro de un string,
hay que hacerlo con ``\\``::

    >>> print 'c:\\>'
    c:\>
    >>> print '\\o/  o\n |  /|\\\n/ \\ / \\'
    \o/  o
     |  /|\
    / \ / \

Reemplazar secciones del string
-------------------------------
.. index:: replace, reemplazar string

El método ``s.replace(antes, despues)`` busca en el string ``s``
todas las apariciones del texto ``antes`` y las reemplaza por ``despues``::

    >>> 'La mar astaba sarana'.replace('a', 'e')
    'Le mer estebe serene'
    >>> 'La mar astaba sarana'.replace('a', 'i')
    'Li mir istibi sirini'
    >>> 'La mar astaba sarana'.replace('a', 'o')
    'Lo mor ostobo sorono'

Hay que tener siempre muy claro que esta operación
no modifica el string, sino que retorna uno nuevo::

    >>> orden = 'Quiero arroz con pollo'
    >>> orden.replace('arroz', 'pure').replace('pollo', 'huevo')
    'Quiero pure con huevo'
    >>> orden
    'Quiero arroz con pollo'

Separar y juntar strings
------------------------
.. index:: split, separar string

``s.split()`` separa el strings en varios strings,
usando los espacios en blanco como separador.
El valor retornado es una lista de strings::

    >>> oracion = 'El veloz murcielago hindu  comia feliz  cardillo y kiwi'
    >>> oracion.split()
    ['El', 'veloz', 'murcielago', 'hindu', 'comia', 'feliz', 'cardillo', 'y', 'kiwi']

Además, es posible pasar un parámetro al método ``split``
que indica cuál será el separador a usar (en vez de los espacios en blanco)::

    >>> s = 'Ana lavaba las sabanas'
    >>> s.split()
    ['Ana', 'lavaba', 'las', 'sabanas']
    >>> s.split('a')
    ['An', ' l', 'v', 'b', ' l', 's s', 'b', 'n', 's']
    >>> s.split('l')
    ['Ana ', 'avaba ', 'as sabanas']
    >>> s.split('aba')
    ['Ana lav', ' las s', 'nas']

Esto es muy útil para pedir al usuario que ingrese datos en un programa
de una manera más conveniente, y no uno por uno.
Por ejemplo, antes hacíamos programas que funcionaban así:

.. testcase::

    Ingrese a: `2.3`
    Ingrese b: `1.9`
    Ingrese c: `2.3`
    El triangulo es isoceles.

Ahora podemos hacerlos así:

.. testcase::

    Ingrese lados del triangulo: `2.3 1.9 2.3`
    El triangulo es isoceles.

En este caso, el código del programa podría ser::

    entrada = raw_input('Ingrese lados del triangulo: ')
    lados = entrada.split()
    a = int(lados[0])
    b = int(lados[1])
    c = int(lados[2])
    print 'El triangulo es', tipo_triangulo(a, b, c)

O usando la función ``map``, más simplemente::

    entrada = raw_input('Ingrese lados del triangulo: ')
    a, b, c = map(int, entrada.split())
    print 'El triangulo es', tipo_triangulo(a, b, c)

.. index:: join, unir strings

``s.join(lista_de_strings)`` une todos los strings de la lista,
usando al string ``s`` como «pegamento»::

    >>> valores = map(str, range(10))
    >>> pegamento = ' '
    >>> pegamento.join(valores)
    '0 1 2 3 4 5 6 7 8 9'
    >>> ''.join(valores)
    '0123456789'
    >>> ','.join(valores)
    '0,1,2,3,4,5,6,7,8,9'
    >>> ' --> '.join(valores)
    '0 --> 1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9'

Mayúsculas y minúsculas
-----------------------
.. index:: isupper, islower

``s.isupper()`` y ``s.islower()``
indican si el string está, respectivamente, en mayúsculas o minúsculas::

    >>> s = 'hola'
    >>> t = 'Hola'
    >>> u = 'HOLA'
    >>> s.isupper(), s.islower()
    (False, True)
    >>> t.isupper(), t.islower()
    (False, False)
    >>> u.isupper(), u.islower()
    (True, False)

.. index:: upper, lower

``s.upper()`` y ``s.lower()`` entregan el string ``s`` convertido,
respectivamente, a mayúsculas y minúsculas::

    >>> t
    'Hola'
    >>> t.upper()
    'HOLA'
    >>> t.lower()
    'hola'

.. index:: swapcase

``s.swapcase()`` cambia las minúsculas a mayúsculas, respectivamente,
a mayúsculas y minúsculas::

    >>> t.swapcase()
    'hOLA'

Lamentablemente, ninguno de estos métodos funcionan
con acentos y eñes::

    >>> print 'ñandú'.upper()
    ñANDú

Revisar contenidos del string
-----------------------------
.. index:: startswith, endswith

``s.startswith(t)`` y ``s.endswith(t)`` indican si el string ``s``
comienza y termina, respectivamente, con el string ``t``::

    >>> objeto = 'paraguas'
    >>> objeto.startswith('para')
    True
    >>> objeto.endswith('aguas')
    True
    >>> objeto.endswith('x')
    False
    >>> objeto.endswith('guaguas')
    False

Nuestro conocido operador ``in``
indica si un string está contenido dentro de otro::

    >>> 'pollo' in 'repollos'
    True
    >>> 'pollo' in 'gallinero'
    False

Alineación de strings
---------------------
.. index:: ljust, rjust, center

Los métodos ``s.ljust(n)``, ``s.rjust(n)`` y ``s.center(n)``
rellenan el string con espacios para que su largo sea igual a ``n``,
de modo que el contenido quede alineado, respectivamente,
a la izquierda, a la derecha y al centro::

    >>> contenido.ljust(20)
    'hola                '
    >>> contenido.center(20)
    '        hola        '
    >>> contenido.rjust(20)
    '                hola'

Estos métodos son útiles para imprimir tablas bien alineadas::

    datos = [
        ('Pepito', (1991, 12, 5), 'Osorno', '***'),
        ('Yayita', (1990, 1, 31), 'Arica', '*'),
        ('Fulanito', (1992, 10, 29), 'Porvenir', '****'),
    ]

    for n, (a, m, d), c, e in datos:
        print n.ljust(10),
        print str(a).rjust(4), str(m).rjust(2), str(d).rjust(2),
        print c.ljust(10), e.center(5)

Este programa imprime lo siguiente:

.. testcase::

    Pepito     1991 12  5 Osorno      ***
    Yayita     1990  1 31 Arica        *
    Fulanito   1992 10 29 Porvenir    ****

Interpolación de strings
------------------------
.. index:: interpolación de strings, format

El método ``format`` permite usar un string como una plantilla
que se puede completar con distintos valores dependiendo de la situación.

Las posiciones en que se deben rellenar los valores
se indican dentro del string usando un número
entre paréntesis de llaves::

    >>> s = 'Soy {0} y vivo en {1}'

Estas posiciones se llaman *campos*.
En el ejemplo, el string ``s`` tiene dos campos,
numerados del cero al uno.

Para llenar los campos,
hay que llamar al método ``format``
pasándole los valores como parámetros::

    >>> s.format('Perico', 'Valparaiso')
    'Soy Perico y vivo en Valparaiso'
    >>> s.format('Erika', 'Berlin')
    'Soy Erika y vivo en Berlin'
    >>> s.format('Wang Dawei', 'Beijing')
    'Soy Wang Dawei y vivo en Beijing'

El número indica en qué posición va el parámetro
que está asociado al campo::

    >>> '{1}{0}{2}{0}'.format('a', 'v', 'c')
    'vaca'
    >>> '{0} y {1}'.format('carne', 'huevos')
    'carne y huevos'
    >>> '{1} y {0}'.format('carne', 'huevos')
    'huevos y carne'

Otra opción es referirse a los campos con un nombre.
En este caso,
hay que llamar al método ``format``
diciendo explícitamente el nombre del parámetro
para asociarlo al valor::

    >>> s = '{nombre} estudia en la {universidad}'
    >>> s.format(nombre='Perico', universidad='UTFSM')
    'Perico estudia en la UTFSM'
    >>> s.format(nombre='Fulana', universidad='PUCV')
    'Fulana estudia en la PUCV'
    >>> s.format(universidad='UPLA', nombre='Yayita')
    'Yayita estudia en la UPLA'

