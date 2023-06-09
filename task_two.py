from collections import deque
from queue import Queue

class Graph:

    def addEdge(self, v, w):

        global visited, adj
        adj[v].append(w)
        adj[w].append(v)

    def cityReachable(self, componentNum, src):
        global visited, adj

        queue = deque()
        queue.append(src)
        visited[src] = 1

        reachableNodes = []

        while (len(queue) > 0):
            u = queue.popleft()
            reachableNodes.append(u)

            for itr in adj[u]:
                if (visited[itr] == 0):
                    visited[itr] = 1
                    queue.append(itr)

        return reachableNodes
    
    def displayReachableNodes(self, m):

        for i in m:
            print(i, end = " ")
            print(m)
    
    def findReachableNodes(self, arr, n):

        arr = [ 2, 4, 5 ]
        n = len(arr)
        global V, adj, visited
        a = []
        componentNum = 0

        for i in range(n):
            u = arr[i]
            if (visited[u] == 0):
                componentNum += 1
                a = self.cityReachable(componentNum, u)

                print("Reachable Nodes from ", u, " are")
                print(self.displayReachableNodes(a))

    def minDistance(self, graph, source):
        Q = Queue()
        # dictionary with large distance of each node from source
        distance = {k: 9999999 for k in graph.keys()}
        visited = set()
        Q.put(source)
        visited.update({0})
        while not Q.empty():
            vertex = Q.get()
            if vertex == source:
                distance[vertex] = 0
            for u in graph[vertex]:
                if u not in visited:
                    if distance[u] > distance[vertex] + 1:
                        distance[u] = distance[vertex] + 1
                    Q.put(u)
                    visited.update({u})
        return distance

    def minSpanningTree(self):
        print("Min spanning tree")

class MainProject(Graph):

    def showFunctionality(self):
        print('London, Manchester, Liverpool, Bournemouth, Southampton, Exeter, Leeds, Cardiff')
        print('1. Searching a city from the current city, from the above list of cities.')
        print('2. The minimum distance between two cities, from the above list of cities.')
        print('3 Finding the minimum spanning tree from, from the above list of cities.')
        userInput = input("Choose an option by inputting the corresponding number: ")
        if userInput == "1":
            self.option1()
        elif userInput == "2":
            self.option2()
        else:
            self.option3()

    def option1(self):
        print("You have chosen to check if one city is reachable to another.")
        print("Input your chosen source city then your chosen destination city")
        self.cityReachable

    def option2(self):
        print("You have chosen to check the minimum distance from the source city to the destination city.")
        print("Input your chosen source city then your chosen destination city")
        self.minDistance

    def option3(self):
        print("You have chosen to to check the minimum spanning tree and total cost of the spanning tree. See below.")
        self.minSpanningTree()

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(MainProject):
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        
    def printList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def validate(self, username, password):
        current = self.head
        print(username)
        while(current):
            if (current.data['Username'] == username and current.data['Password'] == password):
                self.showFunctionality()
                break
            else:
                current = current.next
    
    def login(self):
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        self.validate(username, password)

linked_list = LinkedList()
linked_list.insert({'Username': 'Username 1', "Password": 'Password 1'})
linked_list.insert({'Username': 'Username 2', "Password": 'Password 2'})
linked_list.insert({'Username': 'Username 3', "Password": 'Password 3'})
linked_list.insert({'Username': 'Username 4', "Password": 'Password 4'})
linked_list.insert({'Username': 'Username 5', "Password": 'Password 5'})
linked_list.insert({'Username': 'Username 6', "Password": 'Password 6'})
linked_list.insert({'Username': 'Username 7', "Password": 'Password 7'})
linked_list.insert({'Username': 'Username 8', "Password": 'Password 8'})
linked_list.insert({'Username': 'Username 9', "Password": 'Password 9'})
linked_list.insert({'Username': 'Username 10', "Password": 'Password 10'})
linked_list.login()

V = 7
bfs = Graph()
adj = [[] for i in range(V + 1)]
visited = [0 for i in range(V + 1)]
bfs.addEdge(1, 2)
bfs.addEdge(2, 3)
bfs.addEdge(3, 4)
bfs.addEdge(3, 1)
bfs.addEdge(5, 6)
bfs.addEdge(5, 7)
# For every ith element in the arr
# find all reachable nodes from query[i]
arr = [ 2, 4, 5 ]
# Find number of elements in Set
n = len(arr)
#bfs.findReachableNodes(arr, n)

# graph = {0: [1, 3], 1: [0, 2, 3], 2: [4, 1, 5], 3: [4, 0, 1], 4: [2, 3, 5], 5: [4, 2]}
# print("Min distance from source for each node is")
# print(bfs.minDistance(graph, 0))