>>> a = array([5.0, 7.0, 8.0])
>>> b = array([5.5, 6.5, 4.1])
>>> c = array([9.0, 9.2, 9.4])

>>> a < b
array([ True, False, False], dtype=bool)

>>> a < c
array([ True,  True,  True], dtype=bool)

>>> all(a < c)
True

>>> any(b > 6)
True

