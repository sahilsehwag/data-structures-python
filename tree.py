from deque import Queue

#BST
class BST:
    #NODE
    class Node:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right
    #NODE


    #CONSTRUCTOR
    def __init__(self):
        self.root = None
        self.size = 0
    #CONSTRUCTOR


    #METHODS
    def insert(self, value, root=self.root): 
        if root is None:
            root = Node(value, None, None)
            self.size += 1
        elif value <= root.value:
            insert(value, root.left)
        else:
            insert(value, root.right)
    def remove(self, node): 
        pass
    def search(self, value, root=self.root): 
        if root is None: 
            return None
        elif root.value == value:
            return root
        elif value <= root.value:
            return search(value, root.left)
        else:
            return search(value, root.right)
    def preorder(self, root=self.root, function=print): 
        if root is None: print()
        else:
            function(root.value)
            preorder(root.left)
            preorder(root.right)
    def inorder(self, root=self.root, function=print):
        if root is None: print()
        else:
            preorder(root.left)
            function(root.value)
            preorder(root.right)
    def postorder(self, root=self.root, function=print):
        if root is None: print()
        else:
            preorder(root.left)
            preorder(root.right)
            function(root.value)
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def bfs(self, function=print): 
        queue = Queue()
        queue.push(self.root)
        while not queue.isEmpty():
            node = queue.pop()
            queue.push(node.left)
            queue.push(node.right)
            function(node.value)
    def dfs(self): pass
    #METHODS
#BST


#B-TREE
class BTree:
    #CONSTRUCTOR
    def __init__(self):
        pass
    #CONSTRUCTOR


    #METHODS
    def preorder(self): pass
    def inorder(self): pass
    def postorder(self): pass
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def insert(self): pass
    def delete(self): pass
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#B-TREE


#2-3-TREE
class BTree:
    #CONSTRUCTOR
    def __init__(self):
        pass
    #CONSTRUCTOR


    #METHODS
    def preorder(self): pass
    def inorder(self): pass
    def postorder(self): pass
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def insert(self): pass
    def delete(self): pass
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#2-3-TREE


#2-3-4-TREE
class BTree:
    #CONSTRUCTOR
    def __init__(self):
        pass
    #CONSTRUCTOR


    #METHODS
    def preorder(self): pass
    def inorder(self): pass
    def postorder(self): pass
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def insert(self): pass
    def delete(self): pass
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#2-3-4-TREE


#B+ TREE
class BTree:
    #CONSTRUCTOR
    def __init__(self):
        pass
    #CONSTRUCTOR


    #METHODS
    def preorder(self): pass
    def inorder(self): pass
    def postorder(self): pass
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def insert(self): pass
    def delete(self): pass
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#B+ TREE


#B* TREE
class BTree:
    #CONSTRUCTOR
    def __init__(self):
        pass
    #CONSTRUCTOR


    #METHODS
    def preorder(self): pass
    def inorder(self): pass
    def postorder(self): pass
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def insert(self): pass
    def delete(self): pass
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#B* TREE


#AVL TREE
class BTree:
    #CONSTRUCTOR
    def __init__(self):
        pass
    #CONSTRUCTOR


    #METHODS
    def preorder(self): pass
    def inorder(self): pass
    def postorder(self): pass
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def insert(self): pass
    def delete(self): pass
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#AVL TREE


#ARRAY BINARY HEAP
class ABinaryHeap:
    #CONSTRUCTOR
    def __init__(self):
        pass
    #CONSTRUCTOR


    #METHODS
    def preorder(self): pass
    def inorder(self): pass
    def postorder(self): pass
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def insert(self): pass
    def delete(self): pass
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#ARRAY BINARY HEAP


#LINKEDLIST BINARY HEAP
class LBinaryHeap:
    #CONSTRUCTOR
    def __init__(self):
        pass
    #CONSTRUCTOR


    #METHODS
    def preorder(self): pass
    def inorder(self): pass
    def postorder(self): pass
    def getMin(self): pass
    def getMax(self): pass
    def getHeight(self): pass
    def insert(self): pass
    def delete(self): pass
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#LINKEDLIST BINARY HEAP
