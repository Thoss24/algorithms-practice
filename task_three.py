from collections import deque
from threading import Thread

# graph = {
#   '5' : {'3', '7'}, #assign each city a number value. i.e, ask user "To select London as source press 1, and to choose exeter as destination choose 2"
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

# visited = [] # List for visited nodes.
# queue = []     #Initialize a queue

# def bfs(visited, graph, node): #function for BFS
#   visited.append(node)
#   queue.append(node)

#   while queue:          # Creating loop to visit each node
#     m = queue.pop(0) 
#     print (m, end = " ") 

#     for city in graph[m]:
#       if city not in visited:
#         visited.append(city)
#         queue.append(city)

# # Driver Code
# print("Following is the Breadth-First Search")
# bfs(visited, graph, '5')    # function calling

# #Python3 program to find all the reachable nodes
# #for every node present in arr[0..n-1]
 
# def addEdge(v, w):
     
#     global visited, adj
#     adj[v].append(w)
#     adj[w].append(v)
 
# def BFS(componentNum, src):
     
#     global visited, adj
     
#     # Mark all the vertices as not visited
#     # Create a queue for BFS
#     #a =  visited
#     queue = deque()
 
#     queue.append(src)
 
#     # Assign Component Number
#     visited[src] = 1
 
#     # Vector to store all the reachable
#     # nodes from 'src'
#     reachableNodes = []
#     #print("0:",visited)
 
#     while (len(queue) > 0):
         
#         # Dequeue a vertex from queue
#         u = queue.popleft()
 
#         reachableNodes.append(u)
 
#         # Get all adjacent vertices of the dequeued
#         # vertex u. If a adjacent has not been visited,
#         # then mark it visited and enqueue it
#         for itr in adj[u]:
#             if (visited[itr] == 0):
                 
#                 # Assign Component Number to all the
#                 # reachable nodes
#                 visited[itr] = 1
#                 queue.append(itr)
 
#     return reachableNodes
 
# # Display all the Reachable Nodes
# # from a node 'n'
# def displayReachableNodes(m):
     
#     for i in m:
#         print(i, end = " ")
 
#     print()
 
# def findReachableNodes(arr, n):
     
#     global V, adj, visited
     
#     # Get the number of nodes in the graph
 
#     # Map to store list of reachable Nodes for a
#     # given node.
#     a = []
 
#     # Initialize component Number with 0
#     componentNum = 0
 
#     # For each node in arr[] find reachable
#     # Nodes
#     for i in range(n):
#         u = arr[i]
 
#         # Visit all the nodes of the component
#         if (visited[u] == 0):
#             componentNum += 1
 
#             # Store the reachable Nodes corresponding
#             # to the node 'i'
#             a = BFS(componentNum, u)
 
#         # At this point, we have all reachable nodes
#         # from u, print them by doing a look up in map m.
#         print("Reachable Nodes from ", u, " are")
#         displayReachableNodes(a)
 
# # Driver code
# if __name__ == '__main__':
     
#     V = input("number: ")
#     adj = [[] for i in range(V + 1)]
#     visited = [0 for i in range(V + 1)]
#     addEdge(1, 2)
#     addEdge(2, 3)
#     addEdge(3, 4)
#     addEdge(3, 1)
#     addEdge(5, 6)
#     addEdge(5, 7)
 
#     # For every ith element in the arr
#     # find all reachable nodes from query[i]
#     arr = [ 2, 4, 5 ]
 
#     # Find number of elements in Set
#     n = len(arr)
 
#     findReachableNodes(arr, n)

class Prims:

    def __init__(self, n, graph):
        self.n = n
        self.graph = graph

    def Prims(self):
        inf = 9999999 # number of vertices in graph
        selected_node = [0, 0, 0, 0, 0]
        no_edge = 0
        selected_node[0] = True

        while (no_edge < self.n - 1):
            minimum = inf
            a = 0
            b = 0
            for m in range(self.n):
                if selected_node[m]:
                    for n in range(self.n):
                        if ((not selected_node[n]) and self.graph[m][n]):
                            if minimum > self.graph[m][n]:
                                minimum = self.graph[m][n]
                                a = m
                                b = n
            print("Edge : Weight\n")
            print(str(a) + "-" + str(b) + ":" + str(self.graph[a][b]))
            selected_node[b] = True
            no_edge += 1


class Kruskals:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    # function to add edge to graph    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        print(self.graph)

    def find(self, parent, i):
        if parent[i] != i:

            # reassign nodes parent
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, x, y):

        # attach smaller rank tree
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        else:
            parent[y] = x
            rank[x] += 1

    def KruskalsMST(self):
        # to store result
        resultMST = []
        # to store edges
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while e < self.vertices - 1:

            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            #if including edge does not cause cycle, include it in result and increment the index for next edge
            if x != y:
                e = e + 1
                resultMST.append([u, v, w])
                self.union(parent, rank, x, y)

            minCost = 0
            for u, v, weight in resultMST:
                minCost += weight
                print(u, v, weight)
                print("Min spanning tree", minCost)

graph = [[0, 19, 5, 0, 0],
         [19, 0, 5, 9, 2],
         [5, 5, 0, 1, 6],
         [0, 9, 1, 0, 1],
         [0, 2, 6, 1, 0]]

prims = Prims(5, graph)
kruskals = Kruskals(4)

kruskals.addEdge(0, 1, 10)
kruskals.addEdge(0, 2, 6)
kruskals.addEdge(0, 3, 5)
kruskals.addEdge(1, 3, 15)
kruskals.addEdge(2, 3, 4)

kruskals.KruskalsMST()

# if __name__ == '__main__':
#     Thread(target= prims.Prims).start()
#     Thread(target= kruskals.kruskalsMST).start()