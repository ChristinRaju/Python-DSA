# Node class: represents one box (node) in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data    # Store the actual data value
        self.next = None    # Pointer to the next node (initially None)
        self.prev = None    # Pointer to the previous node (initially None)


# DoublyLinkedList class: manages the nodes and operations
class DoublyLinkedList:
    def __init__(self):
        self.head = None    # Head pointer (points to the first node in the list)

    # Function to insert a new node at the END of the doubly linked list
    def insertAtEnd(self, data):
        new_node = Node(data)             # Step 1: Create a new node with the given data

        if self.head is None:             # Step 2: If the list is empty
            self.head = new_node          #         make the new node the head
            return

        current_node = self.head          # Step 3: Start from head
        while current_node.next:          # Traverse until the last node
            current_node = current_node.next

        current_node.next = new_node      # Step 4: Link the last node to the new node
        new_node.prev = current_node      # Also link new node back to the last node

    # Function to print all nodes in the linked list (forward)
    def printList(self):
        current = self.head               # Start from head
        while current:                    # Traverse until the end (None)
            print(current.data, end=" <-> ")
            current = current.next
        print("None")                     # End of list marker


# Create a DoublyLinkedList object
dll = DoublyLinkedList()

# Insert nodes at the end
dll.insertAtEnd(10)   # List: 10 <-> None
dll.insertAtEnd(20)   # List: 10 <-> 20 <-> None

print("Before inserting at end:")
dll.printList()       # Output: 10 <-> 20 <-> None

# Insert another node at the end
dll.insertAtEnd(30)   # List: 10 <-> 20 <-> 30 <-> None

print("After inserting 30 at end:")
dll.printList()       # Output: 10 <-> 20 <-> 30 <-> None
