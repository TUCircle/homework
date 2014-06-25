#!/usr/bin/env python2
#-*- coding: utf-8 -*-



# Funktion zur Berechnung des kartesischen Produkts:
# Alle Möglichkeiten einschließlich duplikaten
# Beispiele:
# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
def product(*args, **kwds):
    # Erstelle pools als Cache für kartesische Produkte
    pools = map(tuple, args) * kwds.get('repeat', 1)
    # Erstelle 2D Array für zwischenergebnisse
    result = [[]]
    for pool in pools:
        # Für jeden Pool errechne kartesisches produkt
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        # gebe iterierbares Objekt zurück für 
        # jedes Zwischenergebnis
        yield tuple(prod)


def iter(A,b):
  n = len(A)

  # Der Cache besteht aus 2 Arrays
  # Array D speichert die kartesischen Produkte
  # Array C speichert die errechneten Summen 
  # Man hätte hier auch ein 1 2D-Array
  # nehmen können statt 2 Arrays aber 
  # 2 Arrays erschien mir effizienter
  # und einfacher.
  C = []
  D = []
  for j in xrange(n, 0, -1):
    for i in product(A, repeat=j):
      D.append(i)
      C.append(sum(i))
  # Annähern des besten Werts
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
