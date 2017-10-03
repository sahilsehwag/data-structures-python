import math
from deque import Queue


#EDGE LIST
class ELGraph:
    #NODE
    class Node:
        def __init__(self, value, nodes=[]):
            self.value = value
            self.edges = edges
    class Edge:
        def __init__(self, source, destination, weight=1):
            self.source = source
            self.destination = destination
    #NODE


    #CONSTRUCTOR
    def __init__(self, edges=[]):
        self.edges = []
    #CONSTRUCTOR


    #METHODS
    #METHODS
#EDGE LIST


#ADJANCEY MATRIX
class AMGraph:
    #NODE
    class Node:
        def __init__(self, value, nodes=[]):
            self.value = value
            self.edges = edges
    class Edge:
        def __init__(self, source, destination, weight=1):
            self.source = source
            self.destination = destination
    #NODE


    #CONSTRUCTOR
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.matrix = [[0 for _ in range(len(self.nodes))] for _ in range(len(self.nodes))]
        for i, node in enumerate(self.nodes):
            for adjacentEdge in node.edges:
                adjacentNode = adjacentEdge.source if adjacentEdge.source is not node else adjacentEdge.destination
                j = self.nodes.index(adjacentNode)
                self.matrix[i][j] = adjacentEdge.weight
    #CONSTRUCTOR


    #METHODS
    def bfs(self): pass
    def dfs(self): pass
    #METHODS
#ADJANCEY MATRIX


#ADJANCEY LIST
class ALGraph:
    #NODE
    class Node:
        def __init__(self, value, nodes=[], edges=[]):
            self.value = value
            self.edges = edges
        def getAdjacentNode(self, edge):
            return edge.source if edge.source is not self else edge.destination
        def getAdjacentNodes(self):
            return [self.getAdjacentNode(edge) for edge in self.edges]
    class Edge:
        def __init__(self, source, destination, weight=1):
            self.source = source
            self.destination = destination
    #NODE


    #CONSTRUCTOR
    def __init__(self, nodes=[]):
        self.nodes = nodes
    #CONSTRUCTOR


    #METHODS
    def bfs(self): pass
    def dfs(self): pass
    def djikstra(self, source, destination): 
        visitedFlags = [False for _ in range(len(self.nodes))]
        distances = [math.inf for _ in range(len(self.nodes))]
        distances[self.nodes.index(source)] = 0
        shortestPath = [source]
        queue = Queue()
        queue.push(source)

        while not queue.isEmpty():
            #removing node from queue
            node = queue.pop()
            nodeIndex = self.nodes.index(node)

            minNode = None
            minNodeIndex = None
            for adjacentEdge in node.edges:
                #getting adjacent nodes
                adjacentNode = node.getAdjacentNode(adjacentEdge)
                adjNodeIndex = self.nodes.index(adjacentNode)

                #adding unvisited adjacent nodes to queue
                if visitedFlags[adjNodeIndex] is False:
                    queue.push(adjacentNode)
                    visitedFlags[adjNodeIndex] = True

                #updating shortest distance of adjacent node
                if adjacentEdge.weight + distances[nodeIndex] <= distances[adjNodeIndex]:
                    distances[adjNodeIndex] = adjacentEdge.weight + distances[nodeIndex]

                #setting node with least weight
                if minNode is None or distances[adjNodeIndex] < distances[minNodeIndex]:  
                    minNode = adjacentNode
                    minNodeIndex = adjNodeIndex
            shortestPath.append(minNode)
    def __removeLoops(self): pass
    def __removeParallelEdges(self): pass
    def bellmanFord(self): pass
    def isBipartite(self): pass
    def hasCycle(self): pass
    def shortestPath(self, algorithm='djikstra'): pass
    #METHODS
#ADJANCEY LIST
