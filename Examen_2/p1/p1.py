# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:25:25 2022

@author: User
"""
# PPREGUNTA 1
# Crear un programar GUI que verifique que una palabra es palindroma(palindroma es 
# aquella palabra que es lo mismo de der a izq o viceversa

from tkinter import *

def invertir(cadena):
    res = ''
    index = len(palabra)
    while index >0:
        ultimo_caracter = palabra[index-1]
        res = res + ultimo_caracter
        index=index-1
    return res
    label_res.config(text=f"la palabra es: {res}")

ventana = Tk()
ventana.geometry("350x200")
ventana.title("PREGUNTA 1")
ventana.config(background='dark gray')

label_1 = Label(ventana, text="Enter a Word:")
input_text = Entry(ventana, bg="powder blue")
label_res=Label(ventana, text="<<result>>")
boton = Button(ventana, text="Validate", command=lambda: invertir())

label_1.place(x=20,y=10)
input_text.place(x=150,y=10)
label_res.place(x=180,y=50)
boton.place(x=180,y=100)               

ventana.mainloop()