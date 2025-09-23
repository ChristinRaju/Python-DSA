# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at END
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    # Insert at POSITION (0-based index)
    def insertAtPosition(self, data, position):
        new_node = Node(data)

        # Case 1: Empty list
        if self.head is None:
            if position == 0:
                self.head = new_node
            else:
                print("Position out of range (list empty)")
            return

        # Case 2: Insert at head
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # Case 3: Insert in middle or end
        current_node = self.head
        count = 0
        while current_node and count < position - 1:
            current_node = current_node.next
            count += 1

        if current_node is None:
            print("Position out of range")
            return

        new_node.next = current_node.next
        new_node.prev = current_node
        if current_node.next:   # If not inserting at the end
            current_node.next.prev = new_node
        current_node.next = new_node

    # Print list forward
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


dll = DoublyLinkedList()

# Insert at end
dll.insertAtPosition(1, 0)   # List: 1
dll.insertAtPosition(2, 1)   # List: 1 <-> 2
dll.insertAtPosition(3, 2)   # List: 1 <-> 2 <-> 3


print("Before insertion:")
dll.printList()   # 1 <-> 2 <-> 4 <-> None

# Insert at position 2 (between 2 and 4)
dll.insertAtPosition(4, 1)   # Insert 4 at position 1 → 1 <-> 4 <-> 2 <-> 3

print("After inserting 4 at position 1:")
dll.printList()   # 1 <-> 2 <-> 3 <-> 4 <-> None
