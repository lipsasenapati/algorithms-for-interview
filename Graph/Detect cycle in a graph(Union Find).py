from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def findParent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.findParent(parent, parent[i])
    
    def union(self, parent, x, y):
        parent[x]=y

    def isCyclic(self):
        parent = [-1]*self.V
        for i in self.graph:
            for j in self.graph[i]:
                x = self.findParent(parent, i)
                y = self.findParent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)

g = Graph(3)

g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")