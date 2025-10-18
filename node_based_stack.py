# Define a Node class first
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        # New node points to old top
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data}")

    def pop(self):
        if self.top is None:
            return "Stack is empty"

        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top is None:
            return "Stack is empty"
        return self.top.data

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        print("Stack elements (top → bottom): ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# --- Testing the Stack ---
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped:", s.pop())
print("Top element:", s.peek())
s.display()
