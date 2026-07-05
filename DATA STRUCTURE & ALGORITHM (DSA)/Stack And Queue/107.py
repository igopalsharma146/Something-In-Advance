# Program: Implement Stack Using Array (Using Class)

class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    # Push Operation
    def push(self, value):
        if len(self.stack) == self.size:
            print("Stack Overflow")
            return
        self.stack.append(value)
        print(value, "Pushed into Stack")

    # Pop Operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
            return
        print(self.stack.pop(), "Popped from Stack")

    # Peek Operation
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
            return
        print("Top Element:", self.stack[-1])

    # isEmpty Operation
    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    # Size Operation
    def stack_size(self):
        print("Stack Size:", len(self.stack))

    # Display Stack
    def display(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Stack:", self.stack)


# Driver Code
size = int(input("Enter Stack Size: "))
s = Stack(size)
s.push(10)
s.push(20)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()
s.stack_size()
s.isEmpty()

print("\nTime Complexity")
print("Push : O(1)")
print("Pop : O(1)")
print("Peek : O(1)")
print("isEmpty : O(1)")
print("Size : O(1)")
print("Display : O(N)")

print("\nSpace Complexity : O(N)")