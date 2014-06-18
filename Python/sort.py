#!/usr/bin/env python2
#-*- coding: utf-8 -*- 
# 
# Christian Rebischke 
#
# Laufzeit n^2 da Insertion-Sort 2mal hintereinander
#
# Eingegebene Namensliste MUSS diesem Format entsprechen
# und die Namen müssen mit Großen Buchstaben beginnen.
a = [("Max", "Schnell"), ("Max", "Muster"), ("Dora", "Muster"), 
    ("Anna", "Schnell"), ("Tom", "Schnell"), ("Dora", "Schnell")]

def sort(a):
    # Insertion-Sort sortiert 1. Element im Tuple
    # in diesem Fall den Vornamen
    for k in range(1, len(a)): 
      save = a[k]
      i = k 
      while i > 0 and a[i-1] > save: 
        a[i] = a[i-1] 
        i -= 1 
      a[i] = save 
    
    #Debugging Ausgaben zum Verständnis
    print "Namensliste sortiert nach Vornamen"
    print a

    # Die Tuple werden getauscht. Die Position im Array
    # bleibt dabei aber erhalten.
    a = [(t[1], t[0]) for t in a]

    # Insertion-Sort sortiert 1. Element im Tuple
    # in diesem Fall den Nachnamen da 
    # Vor und Nachname getauscht worden sind im Tuple
    for k in range(1, len(a)):
      save = a[k]
      i = k
      while i > 0 and a[i-1] > save:
        a[i] = a[i-1]
        i -= 1
      a[i] = save

    # Die Tuple werden wieder zurück getauscht
    # Damit die Namen wieder im Format 
    # Vorname, Nachname bereit stehen.
    a = [(t[1], t[0]) for t in a]
    
    #Debugging Ausgaben zum Verständnis
    print "Namensliste sortiert nach Nachnamen"
    print a

# Main funktion ruft sort auf
print "Eingegeben Namensliste:"
print a
sort(a)
