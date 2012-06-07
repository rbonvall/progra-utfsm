def combinar_mapas(ma, mb):
    mapa = dict()
    for ciudad in ma:
        mapa[ciudad] = ma[ciudad]
    for ciudad in mb:
        if ciudad in mapa:
            mapa[ciudad] |= mb[ciudad]
        else:
            mapa[ciudad] = mb[ciudad]
    return mapa


# Ejemplos del enunciado
mapa1 = {
    'A': set('BH'),
    'B': set('AD'),
    'D': set('BH'),
    'E': set('H'),
    'H': set('ADE'),
}
mapa2 = {
    'B': set('DF'),
    'D': set('BFGE'),
    'E': set('D'),
    'F': set('BDG'),
    'G': set('DF'),
}
mapa_combinado = {
    'A': set('BH'),
    'B': set('ADF'),
    'D': set('BFGHE'),
    'E': set('DH'),
    'F': set('BDG'),
    'G': set('DF'),
    'H': set('ADE'),
}
assert combinar_mapas(mapa1, mapa2) == mapa_combinado

