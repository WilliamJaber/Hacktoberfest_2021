
from Stack import Stack
from LinkedList_Stack import LStack




def main():
    print('Regular Stack')
    s = Stack()
    s.push('Mon')
    s.push('Tue')
    s.push('Wed')
    print(s.peek())
    print(s.getSize())

    print('Linked List Stack')
    
    LinkedStack = LStack()
    print(LinkedStack.push(1))
    print(LinkedStack.push(5))
    print("Pop: ", LinkedStack.pop()) # returns 5
    print(LinkedStack.getSize())
    print(LinkedStack.push(7))
    print("Peek: ", LinkedStack.peek())
    print(LinkedStack.getSize())
    print(LinkedStack.push(8))


if __name__ == '__main__':
    main()
