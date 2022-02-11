# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:01:06 2022

@author: User
"""

# imprtr modulo

import aritmetica
print(aritmetica.sumar(1, 1))
print(aritmetica.div(1, 1))
print(aritmetica.restar(1, 1))
print('')
# otra manera de importar

from aritmetica import sumar, div

print(sumar(1,1))
print(div(1,1))
print('')
# importar todas la funcones de la libreria

from aritmetica import *

print(sumar(1,1))
print(restar(2, 3))
print(mult(2, 3))
print(div(5, 2))
