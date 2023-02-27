# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:59:20 2022

@author: Ana Paula
"""

import array

class Deque:
    def __init__(self, max):
        self.array = array.array('i', [0 for i in range(max)])
        self.inicio = 0
        self.final = -1
        self.count = 0
    
    def AddRear(self, newItem):
        if self.IsFull():
            raise Exception('Fila Cheia')
            
        self.final = (self.final + 1) % len(self.array)
        self.array[self.final] = newItem
        self.count += 1
        
    def RemoveRear(self):
        if self.IsEmpty():
           raise Exception('Fila Vazia')
            
        item = self.array[self.final]
        self.final = (self.final - 1) % len(self.array)
        self.count -= 1
        return item
    
    def AddFront(self, newItem):
        if self.IsFull():
            raise Exception('Fila Cheia')
        
        self.inicio = (self.inicio - 1) % len(self.array)
        self.array[self.inicio] = newItem
        self.count += 1
    
    def RemoveFront(self):
        if self.IsEmpty():
            raise Exception('Fila Vazia')
            
        it = self.array[self.inicio]
        self.inicio = (self.inicio + 1) % len(self.array)
        self.count -= 1
        return it
    
    def IsFull(self):
        return self.count == len(self.array)
    
    def IsEmpty(self):
        return self.count == 0
    
    def Count(self):
        return self.count
        
'*********************************************************************'
#Exemplo:
meudeque = Deque(20)
meudeque.AddRear(7)
meudeque.AddRear(9)
meudeque.AddFront(15)
meudeque.AddFront(4)
meudeque.AddFront(22)
print(meudeque.RemoveRear())
print(meudeque.RemoveFront())
print(meudeque.IsFull())
print(meudeque.IsEmpty())
print(meudeque.Count())

'*************************************************************************'
class Node:
  def __init__(self, newItem, nextNode):
    self.item = newItem
    self.next = nextNode


class QueueInList:
  def __init__(self):
    self.inicio = None
    self.final = None
    self.count = 0

  
  def Enqueue(self, newItem):
    newNode = Node(newItem, None)
    
    if self.final != None:
      self.final.next = newNode
    else:
      self.inicio = newNode

    self.final = newNode
    self.count += 1

  def Dequeue(self):
    if self.IsEmpty():
      raise Exception('A fila está vazia.')

    item = self.inicio.item
    self.inicio = self.inicio.next
    if self.inicio == None:
      self.final = None

    self.count -= 1
    return item 

  def Peek(self):
    if self.IsEmpty():
      raise Exception('A fila está vazia.')

    return self.inicio.item

  def IsEmpty(self):
    return (self.inicio == None)

  def Count(self):
    return self.count

  def Display(self):
      for i in range(0, self.count):
          print(self.Dequeue())
          
  def SlowEnqueue(self, newItem):
      newNode = Node(newItem, None)
      x = self.inicio
      for i in range(0, self.count):
          self.x.next = newNode
          self.inicio = x
      self.count += 1
      
'************************************************************'
#Exemplo:
fila = QueueInList()
fila.Enqueue(9)
fila.Enqueue(23)
fila.Enqueue(72)
print(fila.Dequeue())
print(fila.Peek())
print(fila.IsEmpty())
print(fila.Count())
fila.SlowEnqueue(45)
fila.Display()
