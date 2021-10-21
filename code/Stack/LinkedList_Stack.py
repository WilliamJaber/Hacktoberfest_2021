#!/usr/bin/env python3
"""
project:
created:2021-10-15
@author:Seraph★VI
email:seraph776@gmail.com
github: https://github.com/seraph776

"""

class Node:

  def __init__(self, val):
    self.val = val
    self.next = next


class LStack:

  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, val):
    node = Node(val)
    node.next = self.head
    self.head = node
    self.size += 1
    return self.size
  
  def pop(self):
    if not self.isEmpty():
      temp = self.head.val
      self.head = self.head.next
      self.size -= 1
      return temp
    raise  "Empty stack"
  
  def peek(self):
    if not self.isEmpty():
      return self.head.val
    raise "Empty stack"
  
  def isEmpty(self):
    return self.size==0 
    
  def getSize(self):
    return self.size
