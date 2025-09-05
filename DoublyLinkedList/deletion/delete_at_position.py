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

    # Function to delete a node at a specific POSITION
    def deleteAtPosition(self, position):
        if self.head is None:             # Case 1: Empty list
            print("Doubly linked list is empty")
            return

        if position < 0:                  # Invalid position
            print("Invalid position")
            return

        # Case 2: Deleting the head node
        if position == 0:
            if self.head.next:            # If more than one node
                self.head = self.head.next
                self.head.prev = None
            else:                         # If only one node
                self.head = None
            return

        # Case 3: Deleting from middle or end
        current_node = self.head
        count = 0
        while current_node and count < position:
            current_node = current_node.next
            count += 1

        if current_node is None:          # Position is out of range
            print("Position out of range")
            return

        if current_node.next:             # Update next node's prev pointer
            current_node.next.prev = current_node.prev
        if current_node.prev:             # Update prev node's next pointer
            current_node.prev.next = current_node.next

        del current_node                  # Free memory

    # Function to print all nodes in the linked list (forward)
    def printList(self):
        current = self.head               # Start from head
        while current:                    # Traverse until the end (None)
            print(current.data, end=" <-> ")
            current = current.next
        print("None")                     # End of list marker


# ---------------- Driver Code ----------------
dll = DoublyLinkedList()

# Insert nodes at the end
dll.insertAtEnd(1)   # List: 1 <-> None
dll.insertAtEnd(2)   # List: 1 <-> 2 <-> None
dll.insertAtEnd(3)   # List: 1 <-> 2 <-> 3 <-> None
dll.insertAtEnd(4)   # List: 1 <-> 2 <-> 3 <-> 4 <-> None

print("Before deletion at position 2:")
dll.printList()       # Output: 1 <-> 2 <-> 3 <-> 4 <-> None

# Delete node at position 2 (zero-based index, so it deletes "3")
dll.deleteAtPosition(2)

print("After deletion at position 2:")
dll.printList()       # Output: 1 <-> 2 <-> 4 <-> None
