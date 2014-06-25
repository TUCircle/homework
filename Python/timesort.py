#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Algorithmus zur Berechnung
der idealen Abarbeitungszeit 
von Aufgaben. Ziel des Algorithmus
ist die Wartezeit minimal zu halten.
"""

#Funktion zur Berechnung der Summe eines 
#Arrays
def sum(array):
  value = 0
  for i in range(0, len(array)):
    value += array[i]
  return value


def timesort(a):
  #Insertionsort
  for k in range(1, len(a)): 
    save = a[k]
    i = k 
    while i > 0 and a[i-1] > save: 
      a[i] = a[i-1] 
      i -= 1 
    a[i] = save
  #Minimale Zeit ausrechnen
  solution = 0
  for i in range(0,len(a)):
    solution += sum(a[:i+1])
  return a, solution


#Testarray
a = [3,10,5]

print("Eingabe: ")
print(a)
print("Ergebnis-Array: ")
print(timesort(a)[0])
print("Minimale Zeit: ")
print(timesort(a)[1])
