# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:48:31 2022

@author: User
"""

# Pregunta 2
# Dada la Lista [12,1, 3, 5 , 15, 24] separar en dos listas de pares e impares

list = [12,1, 3, 5 , 15, 24]
listaPares=[]
listaImpares=[]
for num in list:
    if num % 2 == 0:
        # es par
        listaPares.append(num)
    else:
        listaImpares.append(num)

print(list)
print(listaPares)
print(listaImpares)