# Program: Implement Queue Using Two Stacks (Using Class)

class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Enqueue Operation
    def enqueue(self, value):
        self.stack1.append(value)
        print(value, "Inserted into Queue")

    # Dequeue Operation
    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue Underflow")
            return

        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        print(self.stack2.pop(), "Deleted from Queue")

    # Front Operation
    def front(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is Empty")
            return

        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        print("Front Element:", self.stack2[-1])

    # Rear Operation
    def rear(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is Empty")
            return

        if len(self.stack1) != 0:
            print("Rear Element:", self.stack1[-1])
        else:
            print("Rear Element:", self.stack2[0])

    # isEmpty Operation
    def isEmpty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")

    # Size Operation
    def queue_size(self):
        print("Queue Size:", len(self.stack1) + len(self.stack2))

    # Display Queue
    def display(self):
        temp = self.stack2[::-1] + self.stack1

        if len(temp) == 0:
            print("Queue is Empty")
        else:
            print("Queue:", temp)


# Driver Code

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.front()
q.rear()
q.dequeue()
q.display()

q.queue_size()
q.isEmpty()

print("\nTime Complexity")
print("Enqueue : O(1)")
print("Dequeue : Amortized O(1), Worst O(N)")
print("Front : Amortized O(1)")
print("Rear : O(1)")
print("isEmpty : O(1)")
print("Size : O(1)")
print("Display : O(N)")

print("\nSpace Complexity : O(N)")