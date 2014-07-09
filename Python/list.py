#!/usr/bin/env python2
#-*- coding: utf-8 -*-


#Voraussetzung ist ein sortiertes Array

A = [[1,"nutzlast"],[50,"cargo"],[100,"noch mehr cargo"]]

def insert(k,A):
# Algorithmus zum Einfügen von Daten
  # Wenn k kleiner als erstes Objekt
  # füge es an den Anfang der Liste an
  if k < A[0]:
    A = [k] + A
    return A
  # Wenn k größer oder gleich als letztes Objekt
  # Füge es an das Ende der Liste an
  if k >= A[-1]:
    A = A + [k]
    return A
  # Sonst erweitere Array 
  A = A + [0]
  l = len(A)
  for i in xrange(0, l):
    # Wenn k größer als linkes Element
    # und kleiner als rechtes Element
    # Füge k ein
    if k > A[i-1] and k < A[i+1]:
      for j in xrange(l-1,-1,-1):
        # wenn j == j ist Stelle zum einfügen
        # gefunden
        if j == i:
          break
        # Andernfalls schaffe platz für das Element
        A[j] = A[j-1]
      # hier wird k eingefügt
      A[i+1] = k
      return A

def find(k,A):
# Algorithmus zum finden von k in A
# gibt index zurück
  l = len(A)
  for i in xrange(0,l):
    if A[i] == k:
      return i
  return -1

def delete(k,A):
# Algorithmus zum löschen von k in A
# benutzt find(k,A) um index herauszufinden
  index = find(k,A)
  del A[index]
  return A

print A
A = insert([98, "langsam reichts mit cargo"],A)
print A
A = delete([98, "langsam reichts mit cargo"],A)
print(A)
