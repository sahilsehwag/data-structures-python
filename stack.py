from linkedList import LinkedList, Node


#STACK ARRAY
class AStack:
    #CONSTRUCTOR
    def __init__(self):
        self.datastore = []
    #CONSTRUCTOR


    #METHODS
    def push(self, value):
        self.datastore.append(value)
    def pop(self): 
        if len(self.datastore) > 0:
            return self.datastore.pop(len(self.datastore) - 1)
        else: return False
    def isEmpty(self): 
        return len(self.datastore) == 0
    def top(self): 
        if len(self.datastore) > 0: 
            return self.datastore[len(self.datastore) - 1]
    def print(self):
        for i in range(len(self.datastore)):
            print(self.datastore[i], end=(' ' if i != len(self.datastore) - 1 else '\n'))
    #METHODS
#STACK


#STACK LINKEDLIST
class LStack:
    #CONSTRUCTOR
    def __init__(self):
        self.datastore = LinkedList()
    #CONSTRUCTOR


    #METHODS
    def push(self, value): 
        newNode = Node(value, self.datastore.head)
        self.datastore.head = newNode
    def pop(self): 
        nodeToDelete = self.datastore.head
        self.datastore.head = self.datastore.head.next
        return nodeToDelete.value
    def isEmpty(self): 
        return self.datastore.isEmpty()
    def top(self): 
        return self.datastore.head.value
    def print(self):
        self.datastore.print()
    #METHODS
#STACK


#CIRCULAR STACK
class CircularStack:
    pass
#CIRCULAR STACK
