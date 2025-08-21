class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Remove first node
    def remove_first_node(self):
        if self.head is None:
            print("List is empty, nothing to remove")
            return
        self.head = self.head.next

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


# -------------------------
# Manually create a Linked List
# -------------------------
ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

print("Initial List:")
ll.display()

print("\nAfter removing first node:")
ll.remove_first_node()
ll.display()
