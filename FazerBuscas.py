# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 17:09:39 2022

@author: Ana Paula
"""

import numpy
import random
import datetime

class MyArrayList:
    def __init__(self, maxsize):
        self.items = numpy.zeros((maxsize,), dtype=int)
        self.count = 0
        
    def AddLast(self, newItem):
        if (self.IsFull()):
            raise Exception('Lista Cheia')
        self.items[self.count] = newItem
        self.count += 1
        
    def IsFull(self):
        return self.count == len(self.items)
    
    def LinearSearch_SortedArray(self, key):
        n = len(self.items)
        k = 0
        while (k < n and self.items[k] < key):
            k += 1
            
        if (k < n and self.items[k] == key):
            return True
        else:
            return False
        
    def BinarySearch(self, key):
        min = 0
        max = len(self.items) - 1
        while min <= max:
            mid = (min + max) // 2
            if (key == self.items[mid]):
                return True
            elif (key < self.items[mid]):
                max = mid - 1
            else:
                min = mid + 1
        return False
    
    def Display(self):
        j = len(self.items)
        for i in range(0, j):
            print(self.items[i])
            
    def SortList(self):
        self.items.sort()
            
'***********************************************************'    
#Programa Principal
# Usamos N == 1.000,50.000,100.000,500.000,1.000.000,100.000.000
N = 1000
MAX = 100000
lista1 = MyArrayList(N)
print('Preenchendo o array com N elementos aleatórios...')
for i in range(0, N):
    x = random.randint(0, MAX)
    lista1.AddLast(x)
    
print('Ordenando...')
lista1.SortList()
'*********************************************************'
print('Efetuando 200 buscas...')
start = datetime.datetime.now()
for i in range(0, 200):
    Max = random.randint(0, 2*MAX)
    lista1.BinarySearch(Max)
    #lista1.LinearSearch_SortedArray(Max)
end = datetime.datetime.now()
delta = end - start
print('Tempo gasto nas buscas: ', delta)

'************************************************************'






        
    
    
