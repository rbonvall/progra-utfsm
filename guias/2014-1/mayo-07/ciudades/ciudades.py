'''
# CASOS
>>> ciudades(info)
set(['Concepcion', 'Osorno', 'Arica',
     'Chillan', 'Puerto Montt'])

>>> regiones(info)
set(['X', 'XV', 'VIII'])

>>> ciudades_por_region(info)
{'X':    set(['Puerto Montt', 'Osorno']),
 'XV':   set(['Arica']),
 'VIII': set(['Concepcion', 'Chillan'])}

# FIN CASOS
'''


# Fuente: http://ww2.educarchile.cl/UserFiles/P0001/Image/CR_Imagen/Mapas%20IGM/mapas_historia_chilena/fundacion_y_origen_de_las_c.gif
# INFO
info = {
  'Arica': ('XV', 1570),
  'Concepcion': ('VIII', 1550),
  'Osorno': ('X', 1558),
  'Puerto Montt': ('X', 1853),
  'Chillan': ('VIII', 1580)
}
# FIN INFO

def ciudades(info):
    return set(info)

def regiones(info):
    r = set()
    for c in info:
        region, anno = info[c]
        r.add(region)
    return r

def ciudades_por_region(info):
    d = {}
    for ciudad in info:
        region, anno = info[ciudad]
        if region not in d:
            d[region] = set()
        d[region].add(ciudad)
    return d

