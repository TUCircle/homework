#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#Christian Rebischke 

#Testwerte
A = [1,5,4,8,8,5,4,3,2,9,5,3]
z = 5

def relativ(A,z):
  #Wenn Liste leer gebe 0 zurück
  if A == []:
    return 0
  counter = 0.0
  length = 0.0
  #Berechnet Länge der Liste
  #und absoluten Betrag für relative Umrechnung
  #War mir nicht sicher ob len() erlaubt ist
  for i in A:
    length += 1.0
    if z == i:
      counter += 1.0
  #Formel für Umrechnung in Komma-Prozent
  #Zum Beispiel 0.25 = 25%
  return (100*counter) / length

print(relativ(A,z))
