Consulta médica
---------------
Una consulta médica tiene un archivo ``pacientes.txt``
con los datos personales de sus pacientes.
Cada línea del archivo tiene el rut, el nombre y la edad de un paciente,
separados por un símbolo ``:``.
Así se ve el archivo:

.. code-block:: none

    12067539-7:Anastasia López:32
    15007265-4:Andrés Morales:26
    8509454-8:Pablo Muñoz:45
    7752666-8:Ignacio Navarro:49
    8015253-1:Alejandro Pacheco:51
    9217890-0:Patricio Pimienta:39
    9487280-4:Ignacio Rosas:42
    12393241-2:Ignacio Rubio:33
    11426761-9:Romina Pérez:35
    15690109-1:Francisco Ruiz:26
    6092377-9:Alfonso San Martín:65
    9023365-3:Manuel Toledo:38
    10985778-5:Jesús Valdés:38
    13314970-8:Abel Vázquez:30
    7295601-k:Edison Muñoz:60
    5106360-0:Andrea Vega:71
    8654231-5:Andrés Zambrano:55
    10105321-0:Antonio Almarza:31
    13087677-3:Jorge Álvarez:28
    9184011-1:Laura Andrade:47
    12028339-1:Jorge Argandoña:29
    10523653-0:Camila Avaria:40
    12187197-1:Felipe Ávila:36
    5935556-2:Aquiles Barriga:80
    14350739-4:Eduardo Bello:29
    6951420-0:Cora Benítez:68
    11370775-5:Hugo Berger:31
    11111756-k:Cristóbal Bórquez:34

Además,
cada vez que alguien se atiende en la consulta,
la visita es registrada en el archivo ``atenciones.txt``,
agregando una línea que tiene el rut del paciente,
la fecha de la visita (en formato ``dia-mes-año``)
y el precio de la atención,
también separados por ``:``.
El archivo se ve así:

.. code-block:: none

    8015253-1:4-5-2010:69580
    12393241-2:6-5-2010:57274
    10985778-5:8-5-2010:73206
    8015253-1:10-5-2010:30796
    8015253-1:12-5-2010:47048
    12028339-1:12-5-2010:47927
    11426761-9:13-5-2010:39117
    10985778-5:15-5-2010:86209
    7752666-8:18-5-2010:41916
    8015253-1:18-5-2010:74101
    12187197-1:20-5-2010:38909
    8654231-5:20-5-2010:75018
    8654231-5:22-5-2010:64944
    5106360-0:24-5-2010:53341
    8015253-1:27-5-2010:76047
    9217890-0:30-5-2010:57726
    7752666-8:1-6-2010:54987
    8509454-8:2-6-2010:76483
    6092377-9:2-6-2010:62106
    11370775-5:3-6-2010:67035
    11370775-5:7-6-2010:47299
    8509454-8:7-6-2010:73254
    8509454-8:10-6-2010:82955
    11111756-k:10-6-2010:56520
    7752666-8:10-6-2010:40820
    12028339-1:12-6-2010:79237
    11111756-k:13-6-2010:69094
    5935556-2:14-6-2010:73174
    11111756-k:21-6-2010:70417
    11426761-9:22-6-2010:80217
    12067539-7:25-6-2010:31555
    11370775-5:26-6-2010:75796
    10523653-0:26-6-2010:34585
    6951420-0:28-6-2010:45433
    5106360-0:1-7-2010:48445
    8654231-5:4-7-2010:76458

Note que las fechas están ordenadas de menos a más reciente,
ya que las nuevas líneas siempre se van agregando al final.

1. Escriba la función ``costo_total_paciente(rut)``
   que entregue el costo total de las atenciones
   del paciente con el rut dado::

    >>> costo_total_paciente('8015253-1')
    297572
    >>> costo_total_paciente('14350739-4')
    0

2. Escriba la función ``pacientes_dia(dia, mes, ano)``
   que entregue una lista con los nombres de los pacientes
   que se atendieron el día señalado::

    >>> pacientes_dia(2, 6, 2010)
    ['Pablo Muñoz', 'Alfonso San Martín']
    >>> pacientes_dia(23, 6, 2010)
    []

3. Escriba la función ``separar_pacientes()``
   que construya dos nuevos archivos:

   * ``jovenes.txt``, con los datos de los pacientes menores de 30 años;
   * ``mayores.txt``, con los datos de todos los pacientes mayores de 60 años.

   Por ejemplo,
   el archivo ``jovenes.txt`` debe verse así:

   .. code-block:: none

       15007265-4:Andrés Morales:26
       15690109-1:Francisco Ruiz:26
       13087677-3:Jorge Álvarez:28
       12028339-1:Jorge Argandoña:29
       14350739-4:Eduardo Bello:29

4. Escribir una función ``ganancias_por_mes()``
   que construya un nuevo archivo llamado ``ganancias.txt``
   que tenga el total de ganancias por cada mes
   en el siguiente formato:

   .. code-block:: none

       5-2010:933159
       6-2010:1120967
       7-2010:124903

