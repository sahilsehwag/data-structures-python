#NODE
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
#NODE


#SINGLY LINKED LIST
class LinkedList:
    #CONSTRUCTOR
    def __init__(self):
        self.head = None
        self.length = 0
    #CONSTRUCTOR


    #METHODS
    def insertAtHead(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            newNode = Node(value, self.head)
            self.head = newNode
        self.length += 1
    def insertAtTail(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            tail = self.getAt(self.length)
            newNode = Node(value, None)
            tail.next = newNode
        self.length += 1
    def insertAtPos(self, value, position):
        node = get(position - 1)
        nextNode = node.next
        newNode = Node(value, nextNode)
        node.next = newNode

        self.length += 1
    def remove(self, node):
        position = getPosition(node)
        prevNode = getAt(position - 1)
        prevNode.next = node.next
        del node

        self.length -= 1
    def removeAt(self, position):
        node = self.getAt(position - 1)
        nodeToRemove = node.next
        node.next = nodeToRemove.next
        del nodeToRemove
        self.length -= 1
    def getPosition(self, node):
        temp = self.head
        position = 1
        while temp.next is not None:
            if temp is node: return position
            position += 1
            temp = temp.next
        return -1
    def get(self, position, count=1):
        temp = self.head 
        if position > self.length: None
        else:
            for _ in range(position - 1):
                temp = temp.next
            if count is 1: return temp
            else:
                nodes = []
                for _ in range(count):
                    nodes.append(temp)
                    temp = temp.next
                    if temp is None: break
                return nodes
    def getFirstMatch(self, value):
        temp = self.head
        while temp.next is not None:
            if temp.value == value: return temp
            temp = temp.next
    def isEmpty(self):
        return self.head is None
    def reverse(self):
        pass
    def reverseRecursive(self):
        pass
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=('\n' if temp.next is None else ' -> '))
            temp = temp.next
    def printRecursive(self):
        pass
    #METHODS


    #MAGICAL METHODS
    def __str__(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=('\n' if temp.next is None else ' -> '))
            temp = temp.next
        return ''
    def __len__(self):
        return self.length
    #MAGICAL METHODS
#SINGLY LINKED LIST


#DOUBLY LINKED LIST
class DoublyLinkedList:
    #CONSTRUCTOR
    def __init__(self):
        self.head = None
        self.length = 0
    #CONSTRUCTOR


    #METHODS
    def insertAtHead(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            newNode = Node(value, self.head)
            self.head = newNode
        self.length += 1
    def insertAtTail(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            tail = self.getAt(self.length)
            newNode = Node(value, None)
            tail.next = newNode
        self.length += 1
    def insertAtPos(self, value, position):
        node = get(position - 1)
        nextNode = node.next
        newNode = Node(value, nextNode)
        node.next = newNode

        self.length += 1
    def remove(self, node):
        position = getPosition(node)
        prevNode = getAt(position - 1)
        prevNode.next = node.next
        del node

        self.length -= 1
    def removeAt(self, position):
        node = self.getAt(position - 1)
        nodeToRemove = node.next
        node.next = nodeToRemove.next
        del nodeToRemove
        self.length -= 1
    def getPosition(self, node):
        temp = self.head
        position = 1
        while temp.next is not None:
            if temp is node: return position
            position += 1
            temp = temp.next
        return -1
    def get(self, position, count=1):
        temp = self.head 
        if position > self.length: None
        else:
            for _ in range(position - 1):
                temp = temp.next
            if count is 1: return temp
            else:
                nodes = []
                for _ in range(count):
                    nodes.append(temp)
                    temp = temp.next
                    if temp is None: break
                return nodes
    def getFirstMatch(self, value):
        temp = self.head
        while temp.next is not None:
            if temp.value == value: return temp
            temp = temp.next
    def isEmpty(self):
        return self.head is None
    def reverse(self):
        pass
    def reverseRecursive(self):
        pass
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=('\n' if temp.next is None else ' -> '))
            temp = temp.next
    def printRecursive(self):
        pass
    #METHODS


    #MAGICAL METHODS
    def __str__(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=('\n' if temp.next is None else ' -> '))
            temp = temp.next
        return ''
    def __len__(self):
        return self.length
    #MAGICAL METHODS
#DOUBLY LINKED LIST


#CIRCULAR LINKED LIST
class CircularLinkedList:
    #CONSTRUCTOR
    def __init__(self):
        self.head = None
        self.length = 0
    #CONSTRUCTOR


    #METHODS
    def insertAtHead(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            newNode = Node(value, self.head)
            self.head = newNode
        self.length += 1
    def insertAtTail(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            tail = self.getAt(self.length)
            newNode = Node(value, None)
            tail.next = newNode
        self.length += 1
    def insertAtPos(self, value, position):
        node = get(position - 1)
        nextNode = node.next
        newNode = Node(value, nextNode)
        node.next = newNode

        self.length += 1
    def remove(self, node):
        position = getPosition(node)
        prevNode = getAt(position - 1)
        prevNode.next = node.next
        del node

        self.length -= 1
    def removeAt(self, position):
        node = self.getAt(position - 1)
        nodeToRemove = node.next
        node.next = nodeToRemove.next
        del nodeToRemove
        self.length -= 1
    def getPosition(self, node):
        temp = self.head
        position = 1
        while temp.next is not None:
            if temp is node: return position
            position += 1
            temp = temp.next
        return -1
    def get(self, position, count=1):
        temp = self.head 
        if position > self.length: None
        else:
            for _ in range(position - 1):
                temp = temp.next
            if count is 1: return temp
            else:
                nodes = []
                for _ in range(count):
                    nodes.append(temp)
                    temp = temp.next
                    if temp is None: break
                return nodes
    def getFirstMatch(self, value):
        temp = self.head
        while temp.next is not None:
            if temp.value == value: return temp
            temp = temp.next
    def isEmpty(self):
        return self.head is None
    def reverse(self):
        pass
    def reverseRecursive(self):
        pass
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=('\n' if temp.next is None else ' -> '))
            temp = temp.next
    def printRecursive(self):
        pass
    #METHODS


    #MAGICAL METHODS
    def __str__(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=('\n' if temp.next is None else ' -> '))
            temp = temp.next
        return ''
    def __len__(self):
        return self.length
    #MAGICAL METHODS
#CIRCULAR LINKED LIST
