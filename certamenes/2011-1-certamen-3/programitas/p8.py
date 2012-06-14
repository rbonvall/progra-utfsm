from Tkinter import *
v = Tk()
for i in range(4):
    for j in range(4):
        if i == j:
            val = '1'
        else:
            val = '-'
        l = Label(v, text=val)
        l.grid(row=i, column=j)
v.mainloop()
