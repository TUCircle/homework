#!/usr/bin/env python
#-*- coding: utf-8 -*-

#sys für systemargumente
#math zum abrunden bei python2 eigentlich nicht notwendig
import sys,math

# Optionen für Rückgeldwiedergabe
OPTIONS  = [500,200,10]


#DynamicProgramming-wechselgeldalgorithmus
def wechselgeld(number):
  #Output-Array
  output = [0] * len(OPTIONS)
  #Baue Cache auf zur Speicherung der Ergebnisse
  cache = [0] * len(OPTIONS)
  #Zähler für innere Schleife
  counter = 0
  #Iterator für äußere Schleife
  iterator = 0
  #Mirror zum Resetten des Inputs
  copynumber = number
  #Schleifenkonstrukt laufzeit n^2
  for j in xrange(0,len(OPTIONS)):
    for i in xrange(0,len(OPTIONS)):
      #Try-Except block zum fangen von index-fehlern
      try:
        output[counter+j] = int(math.floor(number / OPTIONS[i+j]))
        number = number % OPTIONS[i+j]
        counter +=  1
      except: 
        pass
    #Hier wird das momentane ergebnis im Cache gespeichert
    cache[iterator] = output
    counter = 0
    number = copynumber
    #Resetten des momentanen Outputs
    output = [0] * len(OPTIONS)
    #If-Abfrage dient zum ermitteln des besten Ergebnisses
    if iterator >= 1:
      if sum(cache[iterator-1]) <= sum(cache[iterator]):
        return cache[iterator-1]
    iterator += 1
    
    


#Eingabe des Wechselgeldes in cent Beträgen
#Also 1€ == 100cent
output = wechselgeld(int(sys.argv[1]))
for i in xrange(0, len(OPTIONS)):
  print("Anzahl der %s cent Stücke: %s") % (OPTIONS[i], output[i])

