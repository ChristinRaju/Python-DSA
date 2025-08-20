class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_index(self, data, index):
        if(index == 0):
            self.insert_at_beginning(data)
            return
        
        position = 0
        current_node = self.head

        while current_node != None and position+1 != index:
            position += 1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present in the list.")

    def traverse(self):
        # Traverse through the linked list and print the data
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list

# Test code
# Create a SingleLinkedList object
ll = SingleLinkedList()

# Insert some initial nodes
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)

print("Before inserting at beginning:")
ll.traverse()

# Now insert a new node at the beginning
ll.insert_at_beginning(30)

print("After inserting 30 at beginning:")
ll.traverse()

# Create a new list for testing insert at end
ll2 = SingleLinkedList()

ll2.insert_at_end(10)
ll2.insert_at_end(20)

print("Before inserting at end:")
ll2.traverse()

# Now insert a new node at the end
ll2.insert_at_end(30)

print("After inserting 30 at end:")
ll2.traverse()

# Create a new list for testing insert at index
ll3 = SingleLinkedList()

ll3.insert_at_end(10)
ll3.insert_at_end(20)

print("Before inserting at index:")
ll3.traverse()

# Now insert a new node at index 1
ll3.insert_at_index(15, 1)

print("After inserting 15 at index 1:")
ll3.traverse()

# Now try inserting at an index that does not exist
ll3.insert_at_index(25, 5)  # This should print an error message
