# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:37:39 2022

@author: Ana Paula
"""

class ContaBancaria:
    def __init__(self, conta, agencia, titular):
        self.__conta = conta
        self.__agencia = agencia
        self.__titular = titular
        self.__saldo = 0
        
    def Depositar(self, valor):
        self.__saldo += valor
#        return self.__saldo

    def Sacar(self, debito):
        self.__saldo -= debito
        return self.__saldo
    
    def GetSaldo(self):
        return self.__saldo
    
    def Mostrar(self):
        show = 'Conta %s, agencia %s, titular %s com saldo de %d R$.'%(
            self.__conta, self.__agencia, self.__titular, self.__saldo)
        print(show)
        
# Exemplos de duas contas bancárias!!!
conta1 = ContaBancaria(20061078, 3342, 'Ana')
conta2 = ContaBancaria(10056089, 4456, 'Wesley')

conta1.Depositar(100)
conta1.Depositar(50)
conta1.Sacar(30)
conta1.GetSaldo()
conta1.Mostrar()
conta2.Depositar(200)
conta2.Sacar(20)
conta2.GetSaldo()
conta2.Mostrar()

'##################################################################'
import math

class Vetor:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        
    def ModuloVetor(self):
        self.modulo = math.sqrt((self.A ** self.A) + (self.B ** self.B) + (self.C ** self.C))
        return self.modulo
    
    def NormalizarVetor(self):
        self.normaA = (self.A / self.modulo)
        self.normaB = (self.B / self.modulo)
        self.normaC = (self.C / self.modulo)
        return self.normaA, self.normaB, self.normaC
    
# Exemplos de três vetores!!!
vet1 = Vetor(1, 1, 1)
vet2 = Vetor(1, 2, 3)
vet3 = Vetor(3, 2, 2)
print(vet1.ModuloVetor())
print(vet1.NormalizarVetor())
print(vet2.ModuloVetor())
print(vet2.NormalizarVetor())
print(vet3.ModuloVetor())
print(vet3.NormalizarVetor())

'###################################################################'
class PontoGeometrico:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_z(self):
        return self.__y
    
    def DistanciaAte(self, p2):
        dx = p2.get_x() - self.__x
        dy = p2.get_y() - self.__y
        dz = p2.get_z() - self.__z
        dist = math.sqrt(dx**dx + dy**dy + dz**dz)
        return dist
        
p1 = PontoGeometrico(1, 2, 3)
p2 = PontoGeometrico(4, 5, 6)
print(p1.DistanciaAte(p2))
print(p1.get_x())
print(p2.get_y())
print(p2.get_x())

    
    
