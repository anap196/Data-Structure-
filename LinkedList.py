# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:27:16 2022

@author: Ana Paula
"""

class Node:
  def __init__(self, newItem, nextNode):
    self.item = newItem
    self.next = nextNode


class MylinkedLista:
  def __init__(self):
    self.inicio = None
    self.final = None
    self.count = 0

  def AddFirst(self, newItem):

    newNo = Node(newItem, None)

    newNo.next = self.inicio
    self.inicio = newNo

    if self.final == None:
      self.final = newNo

    self.count += 1

  def AddLast(self, newItem):

    newNo = Node(newItem, None)

    if self.final == None:
      self.inicio = newNo
    else:
      self.final.next = newNo

    self.final = newNo
    self.count += 1

  def InsertAt(self, pos, newItem):
    if pos < 0 or pos > self.count:
      raise Exception('Posição inválida!!!')

    newNo = Node(newItem, None)
    if pos == 0:
      newNo.next = self.inicio
      self.inicio = newNo
    else:
      aux = self.inicio
      for i in range(0, pos-1):
        aux = aux.next

      newNo.next = aux.next
      aux.next = newNo

    if pos == self.count:
      self.final = newNo

    self.count += 1    


  def RemoveFirst(self):
    if self.IsEmpty():
      raise Exception('Lista vazia!!!')
    
    self.inicio = self.inicio.next

    if self.inicio == None:
      self.final = None

    self.count -= 1

  def RemoveLast(self):
    if self.IsEmpty():
      raise Exception('Lista vazia!!!')

    if self.count == 1:
       self.inicio = None
       self.final = None

    else:
      aux = self.inicio
      for i in range(0, self.count - 2):
        aux = aux.next

    aux.next = None
    self.final = aux

    self.count -= 1

  def Remove(self, item):
    if self.IsEmpty():
      raise Exception('Lista vazia!!!')

    aux = self.inicio
    ant = None
    while aux != None and aux.item != item:
      ant = aux
      aux = aux.next
    if (aux == None):
      return False
    if (aux == self.inicio):
      self.inicio = aux.next
    else:
      ant.next = aux.next
    if (aux == self.final):
      self.final = ant

    self.count -= 1
    return True

  def RemoveAt(self, pos):
    if self.IsEmpty():
      raise Exception('Lista vazia!!!')

    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')

    if pos == 0:
       aux = self.inicio
    else:
       aux = self.inicio
       for i in range(0, pos - 1):
        aux = aux.next

    aux.next = aux.next.next

    if aux == self.final:
      self.final = aux

    if self.count == 1:
      self.inicio = None
      self.final = None

    self.count -= 1

  def Find(self, item):
    aux = self.inicio
    while aux != None and aux.item != item:
      aux = aux.next

    if aux == None:
      return False
    
    if aux.item == item:
      return True

  def Get(self, pos):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!!!')

    aux = self.inicio
    for i in range(0, pos):
      if aux == pos:
        return aux.item

  def Set(self, pos, newItem):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!!!')

    aux = self.inicio
    for i in range(0, pos):
      aux = aux.next
    aux = newItem

  def Display(self):
    aux = self.inicio
    while aux != None:
      print(aux.item)
      aux = aux.next

  def IsEmpty(self):
    return self.count == 0

'******************************************************************'
#Exemplo da lista simplesmente ligada:
lista1 = MylinkedLista()
lista1.AddFirst(9)
lista1.AddFirst(5)
lista1.AddLast(75)
lista1.InsertAt(2, 30)
lista1.RemoveFirst()
lista1.RemoveLast()
lista1.Remove(9)
lista1.AddFirst(1)
lista1.AddLast(6)
lista1.RemoveAt(1)
print(lista1.Find(6))
print(lista1.Get(0))
lista1.Display()
'*******************************************************************'
'''class Node:
  def __init__(self, newItem, nextNode):
    self.item = newItem
    self.next = nextNode'''


class CircularLinkedList:
  def __init__(self):
    self.final = None
    self.count = 0

  def AddFirst(self, newItem):
    newNo = Node(newItem, None)

    if self.final == None:
      newNo.next = newNo
      self.final = newNo

    else:
      newNo.next = self.final.next
      self.final.next = newNo

    self.count += 1

  def AddLast(self, newItem):
    self.AddFirst(newItem)
    self.final = self.final.next

  def InsertAt(self, pos, newItem):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!!!')

    newNo = Node(newItem, None)

    if pos == 0:
      newNo.next = self.final.next
      self.final.next = newNo
    else:
      aux = self.final.next
      for i in range(0, pos-1):
        aux = aux.next

    newNo.next = aux.next
    aux.next = newNo

    if pos == self.count:
      self.AddFirst(newItem)
      self.final = self.final.next

    self.count += 1

  def RemoveFirst(self):
    if self.IsEmpty():
      raise Exception('Lista vazia!')

    self.final.next = self.final.next.next
    
  def RemoveLast(self):
    if self.IsEmpty():
      raise Exception('Lista Vazia!!!')

    if self.count == 1:
      self.final = None
    else:
      aux = self.final.next
      for i in range(0, self.count - 2):
        aux = aux.next
      aux.next = aux.next.next
      self.final = aux

    self.count -= 1

  def Remove(self, item):
    if self.IsEmpty():
      raise Exception('Lista Vazia!')

    aux = self.final.next
    anterior = self.final
    while aux != self.final and aux.item != item:
      anterior = aux
      aux = aux.next

    if aux.item != item:
      return False

    if aux == aux.next:
      self.final = None
    else:
      anterior.next = aux.next
      if aux == self.final:
        self.final = anterior
    self.count -= 1
    return True

  def RemoveAt(self, pos):
    if self.IsEmpty():
      raise Exception('Lista Vazia!')

    if pos < 0 or pos > self.count:
      raise Exception('Posição inválida.')

    aux = self.final.next
    anterior = self.final
    for i in range(0, pos):
      anterior = aux
      aux = aux.next

    if aux == self.final:
      self.final = None
    else:
      anterior.next = aux.next
      if aux == self.final:
        self.final = anterior
    self.count -= 1

  def Find(self, item):
    aux = self.final.next
    while aux != self.final and aux.item != item:
      aux = aux.next

    if aux == self.final:
      return False
    
    if aux.item == item:
      return True

  def Get(self, pos):
    if pos < 0 or pos > self.count:
      raise Exception('Posição Inválida!')
    
    aux = self.final.next
    for i in range(0, pos-1):
      aux = aux.next
      
    return aux.item

  def Display(self):
    aux = self.final.next
    while aux != self.final:
      print(aux.item)
      aux = aux.next
    print(aux.item)

  def IsEmpty(self):
    return self.count == 0

'*********************************************************'
#Exemplo 2 - Lista Simplesmente Ligada Circular:
lista2 = CircularLinkedList()
lista2.AddFirst(8)
lista2.AddFirst(7)
lista2.AddLast(0)
lista2.AddLast(81)
lista2.InsertAt(1, 45)
lista2.RemoveFirst()
lista2.RemoveLast()
lista2.RemoveAt(1)
lista2.Remove(8)
print(lista2.Get(0))
lista2.Display()

'*************************************************************'

