# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 04:09:20 2022

@author: User
"""

from tkinter import *

tk = Tk()
tk.geometry("354x460")
tk.title("CALCULADORA")
nombre = Label(tk, text="CALCULADORA", bg='dark gray', font=("Times",30,'bold'))
nombre.pack(side=TOP)
tk.config(background='dark gray')

textoDeEntrada=StringVar()
operador=''

def presionarBoton(numero):
    global operador
    operador = operador + str(numero)
    textoDeEntrada.set(operador)
    
def botonDeOperacion():
    global operador
    suma = str(eval(operador))
    textoDeEntrada.set(suma)
    operador = ''
    
def botonDeOperacion():
    global operador
    resta = str(eval(operador))
    textoDeEntrada.set(resta)
    operador = ''

def botonDeOperacion():
    global operador
    multiplicacion = str(eval(operador))
    textoDeEntrada.set(multiplicacion)
    operador = ''
    
def botonDeOperacion():
    global operador
    division = str(eval(operador))
    textoDeEntrada.set(division)
    operador = ''
    
def botonDeBorrar():
    textoDeEntrada.set('')
    
texto = Entry(tk,font=("Courier New",12,'bold'),textvar=textoDeEntrada,width=25,bd=5,bg='powder blue')
texto.pack()

boton1 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(1),text="1",font=("Courier New",16,'bold'))
boton1.place(x=10,y=100)

boton2 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(2),text="2",font=("Courier New",16,'bold'))
boton2.place(x=10,y=170)

boton3 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(3),text="3",font=("Courier New",16,'bold'))
boton3.place(x=10,y=240)

boton4 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(4),text="4",font=("Courier New",16,'bold'))
boton4.place(x=75,y=100)

boton5 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(5),text="5",font=("Courier New",16,'bold'))
boton5.place(x=75,y=170)

boton6 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(6),text="6",font=("Courier New",16,'bold'))
boton6.place(x=75,y=240)

boton7 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(7),text="7",font=("Courier New",16,'bold'))
boton7.place(x=140,y=100)

boton8 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(8),text="8",font=("Courier New",16,'bold'))
boton8.place(x=140,y=170)

boton9 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(9),text="9",font=("Courier New",16,'bold'))
boton9.place(x=140,y=240)

boton10 = Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:presionarBoton(0),text="0",font=("Courier New",16,'bold'))
boton10.place(x=10,y=310)


botonDeSumar = Button(tk,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:presionarBoton("+"),font=("Courier New",16,'bold'))
botonDeSumar.place(x=205,y=100)

botonDeRestar = Button(tk,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:presionarBoton("-"),font=("Courier New",16,'bold'))
botonDeRestar.place(x=205,y=170)

botonDeMultiplicar = Button(tk,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:presionarBoton("*"),font=("Courier New",16,'bold'))
botonDeMultiplicar.place(x=205,y=240)

botonDeDividir = Button(tk,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:presionarBoton("/"),font=("Courier New",16,'bold'))
botonDeDividir.place(x=205,y=310)

botonDeBorrar = Button(tk,padx=14,pady=119,bd=4,bg='orange',text="C",command=botonDeBorrar,font=("Courier New",16,'bold'))
botonDeBorrar.place(x=270,y=100)

butequal = Button(tk,padx=151,pady=14,bd=4,bg='white',command=botonDeOperacion,text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)

tk.mainloop()
