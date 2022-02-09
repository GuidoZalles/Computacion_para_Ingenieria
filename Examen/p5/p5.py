# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:27:48 2022

@author: User
"""

# Pregunta 5

# Crear un Menu que permita registrar estudiantes y sus notas en dos listas: lista_alumnos y lista_notas con los siguientes requerimientos.

list = []

salir = False

while salir !=True:
    print("-------------Menu-----------------")
    print("1.- Lista Alumnos")
    print("2.- Regitrar nombre y nota del Alumno")
    print("3.- Quitar nombre y nota del Alumno")
    print("4.- Salir")
    print("----------------------------------")
    
    option = int(input("Seleccione una opcion [1-2-3-4]:"))
    
    if option == 1:
        # muestro los alumnos
        print ("La lista de alumnos es: ")
        for alumno in list:
            print(alumno)
          
    elif option == 2:
        new_alumno = input("Ingrese nombre completo del alumno: ")
        nota_alumno = input("Ingrese nombre la NOTA del alumno: ")
        list.append(new_alumno)
        list.append(nota_alumno)
         
    elif option == 3:
        quitar_alumno = input("Ingrese nombre del que sedea quitar: ")
        list.remove(quitar_alumno)
        print("Se quito de la lista a: ",quitar_alumno)
    elif option == 4:
        print("Gracias por su preferencia, Adios..!!")
        salir = True
    else:
        print("Digite una opcion correcta")