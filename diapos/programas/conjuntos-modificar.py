>>> a = set()
>>> a.add(19)
>>> a.add(12)
>>> a.add(8)
>>> a.add(12)
>>> a
set([8, 12, 19])
>>> a.remove(19)
>>> a
set([8, 12])
>>> 12 in a
True

