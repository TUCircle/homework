#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
# Christian Rebischke 
#
# fibonacci über die bekannte rechenformel
# Laufzeit 2^n da der Algorithmus jeweils 2 mal
# sich selbst aufruft für n mal
# Sich also bei jeder Ebene tiefer verdoppelt

import sys

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1

  else:
    e = fib(n-1) + fib(n-2)
    return e

print(fib(int(sys.argv[1])))
