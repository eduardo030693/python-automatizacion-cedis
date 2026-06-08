"""
── Ejercicio 6: Interfaz de escritorio básica con Tkinter ──
Tema: Tkinter - GUI   |   Nivel 6/10  ★★★★★☆☆☆☆☆
Tu programa necesita una ventana para que cualquier persona pueda usarlo sin saber Python.
Tkinter es la librería estándar de Python para interfaces gráficas.
Instrucciones:
Crea una ventana con el título 'Comparador de Inventario'.
Agrega un botón 'Cargar Archivo'.
Al presionar el botón, abre un explorador de archivos con filedialog.
Muestra la ruta del archivo seleccionado en un Label.
"""

import tkinter as tk
from tkinter import filedialog

ventana1 = tk.Tk()
ventana1.title('Comparador de Inventario')
ventana1.geometry('500x200')

texto = tk.StringVar()
texto.set('Ningun archivo seleccionado')

def llamar():
    ruta = filedialog.askopenfilename()
    if ruta:
        texto.set(ruta)

tk.Button(ventana1, text='Cargar Archivo', command=llamar).pack(pady=20)
lbl = tk.Label(ventana1, textvariable=texto, wraplength=480)
lbl.pack()

ventana1.mainloop()
