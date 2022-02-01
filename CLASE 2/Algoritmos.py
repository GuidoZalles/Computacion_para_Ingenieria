# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:11:25 2022

@author: User
"""

# contadore de 1 en 1

cont = 0
cont +=1 #--> cont= cont + 1

# 1.- contar numero del 1 al 10 y mostrar en la pantalla

while cont < 10:
    cont = cont + 1
    print (cont)
    
# 2.- Sumar los numeros del 1 al 10

# list = {1,2,3,.....10}
# range (1,n) --> [1,2,3,....,(n-1)]
sum=0

for num in range(1,11): # [1,2,3....]
    sum = sum + num
    
print (f'La suma total del 1 al 10 es: {sum}')

# 3.- Multiplicador

mult = 1
for num in range(1,11): # [1,2,3...10]
  mult=mult*num
print (f'la multiplicacion es: {mult}')

# 4.- mostrar los pares del 1 al 10

for num in range (1,11):
    if num % 2 == 0:
        print (" numero pares:", num)
        
# 5.- mostrar los numeros impares

for num in range (1,11):
    if num % 2 == 1:
        print (" los numeros impares son:", num)