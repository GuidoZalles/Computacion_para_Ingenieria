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
    print(cont)
    
  
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
print()
for num in range (1,11):
    if num % 2 == 1:
        print (" los numeros impares son:", num)      

## Ejercicio de clase 01
print()
print("Ejercicio de clase # 1")
print()
print("Contar la cantitatd de elementos de:[1,3,4,66,55,4]")

list = [1,3,4,66,55,4]
cont = 0

for num in list:
    cont = cont + 1
print(f'- La cantidad de digitos es: {cont}')

print()

print("lista de los numeros impares y pares es:[1,3,4,66,55,4]")

list = [1,3,4,66,55,4]

for num in list:
    if num % 2 == 1:
        print ("- Los numeros impares son:", num)
print()
for num in list:
    if num % 2 == 0:
        print ("- Los numeros pares son:", num)
# Ejercicio de clase 02

print()
print("Ejercicio de clase # 2")
print()
print("Mostrar la suma y la multiplicacion de los numeros mostrados es:[1,3,4,66,55,4]")

list = [1,3,4,66,55,4]
sum = 0

for num in list:
    sum = sum + num
print ("- La suma es =", sum)

mult = 1

for num in list:
    mult = mult*num
print("- La multiplicacion es =", mult)
    


