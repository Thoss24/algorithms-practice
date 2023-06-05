
class MainProject():

    def showFunctionality(self):
        print('1. Searching a city from the current city')
        print('2. The minimum distance between two cities')
        print('3 FInding the minimum spanning tree')
        userInput = input("Choose an option by inputting the corresponding number: ")

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

# class Credentials(LinkedList):

#     def login(self):
#         username = input('Enter Username: ')
#         password = input('Enter Password: ')
#         self.validate(username, password)

      

linked_list = LinkedList()
#credentials = Credentials()
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