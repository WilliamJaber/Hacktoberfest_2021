#!/usr/bin/env python3
"""project: Pig Latin Script
created:2021-10-15, @author:seraph★776, email:seraph776@gmail.com, github: https://github.com/seraph776"""

class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            temp = self.head.val
            self.head = self.head.next
            self.size -= 1
            
            return self.stack.pop()
        return 'Stack is empty!'

    def peek(self):
        if not isEmpty():
            return self.stack[-1]
        return 'Stack is empty!'


    def isEmpty(self):
        return len(self.stack) == 0

    
    def getSize(self):
        return len(self.stack)




