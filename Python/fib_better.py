#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
# Christian Rebischke 
#
# fibonacci divide and conquer
# 
# Laufzeit: n (siehe mastertheorem)
# Begründung: Das Fibonacci Problem wird in 
# n-Teilprobleme zerlegt und anschließend wieder
# zusammengesetzt.
#
# kurzes Statement zu den Zeilen 
# t = fib(k)
# t1 = fib(k-1)
# t1 = fib(k)
#
# Meine tests haben ergeben das 
# wenn man wertzuweisungen setzt der Algorithmus
# nochmal um einiges schneller läuft
# so ist dieser Algorithmus bei 
# n = 1000000 nach 13,4s fertig
# Wenn man stattdessen jedes mal
# fib(k), fib(k-1) etc berechnet
# insbesondere bei Aufrufen wie:
# fib(k) * fib(k) betrug die laufzeit
# bei n = 1000000 bei mir über 14 Stunden
# Man sollte also bei Funktionsaufrufen darauf
# achten, dass man nichts umsonst doppelt
# berechnet. Dies spart erheblich an Laufzeit.

import sys

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    if (n % 2) == 0:
      k = n/ 2
      t = fib(k)
      e = (t * t) + 2 * t * fib(k-1)
      return e

    else:
      k = (n + 1) / 2
      t1 = fib(k-1)
      t2 = fib(k)
      e = (t1 * t1) + (t2 * t2)
      return e

print(fib(int(sys.argv[1])))

