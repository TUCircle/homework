#!/usr/bin/env python2
#-*- coding: utf-8 -*-
"""
Algorithmus zum finden der besten Aktivitätenzusammensetzung.
Ich verwende zu erst 2x mal insertion-Sort. Bei Insertion-sort
handelt es sich um ein stabiles Sortierverfahren.
Dadurch das Insertion-Sort stabil ist kann ich die beste
Reihenfolge für die Aktivitäten bestimmen.

Wenn ich diese Reihenfolge habe, kann ich mit 
einem Greedy-Algorithmus dann zueinander kompatiblen
Aktivitäten herausziehen und die Summe bestimmen.
"""


#Beispiel Array
#a = [ [Startzeit, Endzeit, "Activit-name"], ..... ]
a = [[0,13,"Act 1"],[3,4,"Act 2"],[5,8,"Act 3"],
    [14,15,"Act 4"],[6,7,"Act 5"],[1,3,"Act 6"]]

def activity(a):
  # Sortiere nach Startzeit
  for k in range(1, len(a)): 
    save = a[k]
    i = k 
    while i > 0 and a[i-1] > save: 
      a[i] = a[i-1] 
      i -= 1 
    a[i] = save 
  
  # Tausche Startzeit mit Endzeit 
  a = [[t[1], t[0], t[2]] for t in a]
  
  # Sortiere nach Endzeit
  for k in range(1, len(a)): 
    save = a[k]
    i = k 
    while i > 0 and a[i-1] > save: 
      a[i] = a[i-1] 
      i -= 1 
    a[i] = save
  
  # Tausche wieder zurück zu Eingangsformat
  a = [[t[1], t[0], t[2]] for t in a]
  
  # Hier beginnt der eigentliche Greedy-Algorithmus
  b = []
  
  # Iteriere durch array durch 
  for i in range(0,len(a)):
    # Wenn b leer dann schreibe erstes teil-array in b
    if b == []:
      b.append(a[0])
    # Try-Catch Block stellt fest wann wir fertig sind
    # und bricht die Iterierung ab. Dieser Zeitpunkt ist
    # genau dann wenn i+1 außerhalb des Arrays liegt.
    try:
      # Vergleiche momentane Start- und Endzeit mit der
      # Start- und Endzeit des naechsten Teil-Arrays
      # Falls alles passt wird das array b erweitert.
      if a[i][1] <= a[i+1][1] and a[i][0] <= a[i+1][0]:
         b.append(a[i+1])
    except:
      break
    
    # Errechne Summe der möglichen zueinander
    # kompatiblen Aktivitäten
    summe = 0
    for i in b:
      summe += 1
  
  #gebe Ergebnisarray und Summe zurück
  return b, summe

print "Mögliche Kombination der Aktivitäten"
print(activity(a)[0])
print "Maximale Zahl der zueinander kompatiblen Aktivitäten"
print(activity(a)[1])
