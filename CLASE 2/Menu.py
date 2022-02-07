# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:56:02 2022

@author: User
"""

"""
Crear un programa que registre nuevos alumnos,liste los actuales alumno borre 
un alumno, el alumno tiene nombre y apellido.
"""
# Crear una lista

list = []

salir = False

while salir !=True:
    print("-------------Menu-----------------")
    print("1.- Lista Alumnos")
    print("2.- Regitrar Alumno")
    # pedir un nombre a borrar
    print("3.- Quitar Alumno")
    print("4.- Salir")
    print("-----------------------------------")
    
    
    option = int(input("Seleccione una opcio [1-2-3-4]: "))
    
    ## opcion 1 listar alumnos
    if option == 1:
        # muestro los alumnos
        print ("La lista de alumnos es: ")
        for alumno in list:
            print (alumno)  
            
    # opcion 2 agregar otro alumno
    elif option == 2:
        new_alumno = input("Ingrese nombre completo del alumno: ")
        list.append(new_alumno)
    elif option == 3:
        quitar_alumno = input("Ingrese nombre del que sedea quitar: ")
        list.remove(quitar_alumno)
        print("Se quito de la lista a: ",quitar_alumno)
    elif option == 4:
        print("Gracias por su preferencia, Adios..!!")
        salir = True
    else:
        print("Digite una opcion correcta")
    
        