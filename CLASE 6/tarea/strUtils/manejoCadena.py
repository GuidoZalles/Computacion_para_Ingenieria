# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 05:48:22 2022

@author: User
"""

def contar_espacio(cadena):
    espacio = 0
    
    for i in cadena:
        if i == " ":
            espacio = espacio + 1
        
    return espacio

palabra = "A seguir aelante bro.. que los dias no paran"
print("la cantidad de espacios del parrafo es: ",contar_espacio(palabra))