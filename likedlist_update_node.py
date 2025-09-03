class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def updateNode(self, data, index):
        if index < 0:
            print("Index not present")
            return

        # Case: Empty list and index 0
        if self.head is None:
            if index == 0:
                self.head = Node(data)
                return
            else:
                print("Index not present")
                return

        current_node = self.head
        position = 0

        # Traverse to the desired position (index)
        while current_node is not None and position < index:
            if current_node.next is None:
                # If we reached the end but haven't reached the target index, create new nodes
                current_node.next = Node(None)
            current_node = current_node.next
            position += 1

        # Now check if we're at the desired position
        if current_node is not None:
            current_node.data = data
        else:
            print("Index not present")

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.updateNode(10, 0)   # Creates node at index 0
ll.updateNode(20, 1)   # Creates node at index 1 (fills gap with None node)
ll.updateNode(30, 2)   # Creates node at index 2 (fills gap with None node)

print("Before update:")
ll.printList()

ll.updateNode(25, 1)  # Update index 1 (20 -> 25)

print("After update at index 1:")
ll.printList()

ll.updateNode(100, 5)  # Index not present, but will create new nodes up to index 5
