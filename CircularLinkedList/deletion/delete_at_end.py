# Python Program for Deletion at the End in Circular Linked List
class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        # Initialize an empty circular linked list with head pointer pointing to None
        self.head = None

    def deleteAtEnd(self):
        # Delete a node from the end of the circular linked list
        if not self.head:
            print("List is empty")
            return

        # Case 1: If there is only one node
        if self.head.next == self.head:
            self.head = None
            return

        # Case 2: More than one node -> Traverse to second last node
        current = self.head
        while current.next.next != self.head:
            current = current.next

        # Skip the last node
        current.next = self.head

    def insertAtEnd(self, data):
        # Insert a new node with data at the end (helper to build list)
        new_node = Node(data)

        if not self.head:
            # If the list is empty, point new_node to itself (circular)
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        # Traverse until we reach the last node (whose next points back to head)
        while current.next != self.head:
            current = current.next

        # Insert the new node at the end
        current.next = new_node
        new_node.next = self.head   # Maintain circular nature

    def printList(self):
        # Display the elements of the circular linked list
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:   # Stop when we circle back to head
                break

        print("(Back to Head)")


# Create a CircularLinkedList object
cll = CircularLinkedList()

# Insert nodes at the end
cll.insertAtEnd(10)   # List: 10 -> (Back to Head)
cll.insertAtEnd(20)   # List: 10 -> 20 -> (Back to Head)
cll.insertAtEnd(30)   # List: 10 -> 20 -> 30 -> (Back to Head)

print("Before deleting at end:")
cll.printList()       # Output: 10 -> 20 -> 30 -> (Back to Head)

# Delete node at the end
cll.deleteAtEnd()

print("After deleting at end:")
cll.printList()       # Output: 10 -> 20 -> (Back to Head)
