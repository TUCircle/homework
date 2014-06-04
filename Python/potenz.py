#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#Divide And Conquer Beispiel

#Nur zum Testen
import sys


def potenz(x,n):
  if n == 0:
    return 1
  elif n == 1:
    return x
  
  if ( n % 2) == 0:
    z = potenz( x, (n / 2))
    z *= z
    return z
  else:
    z = potenz(x, ( ( n - 1) / 2))
    z *= z
    z *= x
    return z


#Testen mit: python2 potenz.py x n
print(potenz(int(sys.argv[1]),int(sys.argv[2])))
    
