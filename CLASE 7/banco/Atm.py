# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 07:50:30 2022

@author: User
"""

class Atm:
    
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
    def showATM(self):
        print("cajero ubicadoen,",self.ubicacion)