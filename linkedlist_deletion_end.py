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

    # Remove last node
    def remove_last_node(self):
        if self.head is None:              # Case 1: Empty list
            print("List is empty, nothing to remove")
            return

        if self.head.next is None:         # Case 2: Only one node
            self.head = None
            return

        curr_node = self.head
        while curr_node.next.next is not None:  # Traverse to second last
            curr_node = curr_node.next

        curr_node.next = None              # Remove link to last node


# -------------------------
# Manually create a Linked List
# -------------------------
ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)

print("Initial List:")
ll.display()

print("\nAfter removing last node:")
ll.remove_last_node()
ll.display()
