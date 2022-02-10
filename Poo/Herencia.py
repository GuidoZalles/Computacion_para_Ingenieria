# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:54:57 2022

@author: User
"""
# EJERCICIO DE CLASE
# HERENCIA...
class Animal:
    # defnir el metodo constructor
    def __init__(self, especie, edad):
        # definimos atributos
        self.especie=especie
        self.edad=edad
    # definimos
    def hablar(self):
        pass
    def moverse(self):
        pass
    def describirse(self):
        print(f"Soy animal {self.especie} de edad {self.edad}")
        
# Implementar clases hijas

class Perro(Animal):
    
    # definir su metodo constructor
    def __init__(self, especie, edad):
        self.especie=especie
        self.edad=edad
        
    #sobre escribir metodo
    def hablar(self):
        print("hua hua !!!")
    # sobre escribir el metodo caminar
    def moverse(self):
        print("moverme en 4 patas")
    def moverseCoordenadas(self, x, y):
        print(f"moverse de la posicion {x}, {y}")

        
# implementacion de la clase
class Vaca(Animal):
    
    # definir metodo constructor
    def __init__(self, especie, edad):
        self.especie=especie
        self.edad=edad
    
    def hablar(self):
        print("Muuuuuuuu")
    def moverse(self):
        print("moverse en 4 patas")
        # sobre escribir metodo
    def describirse(self):
        print(f"Soy una vaca de especie {self.especie} con edad {self.edad}")
    
# -------------- utilizar as clases, clientes -----------
print("PERRO")
perro = Perro("mamifero", 5)
perro.hablar()
perro.moverse()
perro.moverseCoordenadas(10, 10)
perro.describirse()
print(" ")
# crear vaca
print("VACA")
vaca = Vaca("mamifero", 3)
vaca.hablar()
vaca.moverse()
vaca.describirse()