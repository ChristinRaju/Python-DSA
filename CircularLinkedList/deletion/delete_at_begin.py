# Python Program for Deletion at the Beginning of a Circular Linked List

# Node class: represents a node in the circular linked list
class Node:
    def __init__(self, data):
        self.data = data    # Store data
        self.next = None    # Pointer to next node


# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None    # Initially empty list

    # Function to add a node at the end
    def insertAtBegin(self, data):
        new_node = Node(data)   # Step 1: Create a new node with given data

        if self.head is None:   # Step 2: If list is empty
            self.head = new_node
            new_node.next = new_node   # Make it circular (points to itself)
        else:                   # Step 3: If list already has nodes
            temp = self.head
            while temp.next != self.head:  # Traverse till the last node
                temp = temp.next

            new_node.next = self.head  # Link new node to current head
            temp.next = new_node       # Last node points to new node
            self.head = new_node       # Move head to point to the new node

    # Function to delete node at the beginning
    def delete_at_beginning(self):
        if not self.head:              # Step 1: If list is empty
            print("Circular Linked List is empty")
            return

        if self.head.next == self.head:   # Step 2: If only one node
            self.head = None              # Remove it
            return

        # Step 3: Otherwise, find the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Step 4: Update last node's next to 2nd node
        current.next = self.head.next

        # Step 5: Move head to point to 2nd node
        self.head = self.head.next

    # Function to print the circular linked list
    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")


# Driver Code
cll = CircularLinkedList()

# Insert some nodes
cll.insertAtBegin(1)
cll.insertAtBegin(2)
cll.insertAtBegin(3)

print("Circular Linked List before deletion at beginning:")
cll.display()

# Delete node at beginning
cll.delete_at_beginning()

print("Circular Linked List after deletion at beginning:")
cll.display()
