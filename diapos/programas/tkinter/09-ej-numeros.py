from Tkinter import *

N = 12

w = Tk()

# crear N variables y N entradas
data_variables = []
entries = []
for i in range(N):
    v = StringVar()
    e = Entry(w, textvariable=v)
    data_variables.append(v)
    entries.append(e)

# crear variables y etiquetas para mostrar el reporte
var_suma = StringVar()
l_suma = Label(w, textvariable=var_suma)
var_promedio = StringVar()
l_promedio = Label(w, textvariable=var_promedio)
var_minimo = StringVar()
l_minimo = Label(w, textvariable=var_minimo)
var_maximo = StringVar()
l_maximo = Label(w, textvariable=var_maximo)

# crear controlador para calcular y actualizar las etiquetas
def reportar():
    valores = []
    for var in data_variables:
        valores.append(float(var.get()))

    var_suma.set('Suma: {0}'.format(sum(valores)))
    var_promedio.set('Promedio: {0}'.format(sum(valores) / len(valores)))
    var_minimo.set('Minimo: {0}'.format(min(valores)))
    var_maximo.set('Maximo: {0}'.format(max(valores)))

# crear el boton y asociarlo a la funcion que reporta los resultados
b = Button(w, text='Calcular', command=reportar)

# agregar las entradas, el boton y las etiquetas a la ventana
for e in entries:
    e.pack()
b.pack()
for l in [l_suma, l_promedio, l_maximo, l_minimo]:
    l.pack()

# crear la ventana
w.title('Numeros')
w.mainloop()

