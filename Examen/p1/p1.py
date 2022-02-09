# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:33:22 2022

@author: User
"""
# Pregunta 1

# Dada una cadena verificar que sea palindroma(es aquella palabra que se lee lo mismo al derecho y al reves e.j Ana)

def pal_palindroma(cadena):
    pos_iz = 0
    pos_der = len(cadena) - 1
    
    while pos_der >= pos_iz:
        if not cadena[pos_iz] == cadena[pos_der]:
            return("La palabra NO es palindroma.")
        pos_iz = pos_iz + 1
        pos_der = pos_der - 1
        
    return ("La palabra SI es palindroma.")

entrada = input("Ingrese una palabra: ")
salida = pal_palindroma(entrada)
print(salida)
