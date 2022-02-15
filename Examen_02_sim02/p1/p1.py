# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 08:09:59 2022

@author: User
"""

from tkinter import *

ventana = Tk()
ventana.geometry("400x150")

ventana.title("Contador")
nombre = Label(ventana, text="Contador", bg='white', font=("Times",15,'bold'))
nombre.pack(side=TOP)
ventana.config(background='light blue')

textoDeEntrada=StringVar()
operador=''

texto = Entry(ventana,font=("Courier New",12,'bold'),textvar=textoDeEntrada,width=15,bd=5,bg='white')
texto.pack()

boton = Button(ventana,padx=5,pady=8,bd=8,bg='white',text="+",font=("Courier New",16,'bold'))
boton.pack()


ventana.mainloop()