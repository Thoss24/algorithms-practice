adjacency_list = {'A': set([('C', 15), ('B', 2), ('G', 11)]),
                  'B': set([('A', 2), ('F', 6), ('D', 5)]),
                  'C': set([('A', 15), ('D', 18)]),
                  'D': set([('C', 18), ('B', 5), ('E', 6), ('K', 11)]),
                  'E': set([('F', 5), ('I', 13), ('K', 12), ('D', 6)]),
                  'F': set([('B', 6), ('H', 1), ('E', 5)]),
                  'G': set([('A', 11), ('H', 3)]),
                  'H': set([('G', 3), ('F', 1)]),
                  'I': set([('E', 13), ('J', 5)]),
                  'J': set([('I', 5), ('K', 37)])}

my_list = []

def add_node(node):
    if node not in my_list:
        my_list.append(node)
    else:
        print("Node", node, "already exists")

def add_edge(node1, node2):
    temp = []
    if node1 in my_list and node2 in my_list:
        if node1 not in adjacency_list:
            temp.append(node2)
            adjacency_list[node1] = temp

        elif node1 in adjacency_list:
            temp.extend(adjacency_list[node1])
            temp.append(node2)
            adjacency_list[node1] = temp
    else:
        print("Node does not exist")

def graph():
    for node in adjacency_list:
        print(node, "--->", [i for i in adjacency_list[node]])

add_node(2)

graph()

# print(adjacency_list)