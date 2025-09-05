class Node:
    def __init__(self, data):
        self.data = data      # Store the value
        self.next = None      # Pointer to the next node
        self.prev = None      # Pointer to the previous node


# Define a Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None   # Head pointer

    # Function to insert a node at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)

        if self.head is None:     # If list is empty
            self.head = new_node
        else:
            new_node.next = self.head   # Link new node to current head
            self.head.prev = new_node   # Link current head back to new node
            self.head = new_node        # Move head to new node

    # Function to delete a node at the beginning
    def deleteAtBegin(self):
        if self.head is None:   # If list is empty
            print("Doubly Linked List is empty")
            return

        if self.head.next is None:   # If only one node exists
            self.head = None
        else:
            self.head = self.head.next   # Move head to next node
            self.head.prev = None        # Break previous link

    # Function to print list forward
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Create a DoublyLinkedList object
dll = DoublyLinkedList()

# Insert some initial nodes (at beginning)
dll.insertAtBegin(10)   # List: 10 <-> None
dll.insertAtBegin(20)   # List: 20 <-> 10 <-> None
dll.insertAtBegin(30)   # List: 30 <-> 20 <-> 10 <-> None

print("Before deleting at beginning:")
dll.printList()         # Output: 30 <-> 20 <-> 10 <-> None

# Delete the first node
dll.deleteAtBegin()

print("After deleting at beginning:")
dll.printList()         # Output: 20 <-> 10 <-> None
