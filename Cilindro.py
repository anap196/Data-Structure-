# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:41:26 2022

@author: Ana Paula
"""
import math

class Cilindro:
    def __init__(self, raio, altura):
        self.__raio = raio
        self.__altura = altura
        
        
    def Volume(self):
        volume = math.pi*(((self.__raio * self.__raio))*self.__altura)
        return volume
        
    def AreaLateral(self):
        Al= 2*math.pi*(self.__raio)*(self.__altura)
        return Al
    
    def GetRaio(self):
        return self.__raio
    
    def GetAltura(self):
        return self.__altura
    
'*****************************************************************'
#Programa principal    
cilindro1 = Cilindro(5, 3)
print(cilindro1.Volume())
print(cilindro1.AreaLateral())
print(cilindro1.GetRaio())
print(cilindro1.GetAltura())
cilindro2 = Cilindro(4, 2)
print(cilindro2.Volume())
print(cilindro2.AreaLateral())
print(cilindro2.GetRaio())
print(cilindro2.GetAltura())
