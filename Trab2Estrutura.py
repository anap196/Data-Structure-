# -*- coding: utf-8 -*-
"""
Created on Fri May 27 22:57:24 2022

@author: Ana Paula
"""
'EXERCÍCIO 1'

import array

class PilhaEmArray:
    def __init__(self, tamanho):
       self.items = array.array('u', [' ' for i in range(tamanho)])
       self.top = -1  #[len(self.items)]
       
    def Push(self, novoitem):
        if self.IsFull():
            raise Exception('Pilha Cheia')
            
        self.top += 1
        self.items[self.top] = novoitem
        
    def Pop(self):
        if self.IsEmpty():
            raise Exception('Pilha Vazia')
            
        item = self.items[self.top]
        self.top -= 1
        return item
    
    def Peek(self):
        if self.IsEmpty():
            raise Exception('Pilha vazia')
            
        return self.items[self.top]
    
    def IsEmpty(self):
        return self.top == -1
    
    def IsFull(self):
        return self.top == len(self.items) - 1
    
    def Count(self):
        return self.top + 1
    
    @staticmethod
    def ContarParenteses(self, string):
        self.contador = 0
        for s in string:
            if s == '(':
               self.items.Push(s)
               self.contador += 1
        else: 
            if s == ')':
                self.items.Pop()
                self.contador -= 1
        if self.contador == 0:
            return True
        else:
            return False
        
    
P1 = PilhaEmArray(5)
P1.Push('2')
P1.Push('9')
P1.Push('1')
P1.Pop()
P1.Peek()
P1.Count()
'###################################################################'
'EXERCÍCIO 2'

class Node:
    def __init__(self, newItem, nextNode):
        self.item = newItem
        self.next = nextNode
        
class PilhaEmLista:
    def __init__(self):
        self.top = None
        self.count = 0
        
    def Push(self, novoitem):
        NovoNo = Node(novoitem, self.top)
        self.top = NovoNo
        self.count += 1
        
    def Pop(self):
        if self.IsEmpty():
            raise Exception('Pilha Vazia')
        item = self.top.item
        self.top = self.top.next
        self.count -= 1
        return item
    
    def Peek(self):
        if self.IsEmpty():
            raise Exception('Pilha Vazia')
        return self.top.item
    
    def IsEmpty(self):
        return self.top == None
    
    def Count(self):
        return self.count
    
p3 =PilhaEmLista()
p3.Push(19)
p3.Push(5)
p3.Push(22)
print(p3.Pop())
print(p3.Peek())
print(p3.Count())

'#############################################################'
expressao = input('Digite uma expressão: ')
minhaexpressao = PilhaEmArray(30)
minhaexpressao.ContarParenteses()
               
        
        
            
        
           
           