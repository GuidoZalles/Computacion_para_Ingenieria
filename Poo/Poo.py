# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:45:22 2022

@author: User
"""
# ejercicio de clase

class Figura:
    def __init__(self, area_, perimetro_, color):
        self.perimetro = perimetro_
        self.area = area_
        # hasta ahi definimos el constructor
        
        @property()
        def getPerimetro(self):
            return self.perimetro
        
        def getArea(self):
            return self.area
        
        def setPerimetro(self, nuevo_per):
            self._perimetro = nuevo_per
            
        def setArea(self, nueva_area):
            self._area = nueva_area
            
        def dibujar(self):
            pass

class Circulo(Figura):
    def __init__(self, perimetro_, area_, radio, color):
        self.perimetro = perimetro_
        self.area = area_
        self.radio = radio
        self.color = color
        

    
    def cambiarColor():
        pass
    
    def getRadio(self):
        return self.radio
    
    def setRadio(self, nuevo_radio):
        self.radio = nuevo_radio
        
    def getColor(self):
        return self.color
    
    def setColor(self, nuevoColor):
        self.color = nuevoColor
        

     
# cuadrado        
class Cuadrado(Figura):
    def __init__(self, perimetro_, area_, lado, color):
        self.perimetro = perimetro_
        self.area = area_
        self.radio = lado
        self.color = color
        
    
    
    def getLado(self):
        return self.lado
    
    def setLado(self, nuevo_lado):
        self.lado = nuevo_lado
        
# RECTANGULO

class Rectangulo(Figura):
    def __init__(self, perimetro_, area_, base, altura, color):
        self.perimetro = perimetro_
        self.area = area_
        self.base = base
        self.altura = altura
        self.color = color
        
    
    
    def getBase(self):
        return self.base
    
    def setBase(self, nuevo_base):
        self.base = nuevo_base
        
    def getAltura(self):
       return self.altura
   
    def setAltura(self, nuevo_altura):
       self.altura = nuevo_altura 
       
class Imprensora:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
        def imprimir(Figura):
            print("Pude dibujar tu objeto -->  O")
            pass
        
cirk = Circulo(10, 1, 34, "azul")
print(cirk.color)

cirk.setColor("rojo")
print(cirk.getColor())
