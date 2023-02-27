# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 18:24:34 2022

@author: Ana Paula
"""

import array
import random
import datetime

class Sorting:

  @staticmethod
  def QuickSort(array):
    Sorting.QuickSort_(array, 0, len(array) - 1)

  @staticmethod
  def QuickSort_(array, inicio, fim):
    if inicio < fim:
      posPivo = Sorting.__Particiona(array, inicio, fim)
      Sorting.QuickSort_(array, inicio, posPivo - 1)
      Sorting.QuickSort_(array, posPivo + 1, fim)

  @staticmethod
  def __Particiona(array, inicio, fim):
    pivo = array[inicio]
    esq = inicio
    dir = fim
    while esq < dir:
      while (esq <= fim and array[esq] <= pivo):
        esq += 1
      while (array[dir] > pivo):
        dir -= 1

      if (esq < dir):
        temp = array[esq]
        array[esq] = array[dir]
        array[dir] = temp

    array[inicio] = array[dir]
    array[dir] = pivo
    return dir 

  @staticmethod
  def MergeSort(array):
    Sorting.MergeSort_(array, 0, len(array) - 1)

  @staticmethod
  def MergeSort_(array, inicio, fim):
    if (inicio < fim):
      meio = (inicio + fim) // 2

      Sorting.MergeSort_(array, inicio, meio)

      Sorting.MergeSort_(array, meio + 1, fim)

      Sorting.__Merge(array, inicio, meio, fim)

  @staticmethod
  def __Merge(array, inicio, meio, fim):
    n1 = meio - inicio + 1
    n2 = fim - meio
    esq = [0 for i in range(n1)]
    dir = [0 for i in range(n2)]

    for i in range(n1):
      esq[i] = array[inicio + i]

    for j in range(n2):
      dir[j] = array[meio + 1 + j]

    i = 0
    j = 0
    k = inicio
    while (i < n1 and j < n2):
      if (esq[i] <= dir[j]):
        array[k] = esq[i]
        i += 1

      else:
        array[k] = dir[j]
        j += 1
      k += 1

    while i < n1:
      array[k] = esq[i]
      k += 1
      i += 1

    while j < n2:
      array[k] = dir[j]
      k += 1
      j += 1


#Programa principal:  
#Utilizamos N = 1000, 10000, 50000, 100000, 150000, 200000, 250000.  
N = 1000
MAX = 500000
array = array.array('i', [0 for i in range(N)])
for j in range(0, N):
  y = random.randint(0, MAX)
  array[j] = y

start = datetime.datetime.now()
Sorting.QuickSort(array)
#Sorting.MergeSort(array)
end = datetime.datetime.now()
delta = end - start
print('Tempo gasto em segundos: ', delta.total_seconds())