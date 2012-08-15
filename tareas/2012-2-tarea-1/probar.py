#!/usr/bin/env python

# Este es el programa que se va a probar

NOMBRE_PROGRAMA = 't1-normal.py'
#NOMBRE_PROGRAMA = 't1-dificil.py'

# No modifique nada de aqui para abajo!

import subprocess
from sys import argv
from glob import glob

if len(argv) > 1:
    ejemplos = argv[1:]
else:
    ejemplos = sorted(glob('ejemplos/*'))

for ejemplo in ejemplos:
    print '===', ejemplo, '==='
    subprocess.call(['python', NOMBRE_PROGRAMA], stdin=open(ejemplo))

