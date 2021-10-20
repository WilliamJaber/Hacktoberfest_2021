#!/usr/bin/env python3
"""project: Pig Latin Script
created:2021-10-15, @author:seraph★776, email:seraph776@gmail.com, github: https://github.com/seraph776"""

class Stack:
    
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return 'Stack is empty!'

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return 'Stack is empty!'

    
    def getSize(self):
        return len(self.stack)


            
def main():
    s = Stack()
    print(s.isEmpty())
    s.push('Mon')
    s.push('Tue')
    s.push('Wed')        
    print(s.isEmpty())
    s.pop()
    s.push('Thr')    
    s.push('Fri')
    print(s.peek())
    s.push('Sat')
    s.push('Sun') 
    print(s.view())


if __name__ == '__main__':
    main()


