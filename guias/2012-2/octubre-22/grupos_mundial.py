from Tkinter import Tk, Button, Frame, Label, StringVar
from mundial import resultados_por_grupo
from torneos import ordenar_equipos, calcular_puntos, calcular_diferencia

w = Tk()      # ventana principal
fb = Frame(w) # panel de botones
ft = Frame(w) # panel con la tabla
fb.pack()     # empaquetar el primer panel
ft.pack()     # empaquetar el segundo panel

v = StringVar()
etiqueta = Label(ft, textvariable=v, fg='maroon')
etiqueta.grid(row=0, column=0)

for j, cabecera in enumerate(['Equipo', 'Pts', 'Dif'], 1):
    etiqueta = Label(ft, text=cabecera, fg='navy', anchor='-wee'[j])
    etiqueta.grid(row=0, column=j)

filas = []
for i in range(1, 5):
    celdas = {
      'n':   Label(ft, width=2, text=i),
      'eq':  Label(ft, width=16, anchor='w'),
      'pts': Label(ft, width=3,  anchor='e'),
      'dif': Label(ft, width=3,  anchor='e'),
    }
    for j, col in enumerate(['n', 'eq', 'pts', 'dif']):
        celdas[col].grid(row=i, column=j)
    filas.append(celdas)

def limpiar():
    for fila in filas:
        for c in ['eq', 'pts', 'dif']:
            fila[c].configure(text='')

def mostrar_grupo(g):
    print g
    v.set(g)
    p = resultados_por_grupo[g]
    equipos = ordenar_equipos(p)
    for i, equipo in enumerate(equipos):
        pts = calcular_puntos(p, equipo)
        dif = calcular_diferencia(p, equipo)
        filas[i]['eq'].configure(text=equipo)
        filas[i]['pts'].configure(text=pts)
        filas[i]['dif'].configure(text='{:+}'.format(dif))


botones = []
for grupo in 'ABCDEFGH':
    b = Button(fb, text=grupo,
                   command=lambda g=grupo: mostrar_grupo(g))
    b.pack(side='left')


w.mainloop()

