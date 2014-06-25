#!/usr/bin/env python2
#-*- coding: utf-8 -*-


# Funktion zur Berechnung der Permutationen
# Permutationen = Paare ohne Duplikate
# Beispiele:
# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
# permutations(range(3)) --> 012 021 102 120 201 210
#
# Funktioniert gibt mit "yield" iterierbare Objekte zurück
def permutations(iterable, r=None):
    # generiert aus dem Array iterable ein Tuple
    pool = tuple(iterable)
    n = len(pool)
    # r setzt Anzahl der möglichen Kombinationen
    # Wenn r = 2 -> zweierkombinationen
    # Wenn r = 3 -> dreierkombinationen usw..
    r = n if r is None else r
    if r > n:
        return
    # Generiert Array mit Indizes
    indices = range(n)
    # Generiert Kombination
    cycles = range(n, n-r, -1)
    # Erzeugt iterierbares Objekt
    yield tuple(pool[i] for i in indices[:r])
    while n:
        # invertiert indexes von r
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                # mischt indizes durch
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return



def iter(A,b):
  n = len(A)
  
  # Der Cache besteht aus 2 Arrays
  # Array D speichert die Permutationen
  # Array C speichert die errechneten Summen 
  # Man hätte hier auch ein 1 2D-Array
  # nehmen können statt 2 Arrays aber 
  # 2 Arrays erschien mir effizienter
  # und einfacher.
  C = []
  D = []
  for j in xrange(n, 0, -1):
    for i in permutations(A, j):
      D.append(i)
      C.append(sum(i))
  # Annähern des Besten Werts
  for i in xrange(b, -1, -1):
    # Abfangen von möglichen
    # Fehlern wenn maximale
    # Lösung nicht gefunden werden
    # kann.
    try:
      if C.index(i):
        index = C.index(i)
        break
    except:
      pass
  print "Ergebnis ist"
  print D[index]
  print C[index]


A = [10,15,20,22]
b = 50
iter(A,b)
