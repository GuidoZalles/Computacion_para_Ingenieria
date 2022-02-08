# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:01:47 2022

@author: User
"""

# Pregunta 1
# Pedir un parrafo al usuario y contar los espacios en el parrafo


def contar_espacio(cadena):
    espacio = 0
    
    for i in cadena:
        if i == " ":
            espacio = espacio + 1
        
    return espacio

palabra = input("Ingrese un frase: ")
print("la cantidad de espacios del parrafo es: ",contar_espacio(palabra))
        
    
    