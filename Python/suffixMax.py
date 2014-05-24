#!/usr/bin/env python2
#-*- coding: utf-8 -*-

def suffixMax(A):
  """ input: array A von Ints 
      output: maximales Gewicht 
         eines Präfix von A """ 
  currentMax = 0 
  currentSum = 0 
  A = A[::-1]
  for R in range(len(A)): 
    currentSum += A[R] 
    if currentSum > currentMax: 
      currentMax = currentSum 
  return currentMax 


A = [2,3,-2,3,-7,3,-1,-1,2]

print(suffixMax(A))
