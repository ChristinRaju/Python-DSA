# Define a Node class first
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define the Queue using linked list (node-based)
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        # If queue is empty
        if self.rear is None:
            self.front = self.rear = new_node
            return

        # Add new node at the end
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"

        # Remove front node
        temp = self.front
        self.front = self.front.next

        # If queue becomes empty, reset rear also
        if self.front is None:
            self.rear = None

        return temp.data

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # Output: 10
print(q.dequeue())  # Output: 20
print(q.dequeue())  # Output: 30
