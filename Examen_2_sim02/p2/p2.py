# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 08:32:31 2022

@author: User
"""

# Crear un programa GUI que permita invertir una cadena ingresada por el usario

from tkinter import *

def invertirCadena(cadena):
    palabra_invertida = ""
    for char in cadena:
        palabra_invertida = char + palabra_invertida
    return palabra_invertida
        
ventana = Tk()
ventana.geometry("400x200") #para aumentar el tama;o de la ventana

l1 = Label(text="INGRESE LA PALABRA QUE DESEA INVERTIR", bg="dark gray", font=("Arial", 10)) #altura de texto a mostrarse en la ventana
l1.pack()

entrada = Entry(width=50, bg="powder blue")
entrada.pack()

def mostrarInvertido(palabra):
    palabra_invertida = invertirCadena(palabra)
    l3 = Label(text=palabra_invertida, font=("Arial",15))
    l3.pack()

b1 = Button(text="Invertir", width=15, height=3, font=("Arial",15), command=lambda: mostrarInvertido(entrada.get()))
b1.pack()  

ventana.mainloop()
