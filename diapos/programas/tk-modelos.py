from Tkinter import *

w = Tk()

l1 = Label(w, text='Texto estatico')
l1.pack()

v = StringVar()
l2 = Label(w, textvariable=v)
l2.pack()

v.set('Texto variable')
s = v.get()

w.mainloop()
