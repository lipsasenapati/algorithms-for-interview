# The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) 
# and explores as far as possible along each branch before backtracking. 
# So the basic idea is to start from the root or any arbitrary node and mark the node and move to the adjacent unmarked node 
# and continue this loop until there is no unmarked adjacent node. Then backtrack and check for other unmarked nodes and traverse them. 

# from collections import defaultdict 
#not using a hash for dfs decreases look up time from O(n) to O(1)
# use set for DFS and hashmap for BFS

class GraphDFS:
    # def __init__(self):
    #     self.graph = defaultdict(list)

    def __init__(self, V):
        self.V = V #no. of vertices
        self.adj = [[] for i in range(V)] #adjacency lists

    def addEdge(self, u, v):
        self.adj[u].append(v)

    # DFS for a given source
    # def DFS(self, source):
    #     visited = [False for i in range(self.V)]
    #     stack = []
    #     stack.append(source)

    #     while(len(stack)):
    #         source = stack[-1]
    #         stack.pop()
    #         if (not visited[source]):
    #             print(source, end=" ")
    #             visited[source] = True
        
    #         for vertex in self.adj[source]:
    #             if (not visited[vertex]):
    #                 stack.append(vertex)


    def DFSUtil(self, source, visited):
        stack = []
        stack.append(source)

        while (len(stack)):
            source = stack.pop()
            
            if (not visited[source]):
                visited[source] = True
                print(source, end = " ")

            
            for vertex in range(len(self.adj[source])):
                if (not visited[vertex]):
                    stack.append(vertex)




    def DFS(self):
        visited = [False] * self.V
        for i in range(self.V):
            if (not visited[i]):
                self.DFSUtil(i, visited)

# g = GraphDFS(5); # Total 5 vertices in graph
# g.addEdge(1, 0);
# g.addEdge(0, 2);
# g.addEdge(2, 1);
# g.addEdge(0, 3);
# g.addEdge(1, 4);
 
# print("Following is Depth First Traversal")
# g.DFS(0) # calling DFS from a given source

if __name__ == '__main__':
     
    g = GraphDFS(5) # Total 5 vertices in graph
    g.addEdge(1, 0)
    g.addEdge(2, 1)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
 
    print("Following is Depth First Traversal")
    g.DFS()