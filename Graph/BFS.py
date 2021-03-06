#Adjacency lists - map store keys are levels and we have a list of nodes as values 

#0 : [1,2]
#1 : [2]
#2 : [0,3]

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,source):
        visited = [False] * (max(self.graph)+1)
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            source = queue.pop(0)
            print(source, end = " ")

            for vertex in self.graph[source]:
                if visited[vertex] == False:
                    queue.append(vertex)
                    visited[vertex] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)



