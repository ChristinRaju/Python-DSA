class Node:
    # A class representing a single node in the linked list
    def __init__(self, data):
        self.data = data  # Store the data of the node
        self.next = None  # Initially, the node's next pointer is set to None


class LinkedList:
    # A class representing the linked list itself
    def __init__(self):
        self.head = None  # Initially, the linked list is empty, so the head is set to None

    def updateNode(self, data, index):
        # Method to update or create a node at a specific index
        if index < 0:
            # If the index is negative, print an error message
            print("Index not present")
            return

        # Case 1: The list is empty and we are trying to update at index 0
        if self.head is None:
            if index == 0:
                self.head = Node(data)  # Create the first node at index 0
                return
            else:
                # If the list is empty and the index is not 0, it's an invalid index
                print("Index not present")
                return

        # Case 2: The list is not empty
        current_node = self.head  # Start from the head of the list
        position = 0  # We start from position 0 (head)

        # Traverse the list to find the target index
        while current_node is not None and position < index:
            if current_node.next is None:
                # If we've reached the end of the list but haven't found the index,
                # we need to create new nodes with None values to fill the gap
                current_node.next = Node(None)
            current_node = current_node.next  # Move to the next node
            position += 1  # Increment the position

        # Now check if we've reached the desired position
        if current_node is not None:
            current_node.data = data  # Update the data of the node at the target index
        else:
            # If we haven't reached the target index (index out of bounds)
            print("Index not present")

    def printList(self):
        # Method to print the entire list
        current = self.head  # Start from the head of the list
        while current:
            print(current.data, end=" -> ")  # Print the data of each node, followed by an arrow
            current = current.next  # Move to the next node
        print("None")  # Indicate the end of the list


# Example usage:
ll = LinkedList()  # Create a new empty linked list
ll.updateNode(10, 0)   # Creates node with data 10 at index 0
ll.updateNode(20, 1)   # Creates node with data 20 at index 1 (fills gap with None node)
ll.updateNode(30, 2)   # Creates node with data 30 at index 2 (fills gap with None node)

print("Before update:")
ll.printList()  # Print the list before updating any node

ll.updateNode(25, 1)  # Update the node at index 1 (data 20 -> 25)

print("After update at index 1:")
ll.printList()  # Print the list after the update at index 1

ll.updateNode(100, 5)  # Attempt to update index 5 (index not present, creates new nodes up to index 5)
