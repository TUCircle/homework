#!/usr/bin/env python2
#-*- coding: utf-8 -*-

numbers = [1,2,3,4,5,6,7,8,9,10]

class App:
  def __init__(self):
    # Erstelle Stack
    self.s = Stack()
    # ERstelle Warteschlange
    self.q = Queue()
    self.l = len(numbers)
    counter = 1
    # gebe Stack mit Nummern aus 
    for i in numbers:
      print("Element %s im Stack: %s" % (counter, i))
      self.s.push(i)
      counter += 1
    self.main()

  def main(self):
    counter = 1
    print("")
    print("Packe Elemente vom Stack in die Warteschlange")
    # Nutze Warteschlange zum umkehren des Stacks
    for i in xrange(0, self.l):
      print("Element %s in der Warteschlange: %s" % (counter, self.s.peek()))
      self.q.enqueue(self.s.pop())
      counter += 1
    print("")
    print("Packe Elemente wieder zurück")
    counter = 1
    # packe wieder alles auf den Stack
    for i in xrange(0, self.l):
      print("Element %s in der Warteschlange: %s" % (counter, self.q.first()))
      self.s.push(self.q.dequeue())
      counter += 1

# Klasse Stack
class Stack :
 
  def __init__(self) :       
    self.items = [] 
 
  def push(self, item) : 
    self.items.append(item) 
 
  def pop(self) : 
    return self.items.pop() 

  def peek(self):
    return self.items[len(self.items)-1]
 
  def isEmpty(self) : 
    return (self.items == [])  

  def size(self):
    return len(self.items)


# Klasse Warteschlange
class Queue : 
  def __init__(self) :
    self.items = [] 
 
  def enqueue(self, item) : 
    self.items.append(item) 
 
  def dequeue(self) : 
    return self.items.pop(0) 

  def first(self):
    return self.items[0]
 
  def isEmpty(self) : 
    return (self.items == [])  

App = App()
