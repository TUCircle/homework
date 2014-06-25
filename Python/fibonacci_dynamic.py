#!/usr/bin/env python2
#-*- coding: utf-8 -*-
"""
Fibonacci Algorithmus auf Basis von Dynamischer 
Programmierung. 

Dieser Algorithmus nutzt das bottom-up
Verfahren. Er berechnet also die kleineren
leichteren Fibonacci ergebnisse zu erst
speichert diese in die beiden Variablen
previous und Current und
berechnet dann daraus die größeren
schwierigeren. Daraus ergibt sich eine
Laufzeit von O(n).
"""

#Zum testen 
import sys 

def fib(n):
  if n == 0:
    return 0
  else:
    #Initialisieren der beiden Cache 
    #Variablen previous und current
    previous = 0
    current = 1
    for i in range(n-1):
      if n == 1:
        break
      #Verrechnen des Caches zum neuen
      #Wert und füllen des Caches
      #mit neuen Werten
      new = previous + current
      previous = current
      current = new
  return current


#Test-main
print(fib(int(sys.argv[1])))
