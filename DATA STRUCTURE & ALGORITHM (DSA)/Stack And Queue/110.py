# Program: Implement Stack Using Queue (Using Class)
from collections import deque
class Stack:
    def __init__(self):
        self.queue = deque()

    # Push Operation
    def push(self, value):
        self.queue.append(value)

        # Rotate the queue
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        print(value, "Pushed into Stack")

    # Pop Operation
    def pop(self):
        if len(self.queue) == 0:
            print("Stack Underflow")
            return

        print(self.queue.popleft(), "Popped from Stack")

    # Peek Operation
    def peek(self):
        if len(self.queue) == 0:
            print("Stack is Empty")
            return

        print("Top Element:", self.queue[0])

    # isEmpty Operation
    def isEmpty(self):
        if len(self.queue) == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    # Size Operation
    def stack_size(self):
        print("Stack Size:", len(self.queue))

    # Display Stack
    def display(self):
        if len(self.queue) == 0:
            print("Stack is Empty")
        else:
            print("Stack:", list(self.queue))


# Driver Code

s = Stack()
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
print("Push : O(N)")
print("Pop : O(1)")
print("Peek : O(1)")
print("isEmpty : O(1)")
print("Size : O(1)")
print("Display : O(N)")

print("\nSpace Complexity : O(N)")



# Approach Used : One Queue is used.

# Push Operation :
# Insert the new element.
# Rotate the queue so that the newly inserted element comes to the front.

# Example:

# Push(10)

# Queue: [10]
# Push(20)

# Before Rotation:
# [10,20]

# After Rotation:
# [20,10]
# Push(30)

# Before Rotation:
# [20,10,30]

# After Rotation:
# [30,20,10]

# Now the front of the queue always represents the top of the stack.