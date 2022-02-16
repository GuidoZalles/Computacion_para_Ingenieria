# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:33:48 2022

@author: User
"""

from tkinter import *

def sumar():
    op1=int(input_op1.get())
    op2=int(input_op2.get())
    sumar=op1+op2
    print("la suma es:", sumar)
    label_res.config(text=f"the sum is: {op1} + {op2} = {sumar}")

ventana = Tk()
ventana.geometry("400x400")
label_op1=Label(ventana, text="Enter the value of M:")
label_op2=Label(ventana, text="Enter the value of N:")
label_res=Label(ventana, text="<<RESULT>>")

input_op1 = Entry(ventana)
input_op2 = Entry(ventana)

buton_res = Button(ventana, text="Validate", command=lambda: sumar())

label_op1.place(x=10,y=10)
input_op1.place(x=200,y=10)

label_op2.place(x=10,y=50)
input_op2.place(x=200,y=50)

label_res.place(x=210,y=90)
buton_res.place(x=210,y=110)

ventana.mainloop()


