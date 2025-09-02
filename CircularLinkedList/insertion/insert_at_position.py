# Node class: represents a single element (box) in the circular linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the actual data value
        self.next = None      # Pointer to the next node


# CircularLinkedList class: manages the nodes
class CircularLinkedList:
    def __init__(self):
        self.head = None      # Head points to the first node of the list

    # Insert a new node at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)

        if self.head is None:
            # If list is empty, point new node to itself
            self.head = new_node
            new_node.next = self.head
            return

        # Otherwise, traverse to the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Link the new node at the beginning
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    # Insert a new node at a specific index
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return

        position = 0
        current = self.head

        # Traverse until the node BEFORE the given index
        while current.next != self.head and position < index - 1:
            current = current.next
            position += 1

        # If index is out of range (and we circled back to head)
        if current.next == self.head and position < index - 1:
            print(f"Index {index} not present")
            return

        # Insert new node
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

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

# Insert at index 0 (beginning)
cll.insertAtIndex(10, 0)   # List: 10 -> (Back to Head)
cll.insertAtIndex(20, 1)   # List: 10 -> 20 -> (Back to Head)

print("Before inserting at index 1:")
cll.printList()            # Output: 10 -> 20 -> (Back to Head)

# Insert 30 at index 1
cll.insertAtIndex(30, 1)   # List: 10 -> 30 -> 20 -> (Back to Head)

print("After inserting 30 at index 1:")
cll.printList()            # Output: 10 -> 30 -> 20 -> (Back to Head)
