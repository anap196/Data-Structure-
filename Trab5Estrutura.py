# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:06:10 2022

@author: Ana Paula
"""

class Node:
  def __init__(self, newItem):
    self.next = None
    self.prev = None
    self.item = newItem


class DoubleLinkedCircularList:
  def __init__(self):
    self.inicio = None
    self.count = 0

  def __InsertBefore(self, aux, newNode):
    newNode.prev = aux.prev
    newNode.next = aux
    aux.prev.next = newNode
    aux.prev = newNode

  def __RemoveNode(self, aux):
    if self.count <= 1:
      raise Exception('Não Permitido.')
    aux.prev.next = aux.next
    aux.next.prev = aux.prev
    
  def AddFirst(self, newItem):
    self.AddLast(newItem)
    self.inicio = self.inicio.prev

  def AddLast(self, newItem):
    newNode = Node(newItem)

    if self.inicio == None:
      newNode.prev = newNode
      newNode.next = newNode
      self.inicio = newNode
    else:
      self.__InsertBefore(self.inicio, newNode)
    self.count += 1

  def InsertAt(self, pos, newItem):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')

    newNode = Node(newItem)
    if self.inicio == None:
      newNode.prev = newNode
      newNode.next = newNode
    else:
      aux = self.inicio
      for i in range(0, pos):
        aux = aux.next
      self.__InsertBefore(aux, newNode)

    if pos == 0:
      self.inicio = newNode

    self.count += 1

  def RemoveFirst(self):
    if self.IsEmpty():
      raise Exception('Lista Vazia!')

    if self.count == 1:
      self.inicio = None
    else:
      self.__RemoveNode(self.inicio)
      self.inicio = self.inicio.next
    self.count -= 1

  def RemoveLast(self):
    if self.IsEmpty():
      raise Exception('Lista vazia!')
    if self.count == 1:
      self.inicio == None
    else:
      self.__RemoveNode(self.inicio.prev)
    self.count -= 1

  def Remove(self, item):
    if self.IsEmpty():
      raise Exception('Lista vazia!')
    
    aux = self.inicio
    ult = self.inicio.prev
    while aux != ult and aux.item != item:
      aux = aux.next

    if aux.item != item:
      return False
    if self.count == 1:
      self.inicio = None
    else:
      self.__RemoveNode(aux)
      if aux == self.inicio:
        self.inicio == self.inicio.next
    self.count -= 1
    return True

  def RemoveAt(self, pos):
    if self.IsEmpty():
      raise Exception('Lista Vazia!')
    
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')

    if pos == 0:
      self.__RemoveNode(self.inicio)
      self.inicio = self.inicio.next
      
    else:
     aux = self.inicio
     for i in range(0, pos):
       aux = aux.next
       self.__RemoveNode(aux)
    self.count -= 1

  def Find(self, item):
    aux = self.inicio.next
    for i in range(0, self.count):
      aux = aux.next

      if aux.item != item:
        return False
      if aux.item == item:
        aux.item == item
        return True

  def Get(self, pos):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')
    aux = self.inicio
    for i in range(0, pos):
      aux = aux.next
    return aux.item

  def Set(self, pos, newItem):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')

    aux = self.inicio
    for i in range(0, pos):
      aux = aux.next
      self.__InsertBefore(aux, newItem)  

  def DisplayFirstToLast(self):
    aux = self.inicio
    while aux != self.inicio.prev:
      print(aux.item)
      aux = aux.next
    print(aux.item)

  def DisplayLastToFirst(self):
    aux = self.inicio.prev
    while aux != self.inicio:
      print(aux.item)
      aux = aux.prev
    print(aux.item)

  def IsEmpty(self):
     return self.count == 0

'*******************************************************************'
#Exemplo da lista duplamente ligada circular:
lista1 = DoubleLinkedCircularList()
lista1.AddFirst(5)
lista1.AddLast(9)
lista1.AddFirst(13)
lista1.InsertAt(2, 30)
lista1.AddFirst(9)
lista1.AddLast(6)
lista1.AddFirst(15)
lista1.RemoveFirst()
lista1.RemoveLast()
lista1.RemoveAt(2)
lista1.Remove(6)
print(lista1.Find(9))
print(lista1.Get(0))
lista1.DisplayFirstToLast()
lista1.DisplayLastToFirst()

'**********************************************************************'
'''class Node:
  def __init__(self, newItem):
    self.next = None
    self.prev = None
    self.item = newItem'''


class DoubleLinkedCircularListJosephus:
  def __init__(self):
    self.inicio = None
    self.count = 0

  def __InsertBefore(self, aux, newNode):
    newNode.prev = aux.prev
    newNode.next = aux
    aux.prev.next = newNode
    aux.prev = newNode

  def __RemoveNode(self, aux):
    if self.count <= 1:
      raise Exception('Não Permitido.')
    aux.prev.next = aux.next
    aux.next.prev = aux.prev
    
  def AddFirst(self, newItem):
    self.AddLast(newItem)
    self.inicio = self.inicio.prev

  def AddLast(self, newItem):
    newNode = Node(newItem)

    if self.inicio == None:
      newNode.prev = newNode
      newNode.next = newNode
      self.inicio = newNode
    else:
      self.__InsertBefore(self.inicio, newNode)
    self.count += 1

  def InsertAt(self, pos, newItem):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')

    newNode = Node(newItem)
    if self.inicio == None:
      newNode.prev = newNode
      newNode.next = newNode
    else:
      aux = self.inicio
      for i in range(0, pos):
        aux = aux.next
      self.__InsertBefore(aux, newNode)

    if pos == 0:
      self.inicio = newNode

    self.count += 1

  def RemoveFirst(self):
    if self.IsEmpty():
      raise Exception('Lista Vazia!')

    if self.count == 1:
      self.inicio = None
    else:
      self.__RemoveNode(self.inicio)
      self.inicio = self.inicio.next
    self.count -= 1

  def RemoveLast(self):
    if self.IsEmpty():
      raise Exception('Lista vazia!')
    if self.count == 1:
      self.inicio == None
    else:
      self.__RemoveNode(self.inicio.prev)
    self.count -= 1

  def Remove(self, item):
    if self.IsEmpty():
      raise Exception('Lista vazia!')
    
    aux = self.inicio
    ult = self.inicio.prev
    while aux != ult and aux.item != item:
      aux = aux.next

    if aux.item != item:
      return False
    if self.count == 1:
      self.inicio = None
    else:
      self.__RemoveNode(aux)
      if aux == self.inicio:
        self.inicio == self.inicio.next
    self.count -= 1
    return True

  def RemoveAt(self, pos):
    if self.IsEmpty():
      raise Exception('Lista Vazia!')
    
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')

    if pos == 0:
      self.__RemoveNode(self.inicio)
      self.inicio = self.inicio.next
      
    else:
     aux = self.inicio
     for i in range(0, pos):
       aux = aux.next
       self.__RemoveNode(aux)
    self.count -= 1

  def Find(self, item):
    aux = self.inicio.next
    for i in range(0, self.count):
      aux = aux.next

      if aux.item != item:
        return False
      if aux.item == item:
        aux.item == item
        return True

  def Get(self, pos):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')
    aux = self.inicio
    for i in range(0, pos):
      aux = aux.next
    return aux.item

  def Set(self, pos, newItem):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')

    aux = self.inicio
    for i in range(0, pos):
      aux = aux.next
      self.__InsertBefore(aux, newItem)  

  def DisplayFirstToLast(self):
    aux = self.inicio
    while aux != self.inicio.prev:
      print(aux.item)
      aux = aux.next
    print(aux.item)

  def DisplayLastToFirst(self):
    aux = self.inicio.prev
    while aux != self.inicio:
      print(aux.item)
      aux = aux.prev
    print(aux.item)

  def IsEmpty(self):
     return self.count == 0

  def CountNodesAndRemove(self, m):
    m = self.inicio
    for i in range(0, m):
      m = m.prev
    self.inicio = m.prev
    self.__RemoveNode(m)
    self.count -= 1

  def Josephus(self, m):
      if self.IsEmpty():
          raise Exception('Lista vazia!')
          
      for i in range(self.count - 1):
        self.CountNodesAndRemove(m)
      return self.inicio.item