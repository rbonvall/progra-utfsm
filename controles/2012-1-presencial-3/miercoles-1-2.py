'''
# CASO
>>> probabilidad_tsunami([240, 255, 280, 265], 247)
75.0
>>> hay_que_evacuar([240, 255, 280, 265])
False
# FIN CASO
'''

def probabilidad_tsunami(mareas, umbral):
    c = 0
    for x in mareas:
        if x > umbral:
            c += 1
    return 100.0 * c / len(mareas)

def hay_que_evacuar(mareas):
    return probabilidad_tsunami(mareas, 270) > 32

