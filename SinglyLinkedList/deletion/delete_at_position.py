class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Delete node at given position (0-based index)
    def delete_at_position(self, index):
        if self.head is None:   # Empty list
            print("List is empty, nothing to delete")
            return

        # If head needs to be removed
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        position = 0

        # Traverse to the node just before the index
        while current is not None and position < index - 1:
            current = current.next
            position += 1

        # If index is out of range
        if current is None or current.next is None:
            print("Index not present")
            return

        # Skip the node at given index
        current.next = current.next.next


# -------------------------
# Test the Linked List
# -------------------------
ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)

print("Initial List:")
ll.display()

print("\nAfter deleting node at position 2:")
ll.delete_at_position(2)   # removes 30
ll.display()

