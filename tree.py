from deque import Queue

#BST
class BST:
    #NODE
    class Node:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right
        def __str__(self):
            return str(self.value)
    #NODE


    #CONSTRUCTOR
    def __init__(self):
        self.root = None
        self.size = 0
    #CONSTRUCTOR


    #METHODS
    def insert(self, value): 
        self.root = self._insert(value, self.root)
    def remove(self, node): 
        return self._remove(node)
    def search(self, value): 
        return self._search(value, self.root)
    def preorder(self, function=lambda value: print(value, end=' ')): 
        self._preorder(self.root, function)
        print()
    def inorder(self, function=lambda value: print(value, end=' ')):
        self._inorder(self.root, function)
        print()
    def postorder(self, function=lambda value: print(value, end=' ')):
        self._postorder(self.root, function)
        print()
    def bfs(self, function=lambda value: print(value, end=' ')): 
        queue = Queue()
        queue.push(self.root)
        while not queue.isEmpty():
            node = queue.pop()
            queue.push(node.left)
            queue.push(node.right)
            function(node.value)
    def getParent(self, node):
        return self._getParent(node, self.root)
    def getMin(self):
        return self._getMin(self, self.root)
    def getMax(self):
        return self._getMax(self, self.root)
    #METHODS


    #PRIVATE METHODS
    def _insert(self, value, root):
        if root is None:
            self.size += 1
            newNode = self.Node(value, None, None)
            return newNode
        elif value <= root.value:
            root.left = self._insert(value, root.left)
        else:
            root.right = self._insert(value, root.right)
        return root


    def _remove(self, node):
        if node is not self.root:
            parent = self._getParent(node, self.root)

        if node.left is None and node.right is None:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None:
            if parent.left is node:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.right is None:
            if parent.left is node:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            minNode = self._getMin(node.right)
            minNode = self.remove(minNode)

            if node is self.root:
                self.root = minNode
            else:
                if parent.left is node:
                    parent.left = minNode
                else:
                    parent.right = minNode

            minNode.left = node.left
            minNode.right = node.right

        return node


    def _search(self, value, root):
        if root is None: 
            return
        elif root.value == value:
            return root
        elif value <= root.value:
            return self._search(value, root.left)
        else:
            return self._search(value, root.right)


    def _preorder(self, root, function):
        if root is None: return
        else:
            function(root.value)
            self._preorder(root.left, function=function)
            self._preorder(root.right, function=function)


    def _inorder(self, root, function):
        if root is None: return
        else:
            self._inorder(root.left, function)
            function(root.value)
            self._inorder(root.right, function)


    def _postorder(self, root, function):
        if root is None: return
        else:
            self._postorder(root.left, function)
            self._postorder(root.right, function)
            function(root.value)


    def _getParent(self, node, root):
        if root is None: 
            return
        elif root.left is node or root.right is node:
            return root
        elif node.value <= root.value:
            return self._getParent(node, root.left)
        else:
            return self._getParent(node, root.right)


    def _getMin(self, root):
        if root.left is None:
            return root
        else:
            return self._getMin(root.left)


    def _getMax(self, root):
        if root.right is None:
            return root
        else:
            return self._getMax(root.right)
    #PRIVATE METHODS


    #MAGIC METHODS
    #MAGIC METHODS
#BST


#B-TREE
class BTree:
    pass
#B-TREE


#2-3-TREE
class To3Tree:
    pass
#2-3-TREE


#2-3-4-TREE
class To34Tree:
    pass
#2-3-4-TREE


#B+ TREE
class BPlusTree:
    pass
#B+ TREE


#B* TREE
class BStarTree:
    pass
#B* TREE


#AVL TREE
class AVLTree:
    pass
#AVL TREE


#ARRAY BINARY HEAP
class ABinaryHeap:
    pass
#ARRAY BINARY HEAP


#LINKEDLIST BINARY HEAP
class LBinaryHeap:
    pass
#LINKEDLIST BINARY HEAP
