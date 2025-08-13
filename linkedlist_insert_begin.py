class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a LinkedList object
ll = LinkedList()

# Insert some initial nodes
ll.insertAtBegin(10)
ll.insertAtBegin(20)

print("Before inserting at beginning:")
ll.printList()

# Now insert a new node at the beginning
ll.insertAtBegin(30)

print("After inserting 30 at beginning:")
ll.printList()
