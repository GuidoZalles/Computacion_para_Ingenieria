# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:31:56 2022

@author: User
"""
# contador de numeros primos, se puede ingresas n cantidad de numeros.

n = int(input("Ingrese u numero entero positivo: "))
if n > 0:
    for i in range(2,n):
        creciente = 2
        esPrimo = True
        
        while esPrimo and creciente < i:
            if i % creciente == 0:
                esPrimo = False
            else:
                creciente += 1
        if esPrimo:
           print(i, "el numero ingresado es primo:")

