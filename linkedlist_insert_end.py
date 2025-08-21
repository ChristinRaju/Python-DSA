# Node class: represents one box (node) in the linked list
class Node:
    def __init__(self, data):
        self.data = data   # Store the actual data value
        self.next = None   # Pointer to the next node (initially None)


# LinkedList class: manages the nodes and operations
class LinkedList:
    def __init__(self):
        self.head = None   # Head pointer (points to the first node in the list)

    # Function to insert a new node at the END of the linked list
    def insertAtEnd(self, data):
        new_node = Node(data)            # Step 1: Create a new node with the given data

        if self.head is None:            # Step 2: If the list is empty
            self.head = new_node         #         make the new node the head
            return

        current_node = self.head         # Step 3: Start from head
        while current_node.next:         # Traverse until the last node
            current_node = current_node.next

        current_node.next = new_node     # Step 4: Link the last node to the new node

    # Function to print all nodes in the linked list
    def printList(self):
        current = self.head              # Start from head
        while current:                   # Traverse until the end (None)
            print(current.data, end=" -> ")
            current = current.next
        print("None")                    # End of list marker


# Create a LinkedList object
ll = LinkedList()

# Insert nodes at the end
ll.insertAtEnd(10)   # List: 10 -> None
ll.insertAtEnd(20)   # List: 10 -> 20 -> None

print("Before inserting at end:")
ll.printList()       # Output: 10 -> 20 -> None

# Insert another node at the end
ll.insertAtEnd(30)   # List: 10 -> 20 -> 30 -> None

print("After inserting 30 at end:")
ll.printList()       # Output: 10 -> 20 -> 30 -> None
