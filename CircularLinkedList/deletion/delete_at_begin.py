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
    def append(self, data):
        new_node = Node(data)   # Step 1: Create new node

        if not self.head:       # Step 2: If list is empty
            new_node.next = new_node   # Node points to itself
            self.head = new_node
        else:                   # Step 3: Otherwise traverse to last node
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node    # Last node points to new node
            new_node.next = self.head  # New node points to head

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
circular_list = CircularLinkedList()

# Insert some nodes
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)

print("Circular Linked List before deletion at beginning:")
circular_list.display()

# Delete node at beginning
circular_list.delete_at_beginning()

print("Circular Linked List after deletion at beginning:")
circular_list.display()
