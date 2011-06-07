from Tkinter import *

w = Tk()

for i in range(1, 11):
    for j in range(1, 11):
        num = str(i * j)
        l = Label(w, text=num)
        l.grid(row=i, column=j)

w.title('Tabla')
w.mainloop()


