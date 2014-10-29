#!/usr/bin/env python2
#-*- coding: utf-8 -*-
# Hinweise zu tabs in vim: set ts=2 sts=2 sw=2 et
# Christian Rebischke 


############## Import Exceptions #####################
try:
  import sys
  useArgument = True
except ImportError:
  print("Konnte sys nicht importieren")
  print("sys wird gebraucht für Kommandozeilenargumente")
  print("Schalte um auf manuelle Eingabe")
  useArgument = False

try:
  import math
  isMathImported = True
except ImportError:
  print("math konnte nicht importiert werden")
  print("math ist wichtig für eine reibungslose abrundung unter python3")
  print("python2 schneidet bei der teilung einfach ab")
  print("Bitte Standardlib 'math' nachinstallieren oder")
  print("das math.floor() im Quellcode streichen")
  print("Den Fehler auch noch aufzufangen hätte")
  print("hässlichen Code das wollt ich dann doch nicht")
  isMathImported = False

############### Globale Variablen #####################
# PURSE 
# englisch für Geldbörse dient zum definieren
# der einzelnen möglichen CentStücke

PURSE = [100,50,20,10,5,2,1]

############### Eigentlicher Algorithmus ##############

def calc(number):
  """Wechselgeldberechnungsalgorithmus erwartet eine Ganzzahl
     als Eingabe und liefert ein Array zurück.
     Die For-Schleife iteriert die Geldbörse durch 
     und berechnet dann den output anhand der übergebenen zahl
     math.floor ist notwendig zum runden unter python3
     unter python2 kann man darauf verzichten
     weil die zahl einfach 'abgeschnitten' wird"""
  output = [0] * len(PURSE)
  counter = 0
  for i in PURSE:
    output[counter] = int(math.floor(number / i))
    number = number % i
    counter +=  1
  return output


############### Hauptprogramm ########################
# Dynamisches Hauptprogramm was auf ImportError's reagiert

if useArgument == True:
  if len(sys.argv) == 2:
    number = sys.argv[1]
    try:
      number = int(number)
    except:
      print("Bitte eine ganzzahl eingeben")
      exit(1)
    output = calc(number)
    counter = 0
    for i in PURSE:
      print("Anzahl der %s cent Stücke: %s") % (PURSE[counter], output[counter])
      counter += 1
    exit(0)
  elif len(sys.argv) < 2:
    print("Usage: ./wechselgeld.py <geldbetrag ohne komma>")
    exit(1)
  elif len(sys.argv) > 2:
    print("Usage: ./wechselgeld.py <geldbetrag ohne komma>")
    exit(1)
  else:
    print("Usage: ./wechselgeld.py <geldbetrag ohne komma>")
    exit(1)

elif useArgument == False:
  number = raw_input("Bitte einen geldbetrag eingeben: ")
  try:
    number = int(number)
  except:
    print("Bitte eine ganzzahl eingeben")
    exit(1)
  output = calc(number)
  counter = 0
  for i in PURSE:
    print("Anzahl der %s cent Stücke: %s") % (PURSE[counter], output[counter])
    counter += 1
  exit(0)
