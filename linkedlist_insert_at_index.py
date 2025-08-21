# Node class: represents a single element (box) in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the actual data value
        self.next = None      # Pointer to the next node (initially None)


# LinkedList class: manages the nodes
class LinkedList:
    def __init__(self):
        self.head = None      # Head points to the first node of the list

    # Insert a new node at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)       # Step 1: Create new node
        new_node.next = self.head   # Step 2: Point new node → current head
        self.head = new_node        # Step 3: Update head → new node

    # Insert a new node at a specific index
    def insertAtIndex(self, data, index):
        # Case 1: If index is 0 → just insert at beginning
        if index == 0:
            self.insertAtBegin(data)
            return
        
        position = 0
        current_node = self.head

        # Traverse until the node BEFORE the given index
        while current_node is not None and position < index - 1:
            current_node = current_node.next
            position += 1

        # Case 2: If index is out of range
        if current_node is None:
            print(f"Index {index} not present")
            return
        
        # Case 3: Insert new node between current_node and next
        new_node = Node(data)
        new_node.next = current_node.next   # New node → next points to current_node’s next
        current_node.next = new_node        # Current_node → next points to new node

    # Print the full linked list
    def printList(self):
        current = self.head
        while current:                      # Traverse until None
            print(current.data, end=" -> ")
            current = current.next
        print("None")                       # End of list marker


ll = LinkedList()

# Insert at index 0 (beginning)
ll.insertAtIndex(10, 0)   # List: 10 -> None
ll.insertAtIndex(20, 1)   # List: 10 -> 20 -> None

print("Before inserting at index 1:")
ll.printList()            # Output: 10 -> 20 -> None

# Insert 30 at index 1
ll.insertAtIndex(30, 1)   # List: 10 -> 30 -> 20 -> None

print("After inserting 30 at index 1:")
ll.printList()            # Output: 10 -> 30 -> 20 -> None
