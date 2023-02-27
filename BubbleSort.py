# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 20:15:33 2022

@author: Ana Paula
"""

import array
import random
import datetime

class Sorting:

  @staticmethod
  def BubbbleSort(array):
    n = len(array)
    for i in range(n-1, 0, -1):
      for j in range(0, i):
        if (array[j] > array[j + 1]):
          temp = array[j]
          array[j] = array[j + 1]
          array[j + 1] = temp

  @staticmethod
  def SelectionSort(array):
    n = len(array)
    for i in range(0, n-1):
      posMenor = i
      for j in range(i+1, n):
        if (array[j] < array[posMenor]):
          posMenor = j

      temp = array[posMenor]
      array[posMenor] = array[i]
      array[i] = temp

  @staticmethod
  def InsertionSort(array):
    n = len(array)
    for i in range(1, n):
      key = array[i]
      j = i - 1

      while (j >= 0 and array[j] > key):
        array[j + 1] = array[j]
        j -= 1

      array[j + 1] = key

'***********************************'
#Usamos N = 1000, 10000, 50000, 100000, 150000, 200000, 250000.
N = 1000
MAX = 500000
items = array.array('i', [0 for i in range(N)])
for j in range(0, N):
  y = random.randint(0, MAX)
  items[j] = y
  
'***********************************************************'

start = datetime.datetime.now()
Sorting.BubbbleSort(items)
#Sorting.InsertionSort(items)
#Sorting.SelectionSort(items)
end = datetime.datetime.now()
delta = end - start
print('Tempo gasto em segundos: ', delta.total_seconds())
'**************************************************************'
