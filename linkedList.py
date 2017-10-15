

#SINGLY LINKED LIST
class LinkedList:
    #NODE
    class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value)
    #NODE


    #CONSTRUCTOR
    def __init__(self):
        self.head = None
        self.length = 0
    #CONSTRUCTOR


    #METHODS
    def insertAtHead(self, value):
        if self.head is None:
            self.head = self.Node(value, None)
        else:
            newNode = self.Node(value, self.head)
            self.head = newNode
        self.length += 1


    def insertAtTail(self, value):
        if self.head is None:
            self.head = self.Node(value, None)
        else:
            tail = self.getNodeAt(self.length - 1)
            newNode = self.Node(value, None)
            tail.next = newNode
        self.length += 1


    def insertAt(self, value, position):
        if position < 0 or position > self.length:
            return False
        elif position is 0:
            self.insertAtHead(value)
        elif position is self.length:
            self.insertAtTail(value)
        else:
            previousNode = self.getNodeAt(position - 1)
            nextNode = previousNode.next
            newNode = self.Node(value, nextNode)
            previousNode.next = newNode

            self.length += 1


    def remove(self, node):
        position = self.getPosition(node)
        self.removeAt(position)
    def removeAt(self, position):
        if position is 0:
            nodeToRemove = self.head
            self.head = self.head.next
        elif position is self.length - 1:
            prevNode = self.getNodeAt(position - 1)
            nodeToRemove = prevNode.next
            prevNode.next = None
        else:
            node = self.getNodeAt(position - 1)
            nodeToRemove = node.next
            node.next = nodeToRemove.next
        del nodeToRemove
        self.length -= 1


    def getPosition(self, node):
        temp = self.head
        position = 0
        while temp.next is not None:
            if temp is node: return position
            position += 1
            temp = temp.next
        return -1


    def getNodeAt(self, position, count=1):
        temp = self.head 
        if position > self.length: return None
        else:
            for _ in range(position):
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
        if self.length is 0 or self.length is 1: return

        previousNode = self.head
        currentNode = previousNode.next
        nextNode = currentNode.next
        previousNode.next = None

        while currentNode is not None:
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

            if currentNode is None: break
            else:
                nextNode = currentNode.next
        self.head = previousNode


    def recursiveReverse(self):
        self._recursiveReverse(None, self.head, self.head.next)
    #METHODS


    #PRIVATE METHODS
    def _recursiveReverse(self, previous, current, next):
        if self.head == None: 
            return
        elif current.next == None:
            current.next = previous
            self.head = current
            return
        else:
            current.next = previous
            self._recursiveReverse(self, current, next, next.next)
    #PRIVATE METHODS


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
    #NODE
    class Node:
        def __init__(self, value, prev, next):
            self.value = value
            self.next = next
            self.prev = prev

        def __str__(self):
            return str(self.value)
    #NODE


    #CONSTRUCTOR
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
    #CONSTRUCTOR


    #METHODS
    def insertAt(self, position, value):
        if position > self.length:
            print('INVALID POSITION')
            return
        elif self.head is None:
            newNode = self.Node(value, None, None)
            self.head = newNode
        elif self.length == 1:
            if position == 0:
                newNode = self.Node(value, None, self.head)
                self.tail = self.head
                self.head = newNode
                self.tail.prev = newNode
            else:
                newNode = self.Node(value, self.head, None)
                self.tail = newNode
                self.head.next = self.tail
        elif position == 0:
            newNode = self.Node(value, None, self.head)
            self.head = newNode
        elif position == self.length:
            newNode = self.Node(value, self.tail, None)
            self.tail.next = newNode
            self.tail = newNode
        else:
            previous = self.getNodeAt(position - 1)
            next = previous.next

            newNode = self.Node(value, previous, next)
            previous.next = newNode
            next.prev = newNode

        self.length += 1


    def insertAtHead(self, value):
        self.insertAt(0, value)
    def insertAtTail(self, value):
        self.insertAt(self.length, value)
    def remove(self, node):
        position = self.getNodePosition(node.value)
        self.removeAt(position)
    def removeAt(self, position):
        if position >= self.length: print('INVALID POSITION')
        elif self.length == 1:
            del self.head
            self.head = None
        elif position == 0:
            current = self.head
            next = self.head.next
            next.prev = None
            self.head = next

            del current
        elif position == self.length - 1:
            prev = self.getNodeAt(position - 1)
            current = prev.next
            prev.next = None
            self.tail = prev

            del current
        else: 
            prev = self.getNodeAt(position - 1)
            current = prev.next
            next = current.next

            prev.next = next
            next.prev = prev
            del current

        self.length -= 1
    def removeHead(self):
        self.removeAt(0)
    def removeTail(self):
        self.remoteAt(self.length - 1)
    def getNodeAt(self, position):
        if position >= self.length: return

        temp = self.head
        for _ in range(position):
            temp = temp.next
        return temp


    def getNodePosition(self, value):
        temp = self.head

        for i in range(self.length):
            if temp.value == value: return i

        return None


    def reverse(self):
        previous = None
        current = self.head
        next = current.next

        while True:
            if self.head == None: 
                return
            elif current.next == None:
                current.next = previous
                self.head = current
                return
            else:
                current.next = previous

                previous = current
                current = next
                next = next.next


    def recursiveReverse(self):
        self._recursiveReverse(None, self.head, self.head.next)
    def isEmpty(self):
        return self.length == 0
    #METHODS

    #PRIVATE METHODS
    def _recursiveReverse(self):
        pass
    #PRIVATE METHODS


    #MAGICAL METHODS
    def __str__(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=('\n' if temp.next is None else ' <-> '))
            temp = temp.next
        return ''
    def __len__(self):
        return self.length
    #MAGICAL METHODS
