#!/usr/bin/env python2
#-*- coding: utf-8 -*-
# Hinweise zu tabs in vim: set ts=2 sts=2 sw=2 et
# Christian Rebischke 


def wahlzettelNaiv(votes):
  """Naiver Wahlzettel Algorithmus.
     Erwartet eine Liste mit Stimmabgaben
     und gibt den Sieger zurück.
     Wenn kein Sieger feststellbar ist da
     zum Beispiel die absolute Mehrheit(majority)
     fehlt gibt die funktion 'False' zurück"""
  winner = False
  majority = len(votes) / 2
  #besser wäre: __import__("math").floor(len(votes) / 2
  #dies macht den code auch kompatibel mit python3
  elected = {}
  #Stimmen verteilen
  for name in votes:
    if name not in elected:
      elected.update({name:1})
    elif name in elected:
      elected[name] += 1
  #Wahlsieger bestimmen
  for name in elected:
    if elected[name] > majority:
      winner = name
  if winner != False:
    return winner
  else:
    return False 

    
print("Hauptprogramm welches das Array füttert")
print("Der Algorithmus benötigt ein Array als Übergabewert")
array = []
vote = "initialisierung"
while vote != "exit":
  vote = raw_input("Bitte Stimme abgeben: ")
  print("Danke für ihre Stimmabgabe")
  print("Wenn sie keine Stimme mehr abgegeben werden soll")
  print("einfach exit eingeben, danke")
  print("")
  if vote != "exit":
    array.append(vote)
print("Alle Stimmen wurden abgegeben")
print("Rien ne va plus.. nichts geht mehr :D")
winner = wahlzettelNaiv(array)
if winner == False:
  print("Es konnte kein Sieger festgestellt werden")
  exit(1)
else:
  print("")
  print("Der Sieger ist .... %s" % winner)
  exit(0)
