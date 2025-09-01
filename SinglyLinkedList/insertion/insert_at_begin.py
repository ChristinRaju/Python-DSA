# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data   # Store the value in this node
        self.next = None   # Pointer to the next node (initially None)


# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None   # Head pointer (points to the first node in the list)

    # Function to insert a node at the beginning of the list
    def insertAtBegin(self, data):
        new_node = Node(data)     # Step 1: Create a new node with given data

        if self.head is None:     # Step 2: If list is empty
            self.head = new_node  #         Make the new node the head
        else:                     # Step 3: If list already has nodes
            new_node.next = self.head  # Link new node to current head
            self.head = new_node       # Move head to point to the new node

    # Function to print all nodes in the linked list
    def printList(self):
        current = self.head   # Start from head
        while current:        # Traverse until current is None
            print(current.data, end=" -> ")  # Print the data of each node
            current = current.next           # Move to next node
        print("None")         # Indicate the end of the list


# Create a LinkedList object
ll = LinkedList()

# Insert some initial nodes (at beginning)
ll.insertAtBegin(10)   # List: 10 -> None
ll.insertAtBegin(20)   # List: 20 -> 10 -> None

print("Before inserting at beginning:")
ll.printList()         # Output: 20 -> 10 -> None

# Insert another node at the beginning
ll.insertAtBegin(30)   # List: 30 -> 20 -> 10 -> None

print("After inserting 30 at beginning:")
ll.printList()         # Output: 30 -> 20 -> 10 -> None