# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:55:16 2022

@author: User
"""

from tkinter import *
from tkinter import ttk
def selectLanguage(event):
    print("selectec!!!")
    selected = comboBox_languages.get()
    print("the selected", selected)
    label_resul.config(text=f"Language: {selected}")


ventana=Tk()
ventana.geometry("400x400")
#crear componentes
label_resul=Label(ventana, text="<<Result>>")
comboBox_languages= ttk.Combobox(ventana, values=['Java', 'python','C+'])

comboBox_languages.place(x=20,y=20)
label_resul.place(y=200,x=20)

comboBox_languages.bind("<<ComboboxSelected>>",selectLanguage)

ventana.mainloop()
