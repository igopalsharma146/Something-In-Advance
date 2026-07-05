# Stack : Last In First Out (LIFO)

# 1) implement stack using array
# 2) implement queue using array
# 3) implement stack using queue
# 4) implement queue using stack
# 5) implement stack using Linked List
# 6) implement queue using Linked List
# 7) check for balanced parenthesis using stack
# 8) implement min stack using stack

# what is stack ?
# A stack is a linear data structure that follows the LIFO (Last In First Out) principle. can store any type of data. It has two main operations: push (to add an element to the top of the stack) and pop (to remove the top element from the stack). Other common operations include peek (to view the top element without removing it) and isEmpty (to check if the stack is empty).

# stack Opertions:
# 1. Push: Add an element to the top of the stack.
# 2. Pop: Remove the top element from the stack.
# 3. size
# 4. peek
# 5. isEmpty


# Program: Implement Stack Using Array

size = int(input("Enter Stack Size: "))
stack = []

# Push Operation
def push(value):
    if len(stack) == size:
        print("Stack Overflow")
        return

    stack.append(value)
    print(value, "Pushed into Stack")


# Pop Operation
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
        return

    print(stack.pop(), "Popped from Stack")


# Peek Operation
def peek():
    if len(stack) == 0:
        print("Stack is Empty")
        return

    print("Top Element:", stack[-1])


# isEmpty Operation
def isEmpty():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Stack is Not Empty")


# Size Operation
def stack_size():
    print("Stack Size:", len(stack))


# Display Stack
def display():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Stack:", stack)


# Driver Code

push(10)
push(20)
push(30)
display()
peek()
pop()
display()
stack_size()
isEmpty()

print("Time Complexity:")
print("Push : O(1)")
print("Pop : O(1)")
print("Peek : O(1)")
print("Display : O(N)")

print("Space Complexity: O(N)")