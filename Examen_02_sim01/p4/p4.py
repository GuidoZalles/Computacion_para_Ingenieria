# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:25:58 2022

@author: User
"""

class person:
    
    def __init__(self, name, phone_number, email_addres, addres):
        self.name = name
        self.phone_number = phone_number
        self.email_addres = email_addres
        self.addres = addres
        
    def purchaseParkingPass():
        pass
    
class student(person):
    def __init__(self, name, phone_number, email_addres, student_number, average_mark,addres):
        person.__init__(self, name, phone_number, email_addres, addres)
        self.student_number = student_number
        self.average_mark = average_mark
       
        
    def isElegibleToEnroll():
        pass
    
    def getSeminarsTaken():
        pass
    
class professor(person):
    def __init__(self, name, phone_number, email_addres, salary, addres):
        person.__init__(self, name, phone_number, email_addres, addres)
        self.salary = salary
        
class addres:
    def __init__(self, street, city, state, postal_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        
    def validate():
        print("validado")
        
    def outputAsLabel():
        pass
    
direc = addres("santa Fe", "La Paz", "021","Bolivia")
    
profe = professor("Guido", "60584523", "zallesguido@gmail.com", "8000 bs", direc)



    
    
    
    
    
    
    
    