#DOUBLY LINKED LIST


#CIRCULAR LINKED LIST
class CircularLinkedList:
    #NODE
    class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next


        def __str__(self):
            return str(self.value)
    #NODE


    #CONSTRUCTOR
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
    #CONSTRUCTOR


    #METHODS
    def insertAt(self, position, value):
        if position < 0 or position > self.length:
            print('INVALID POSITION')
            return
        elif self.length is 1 and position <= 1:
            if position is 0:
                newNode = self.Node(value, self.head)
                self.tail = self.head
                self.head = newNode

                self.tail.next = self.head
            elif position is 1:
                newNode = self.Node(value, self.head)
                self.head.next = newNode
                self.tail = newNode
        elif position is 0:
            if self.length == 0:
                newNode = self.Node(value, None)
                newNode.next = None
                self.head = newNode
            else:
                newNode = self.Node(value, self.head)
                self.tail.next = newNode
                self.head = newNode
        elif position is self.length - 1:
            prev = self.getNodePosition(position - 1)
            newNode = self.Node(value, self.tail)
            prev.next = newNode
        elif position is self.length:
            prev = self.tail
            newNode = self.Node(value, self.head)
            prev.next = newNode
            self.tail = newNode
        else:
            previous = self.getNodeAt(position - 1)
            next = previous.next
            newNode = self.Node(value, next)
            previous.next = newNode

        self.length += 1


    def insertAtHead(self, value):
        self.insertAt(0, value)


    def insertAtTail(self, value):
        self.insertAt(self.length, value)


    def remove(self, node):
        position = self.getNodePosition(node)
        self.removeAt(position)
    def removeAt(self, position):
        if position is 0:
            nodeToRemove = self.head
            self.head = self.head.next
        elif position is self.length - 1:
            prevNode = self.getNodeAt(position - 1)
            nodeToRemove = prevNode.next
            prevNode.next = None
        else:
            node = self.getNodeAt(position - 1)
            nodeToRemove = node.next
            node.next = nodeToRemove.next
        del nodeToRemove
        self.length -= 1

    def removeHead(self):
        self.removeAt(0)


    def removeTail(self):
        self.removeAt(self.length - 1)


    def getNodeAt(self, position):
        if position >= self.length: return
        else:
            temp = self.head
            for _ in range(position):
                temp = temp.next
            return temp


    def getNodePosition(self, node):
        temp = self.head
        for i in range(self.length - 1):
            if temp is node:
                return i
            temp = temp.next
        return


    def isEmpty(self):
        return self.length == 0


    def reverse(self):
        pass


    def recursiveReverse(self):
        self._recursiveReverse(None, self.head, self.head.next)
    #METHODS


    #PRIVATE METHODS
    def _recursiveReverse(self, previous, current, next):
        if self.head == None: 
            return
        elif current is self.head:
            next = current.next
            current.next = self.tail
            self._recursiveReverse(current, next, next.next)
        elif current is self.tail:
            current.next = previous
            self.head.next = self.tail
            self.tail = self.head
            self.head = current
            return
        else:
            current.next = previous
            self._recursiveReverse(current, next, next.next)
    #PRIVATE METHODS


    #MAGICAL METHODS
    def __str__(self):
        temp = self.head
        while True:
            print(temp.value, end=('\n' if temp.next is self.head else ' -> '))
            temp = temp.next
            if temp is self.head: break
        return ''
    def __len__(self):
        return self.length
    #MAGICAL METHODS
#CIRCULAR LINKED LIST
