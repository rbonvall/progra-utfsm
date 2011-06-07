from Tkinter import *

w = Tk()
botones = Frame(w)

b_piedra = Button(botones, text='Piedra')
b_papel  = Button(botones, text='Papel')
b_tijera = Button(botones, text='Tijera')

b_piedra.pack(side='left')
b_papel.pack(side='left')
b_tijera.pack(side='left')

l_marcador = Label(text='4-1', font=('Arial', 20))
l_resultado = Label(text='El computador eligio tijera')

l_marcador.pack(side='top')
l_resultado.pack(side='top')
botones.pack(side='top')

w.title('Cachipun')
w.mainloop()

