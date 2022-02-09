# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:06:29 2022

@author: User
"""

# pregunta 4
# Dado el archivo input.txt que contine la informacion de estudiantes y sus notas generar un archivo de salida output.csv que contenga la informacion de alumno separados por , (comas)

archivo = open ('input.txt.txt' , 'r' )
 for line in arhivo.readlines():
     lista_sin_espacios = line.split()
     texto_con_comas = ", ".join(lista_sin_espacios)
     archivo_csv = open('output.csv' , 'w+')
     archivo_csv.write(texto_con_comas + "\n")
     archivo_csv.close()
archivo.close()
