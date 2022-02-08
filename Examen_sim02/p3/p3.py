# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:59:46 2022

@author: User
"""
# Pregunta 3
# crear una funcion que pueda contar el numero de palabras

texto = input("Ingrese un parrafo: ")
palabra = texto.split()
i = 0
while i < len(palabra):
    i = i + 1
print("la cantidad de palabras en el parrafo es: ", i)