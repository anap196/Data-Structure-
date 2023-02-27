# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:03:39 2022

@author: Ana Paula
"""

import array

class StackInArray:
    def __init__(self, size):
        self.items = array.array('u',[' ' for i in range(size)])
        self.top = len(self.items)
        
    def Push(self, newItem):
        if self.IsFull():
            raise Exception('Pilha Cheia')
        self.top = len(self.items) - 1
        self.items[self.top] = newItem
        
    def Pop(self):
        if self.IsEmpty():
            raise Exception('Pilha Vazia')
        item = self.items[self.top]
        self.top += 1
        return item
    
    def IsEmpty(self):
        return self.top == len(self.items)
    
    def IsFull(self):
        return self.top == 0
    
    def Display(self):
        aux = self.top
        for i in range(len(self.items), 0):
             aux -= 1
        print(aux)
        
        
        
    