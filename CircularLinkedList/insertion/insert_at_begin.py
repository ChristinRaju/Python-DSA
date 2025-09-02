# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data   # Store the value in this node
        self.next = None   # Pointer to the next node (initially None)


# Define a CircularLinkedList class
class CircularLinkedList:
    def __init__(self):
        self.head = None   # Head pointer (points to the first node)

    # Function to insert a node at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)   # Step 1: Create a new node with given data

        if self.head is None:   # Step 2: If list is empty
            self.head = new_node
            new_node.next = new_node   # Make it circular (points to itself)
        else:                   # Step 3: If list already has nodes
            temp = self.head
            while temp.next != self.head:  # Traverse till the last node
                temp = temp.next

            new_node.next = self.head  # Link new node to current head
            temp.next = new_node       # Last node points to new node
            self.head = new_node       # Move head to point to the new node

    # Function to print all nodes in the circular linked list
    def printList(self):
        if self.head is None:          # Step 1: If list is empty
            print("List is empty")
            return

        current = self.head            # Step 2: Start from head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:   # Stop once we loop back to head
                break
        print("(head)")


# Create a CircularLinkedList object
cll = CircularLinkedList()

# Insert some initial nodes (at beginning)
cll.insertAtBegin(10)   # List: 10 -> (head)
cll.insertAtBegin(20)   # List: 20 -> 10 -> (head)

print("Before inserting at beginning:")
cll.printList()         # Output: 20 -> 10 -> (head)

# Insert another node at the beginning
cll.insertAtBegin(30)   # List: 30 -> 20 -> 10 -> (head)

print("After inserting 30 at beginning:")
cll.printList()         # Output: 30 -> 20 -> 10 -> (head)
