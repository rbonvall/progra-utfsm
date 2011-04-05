def imprimir_datos(nombre, apellido, rol,
                   dia, mes, anno):
    print 'Nombre completo:', nombre, apellido
    print 'Rol:', rol
    print 'Fecha de nacimiento:',
    print dia, '/', mes, '/', anno

imprimir_datos('Perico', 'Los Palotes',
               '201101001-1',  3, 1, 1993)
imprimir_datos('Yayita', 'Vinagre',
               '201101002-2', 10, 9, 1992)
imprimir_datos('Fulano', 'De Tal',
               '201101003-3', 14, 5, 1990)
