#IMPORTS
from linkedlist import DoublyLinkedList
#IMPORTS


#ARRAY DEQUE
class ADeque:
    #CONSTRUCTOR
    def __init__(self):
        self.datastore = []
    #CONSTRUCTOR

    #METHODS
    def pushFront(self, value): pass
    def pushBack(self, value): pass
    def popFront(self, count=1): pass
    def popBack(self, count=1): pass
    def isEmpty(self, value): pass
    def peekFront(self, value): pass
    def peekBack(self, value): pass
    def pushFrontAll(self, values): pass
    def pushBackAll(self, values): pass
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
        self.datastore = []
    #CONSTRUCTOR

    #METHODS
    def pushFront(self, value): pass
    def pushBack(self, value): pass
    def popFront(self): pass
    def popBack(self): pass
    def isEmpty(self, value): pass
    def peekFront(self, value): pass
    def peekBack(self, value): pass
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
