# Node class: represents a single element (box) in the circular linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the actual data value
        self.next = None      # Pointer to the next node


# CircularLinkedList class: manages the nodes
class CircularLinkedList:
    def __init__(self):
        self.head = None      # Head points to the first node of the list

    # Insert a new node at the end (for building the list easily)
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            # If list is empty, point new node to itself
            self.head = new_node
            new_node.next = self.head
            return

        # Traverse until the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Link new node at the end and back to head
        current.next = new_node
        new_node.next = self.head

    # Delete a node at a specific index
    def deleteAtIndex(self, index):
        if not self.head:
            print("List is empty")
            return

        if index < 0:
            print("Invalid index")
            return

        # Case 1: Deleting the head node (index = 0)
        if index == 0:
            # If only one node in the list
            if self.head.next == self.head:
                self.head = None
                return

            # Otherwise, find the last node
            current = self.head
            while current.next != self.head:
                current = current.next

            # Point last node to 2nd node
            current.next = self.head.next
            # Move head to 2nd node
            self.head = self.head.next
            return

        # Case 2: Deleting at a non-zero index
        current = self.head
        position = 0

        # Traverse until the node BEFORE the given index
        while position < index - 1 and current.next != self.head:
            current = current.next
            position += 1

        # If index is out of range
        if current.next == self.head:
            print(f"Index {index} not present")
            return

        # Skip the node at given index
        current.next = current.next.next

    # Print the circular linked list
    def printList(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to Head)")


# Driver Code
cll = CircularLinkedList()

# Append nodes for testing
cll.append(10)
cll.append(20)
cll.append(30)

print("Before deleting at index 1:")
cll.printList()            # Output: 10 -> 20 -> 30 -> (Back to Head)

# Delete node at index 1 (value = 20)
cll.deleteAtIndex(1)

print("After deleting at index 1:")
cll.printList()            # Output: 10 -> 30 -> (Back to Head)
