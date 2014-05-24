#!/usr/bin/env python2
#-*- coding: utf-8 -*-
# Hinweise zu tabs in vim: set ts=2 sts=2 sw=2 et
# Christian Rebischke 


def wahlzettelIntelligent(votes):
  """Intelligenter Wahlzettel Algorithmus
     erwartet eine Liste und gibt wenn
     kein Sieger festzustellen ist
     'False' zurück"""
  majority = len(votes) / 2
  elected = []
  #Phase 1 - Stapeldurchlauf
  for name in votes:
    if not elected:
      elected.append(name)
    elif elected[-1] == name:
      elected.append(name)
    else:
      elected.pop
  if not elected:
    winner = False
  else:
    winner = elected[-1]
    #Phase 2 - Überprüfung auf absolute Mehrheit
    proof = max(set(votes), key=votes.count)
    if winner == proof:
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
winner = wahlzettelIntelligent(array)
if winner == False:
  print("Es konnte kein Sieger festgestellt werden")
  exit(1)
else:
  print("")
  print("Der Sieger ist .... %s" % winner)
  exit(0)
 
  
