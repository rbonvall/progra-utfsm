>>> s = '{nombre} estudia en la {u}'
>>> s.format(nombre='Perico', u='UTFSM')
'Perico estudia en la UTFSM'
>>> s.format(nombre='Fulana', u='PUCV')
'Fulana estudia en la PUCV'
>>> s.format(u='UPLA', nombre='Yayita')
'Yayita estudia en la UPLA'
