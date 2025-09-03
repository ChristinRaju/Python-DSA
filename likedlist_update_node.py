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

        # Traverse to the desired position
        while current_node != None and position < index:
            if current_node.next is None:
                # Create a new node if we are not yet at the index
                current_node.next = Node(None)
            current_node = current_node.next
            position += 1

        # Now update the node
        if current_node != None:
            current_node.data = data
        else:
            print("Index not present")

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.updateNode(10, 0)   # Creates node at index 0
ll.updateNode(20, 1)   # Creates node at index 1
ll.updateNode(30, 2)   # Creates node at index 2

print("Before update:")
ll.printList()

ll.updateNode(25, 1)  # Update index 1 (20 -> 25)

print("After update at index 1:")
ll.printList()

ll.updateNode(100, 5)  # Index not present
