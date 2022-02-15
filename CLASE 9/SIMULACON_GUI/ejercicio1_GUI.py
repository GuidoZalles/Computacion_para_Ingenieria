# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:14:55 2022

@author: User
"""

# 1.- Pedir al usuario una palabra y mostrar la cadena invertida usar tkinter GUI

from tkinter import *

def invertirCadena(cadena):
    palabra_invertida = ""
    for char in cadena:
        palabra_invertida = char + palabra_invertida
    return palabra_invertida
        
ventana = Tk()
ventana.geometry("500x200") #para aumentar el tama;o de la ventana

l1 = Label(text="Ingrese la palabra que deseas volcar:", font=("Arial", 10)) #altura de texto a mostrarse en la ventana
l1.pack()

entrada = Entry(width=50)
entrada.pack()

def mostrarInvertido(palabra):
    palabra_invertida = invertirCadena(palabra)
    l3 = Label(text=palabra_invertida, font=("Arial",15))
    l3.pack()

b1 = Button(text="Invertir", width=15, height=3, font=("Arial",15), command=lambda: mostrarInvertido(entrada.get()))
b1.pack()  

ventana.mainloop()

