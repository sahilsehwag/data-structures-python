#IMPORTS
from linkedlist import DoublyLinkedList
#IMPORTS


#ARRAY DEQUE
class ADeque:
    #CONSTRUCTOR
    def __init__(self):
        self.data = []
    #CONSTRUCTOR

    #METHODS
    def pushFront(self, value): 
        self.data.insert(0, value)

    def pushBack(self, value): 
        self.data.append(value)

    def popFront(self, count=1): 
        for _ in range(count):
            del self.data[0]

    def popBack(self, count=1): 
        for _ in range(count):
            self.data.pop()

    def isEmpty(self): 
        return len(self.data) == 0

    def peekFront(self, value): 
        return self.data[0]

    def peekBack(self, value): 
        return self.data[len(self.data)]

    def pushFrontAll(self, values):
        for value in values:
            self.pushFront(value)

    def pushBackAll(self, values): 
        for value in values:
            self.pushBack(value)

    def getSize(self):
        return len(self.data)
    #METHODS
#ARRAY DEQUE


#LINKEDLIST DEQUE
class LDeque:
    #CONSTRUCTOR
    def __init__(self):
        self.data = DoublyLinkedList()
    #CONSTRUCTOR

    #METHODS
    def pushFront(self, value): 
        self.data.insertAtHead(value)

    def pushBack(self, value): 
        self.data.insertAtTail(value)
        
    def popFront(self, count=1): 
        for _ in range(count):
            self.data.removeHead()

    def popBack(self, count=1):
        for _ in range(count):
            self.data.removeTail()

    def isEmpty(self, value):
        return self.data.isEmpty()

    def peekFront(self, value):
        return self.data.head.value

    def peekBack(self, value):
        return self.data.tail.value

    def pushFrontAll(self, values): 
        for value in values:
            self.pushFront(value)

    def pushBackAll(self, values): 
        for value in values:
            self.pushBack(value)

    def getSize(self):
        return self.data.length
    #METHODS
#LINKEDLIST DEQUE


#QUEUE
class Queue:
    #CONSTRUCTOR
    def __init__(self):
        self.data = ADeque()
    #CONSTRUCTOR

    #METHODS
    def enqueue(self, value): 
        self.data.pushBack(value)

    def dequeue(self): 
        self.data.popFront()

    def isEmpty(self): 
        return self.data.isEmpty()

    def peek(self, value): 
        return self.data.peekFront(value)

    def getSize(self):
        return self.data.getSize()
    #METHODS
#QUEUE


#PRIORITY QUEUE
class PriorityQueue:
    pass
#PRIORITY QUEUE


#CIRCULAR QUEUE
class CircularQueue:
    pass
#CIRCULAR QUEUE
