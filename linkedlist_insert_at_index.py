class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        
        position = 0
        current_node = self.head
        
        # Traverse until the node before the insertion point
        while current_node is not None and position < index - 1:
            current_node = current_node.next
            position += 1
        
        if current_node is None:
            print(f"Index {index} not present")
            return
        
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()

# Insert nodes at beginning and specific indexes
ll.insertAtIndex(10, 0)  # List: 10 -> None
ll.insertAtIndex(20, 1)  # List: 10 -> 20 -> None

print("Before inserting at index 1:")
ll.printList()

ll.insertAtIndex(30, 1)  # Insert 30 at index 1: List should be 10 -> 30 -> 20 -> None

print("After inserting 30 at index 1:")
ll.printList()

