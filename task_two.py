
class Graph:

    def cityReachable(self):
        print("City reachable")
        input("Source city: ")
        input("Destination city: ")

    def minDistance(self):
        print("Min distance")

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
        self.cityReachable()

    def option2(self):
        print("You have chosen to check the minimum distance from the source city to the destination city.")
        print("Input your chosen source city then your chosen destination city")
        self.minDistance()

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


# linked_list = LinkedList()
# linked_list.insert({'Username': 'Username 1', "Password": 'Password 1'})
# linked_list.insert({'Username': 'Username 2', "Password": 'Password 2'})
# linked_list.insert({'Username': 'Username 3', "Password": 'Password 3'})
# linked_list.insert({'Username': 'Username 4', "Password": 'Password 4'})
# linked_list.insert({'Username': 'Username 5', "Password": 'Password 5'})
# linked_list.insert({'Username': 'Username 6', "Password": 'Password 6'})
# linked_list.insert({'Username': 'Username 7', "Password": 'Password 7'})
# linked_list.insert({'Username': 'Username 8', "Password": 'Password 8'})
# linked_list.insert({'Username': 'Username 9', "Password": 'Password 9'})
# linked_list.insert({'Username': 'Username 10', "Password": 'Password 10'})

# linked_list.login()