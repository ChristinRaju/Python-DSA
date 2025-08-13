class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Manually create a linked list:
ll = LinkedList()

ll.insertAtEnd(10)
ll.insertAtEnd(20)

print("Before inserting at end:")
ll.printList()

# Now insert a new node at the end
ll.insertAtEnd(30)

print("After inserting 20 at end:")
ll.printList()
