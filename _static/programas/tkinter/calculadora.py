from Tkinter import *

w = Tk()
frame_botones = Frame(w)

# Se usa tres modelos:
# uno para guardar la operacion en curso (+, -, * o /),
# otro para guardar el valor anterior y
# otro para guardar el valor que se esta escribiendo.
v_operacion = StringVar()
v_operacion.set('+')
v_anterior = StringVar()
v_anterior.set('0')
v_actual = StringVar()
v_actual.set('')

visor = Entry(w, textvariable=v_actual, fg='green', bg='black', width=10,
                 font=('Courier', 20, 'bold'), justify='right')

def crear_agregador(i):
    def a():
        x = v_actual.get()
        y = x + str(i)
        v_actual.set(y)
    return a

def crear_operador(op):
    def o():
        v_operacion.set(op)
        v_anterior.set(v_actual.get())
        v_actual.set('')
    return o

# Esta es la funcion que falta escribir.
def calcular():
    pass

# Crear botones con los digitos y el punto.
for pos, d in enumerate('7894561230.'):
    b = Button(frame_botones, text=d, width=2, command=crear_agregador(d))
    b.grid(row=pos / 3, column=pos % 3)

# Crear botones con los operadores.
for pos, op in enumerate('/*-+'):
    b = Button(frame_botones, text=op, width=2, command=crear_operador(op))
    b.grid(row=pos, column=3)

# Crear boton "=".
b = Button(frame_botones, text='=', width=2, command=calcular)
b.grid(row=3, column=2)

visor.pack()
frame_botones.pack()

w.title('Calculadora')
w.mainloop()

