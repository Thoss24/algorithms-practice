graph = {
  '5' : {'3', '7'}, #assign each city a number value. i.e, ask user "To select London as source press 1, and to choose exeter as destination choose 2"
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for city in graph[m]:
      if city not in visited:
        visited.append(city)
        queue.append(city)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling