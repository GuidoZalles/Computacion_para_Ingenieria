# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:51:05 2022

@author: User
"""
# Pregunta 3

from tkinter import *

def sumar():
    op1=int(input_text_1.get())
    op2=int(input_text_2.get())
    suma= op1 + op2
    print("la suma es ", suma)
    resp.config(text=f"{suma}")
    
def restar():
    op1=int(input_text_1.get())
    op2=int(input_text_2.get())
    resta= op1 - op2
    print("la resta es ", resta)
    resp.config(text=f"{resta}")   
    
def multiplicar():
    op1=int(input_text_1.get())
    op2=int(input_text_2.get())
    mult= op1 * op2
    print("la multiplicacio  es ", mult)
    resp.config(text=f"{mult}") 

ventana = Tk()
ventana.geometry("250x350")
ventana.title("PREGUNTA 1")
ventana.config(background='dark gray')

label_1 = Label(ventana, text="Numero 1")
input_text_1 = Entry(ventana, bg="powder blue")
label_2 = Label(ventana, text="Numero 2")
input_text_2 = Entry(ventana, bg="powder blue")

label_3 = Label(ventana, text="Resultado")
resp = Label(ventana, bg="white")

boton1 = Button(ventana, text="Sumar", command=lambda: sumar())
boton2 = Button(ventana, text="Restar",command=lambda: restar())
boton3 = Button(ventana, text="Multiplicar", command=lambda: multiplicar())

label_1.place(x=100,y=10)
input_text_1.place(x=70,y=50)
label_2.place(x=100,y=100)
input_text_2.place(x=70,y=150)
label_3.place(x=100,y=200)
resp.place(x=120,y=250)
boton1.place(x=10,y=280)
boton2.place(x=80,y=280)
boton3.place(x=150,y=280)

ventana.mainloop()