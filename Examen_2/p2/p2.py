# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:42:23 2022

@author: User
"""

from tkinter import *

ventana = Tk()
ventana.geometry("500x100")
ventana.title("PREGUNTA 2")
ventana.config(background='dark gray')

label_1 = Label(ventana, text="Contador:")
input_text = Entry(ventana, bg="powder blue")
boton_1 = Button(ventana, text="Count Up")
boton_2 = Button(ventana, text="Count Down")
boton_3 = Button(ventana, text="Reset")

label_1.place(x=10,y=20)
input_text.place(x=75,y=20)
boton_1.place(x=210,y=20)
boton_2.place(x=280,y=20)
boton_3.place(x=370,y=20)
                 

ventana.mainloop()