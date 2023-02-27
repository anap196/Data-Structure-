# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:48:04 2021

@author: Ana Paula
"""

import math

class Ponto3D:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_z(self):
        return self.__z
    
    
    
    def DistanciaAte(self, ponto2):
        d1 = ponto2.get_x() - self.__x
        d2 = ponto2.get_y() - self.__y
        d3 = ponto2.get_z() - self.__z
        distancia = math.sqrt(d1*d1 + d2*d2 + d3*d3)
        return distancia

ponto1 = Ponto3D(1, 2, 3)
ponto2 = Ponto3D(4, 5, 6)
distancia = ponto1.DistanciaAte(ponto2)
print(distancia)


class VetorR3:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        
    def Modulo(self):
        nA = self.A * self.A
        nB = self.B * self.B
        nC = self.C * self.C
        norma = math.sqrt(nA + nB + nC)
        return norma

    def NormalizaVetor(self):
        mod = self.Modulo()
        self.A = self.A / mod
        self.B = self.B / mod
        self.C = self.C / mod


#vetor = VetorR3(4, 2, 1)
#print(vetor.Modulo())
#print(vetor.NormalizaVetor())


class Plano3D:
    def __init__(self, Ponto3D, VetorR3):
        self.ponto = self.ponto(Ponto3D)
        self.vetornormal = self.vetornormal(VetorR3)
        

# Professor vou entregar o que consegui fazer, confesso que não entendi
# muito bem a parte do plano 3D, desculpa não tirar dúvidas antes,
# acabou que me enrolei nessa semana. 
        
 