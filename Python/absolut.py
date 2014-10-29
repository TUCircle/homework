#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#Christian Rebischke 

#Testwerte
A = [1,5,4,8,8,5,4,3,2,9,5,3,2]
z = 5

def absolut(A,z):
  """Eine If-Abfrage zur Überprüfung ob A leer ist
     ist nicht von Nöten der Algorithmus gibt
     trotzdem 0 aus"""
  counter = 0
  for i in A:
    if i == z:
      counter += 1
  return counter

print(absolut(A,z))

