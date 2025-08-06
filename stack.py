class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):  # Pushes an item onto the stack and prints it
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):  # Pops the top item if not empty; otherwise returns a message
        if self.is_empty():
            return "Stack is empty"
        return f"Popped: {self.stack.pop()}"

    def peek(self):  # Returns the top of the stack without removing it
        if self.is_empty():
            return "stack is empty!"
        return f"Top: {self.stack[-1]}"

    def is_empty(self):  # Checks if the stack is empty
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack (top -> bottom):", self.stack[::-1])


s = Stack()

s.push(20)  # pushes 20 to the stack
print(s.peek())  # prints the top of the stack
s.push(30)  # pushes 30 to the stack
s.display()

print(s.pop())
print(s.peek())
s.display()
