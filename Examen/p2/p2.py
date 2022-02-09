# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:21:02 2022

@author: User
"""

# pregunta 2

# Dada la lista [10,20,30,10,5, 1, 3, 5, 4] separar en dos listas una lista debe contener solo los pares y la segunda lista solo debe contener los impares

list = [10,20,30,10,5, 1, 3, 5, 4]
pares = []
impares = []

for num in list:
    if num % 2 == 0:
        # es par
        pares.append(num)
    else:
        impares.append(num)

print(list)
print(pares)
print(impares)
