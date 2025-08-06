class Queue:
    def __init__(self):
        self.queue = [30, 40, 50]

    def enqueue(self, item):  # Adds item to the end of the queue
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):  # Removes item from the front of the queue
        if self.is_empty():
            return "Queue is empty"
        return f"Dequeued: {self.queue.pop(0)}"

    def peek(self):  # Returns the front of the queue without removing it
        if self.is_empty():
            return "Queue is empty"
        return f"Front: {self.queue[0]}"

    def is_empty(self):  # Checks if the queue is empty
        return len(self.queue) == 0

    def size(self):  # Returns the number of items in the queue
        return len(self.queue)

    def display(self):
        print("Queue (front -> rear):", self.queue)

q = Queue()

q.enqueue(10)
print(q.peek())  # Should print the front of the queue (10)
print(q.dequeue())  # Removes 10
q.display()  # Shows [20]