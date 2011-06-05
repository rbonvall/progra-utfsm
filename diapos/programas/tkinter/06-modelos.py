from Tkinter import *

w = Tk()

# crear variable, asignarle un valor inicial,
# y crear un controlador que modifica su valor
data = StringVar()
data.set('0')
def incrementar():
    valor = int(data.get())
    data.set(str(valor + 1))

# crear etiqueta, cuyo texto viene de la variable data
l = Label(w, textvariable=data)
l.pack()

# crear boton y asociarle el controlador creado mas arriba
b_inc = Button(w, text='+1', command=incrementar)
b_inc.pack()

# crear otro boton, y usar como controlador
# la funcion exit que provee Python
b_salir = Button(w, text='Salir', command=exit)
b_salir.pack()

w.mainloop()

