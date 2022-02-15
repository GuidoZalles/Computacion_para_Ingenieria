# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 03:39:55 2022

@author: User
"""

# TAREA DE INVESTIGACION
# Como abrir ventana
"""
from tkinter import *
window = Tk()
window.title("1")

window.mainloop()




# Como crear botones 

from tkinter import *
def hola():
    print("Hola señores")
    
root = Tk()

Button(root, text="Clic Aqui", command=hola).pack()

root.mainloop()

"""

# Como crear Label

from tkinter import *
raiz = Tk()
mi_Frame = Frame()
mi_Frame.pack()
mi_Label = Label(mi_Frame, text="Es una etiqueta")
mi_Label.pack()
raiz.mainloop()

from tkinter import *
root = Tk()

Label = Label(root,text="Hello world")
Label.pack()

root.mainloop