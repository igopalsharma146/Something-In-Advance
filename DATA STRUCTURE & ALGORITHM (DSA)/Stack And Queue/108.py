# Queue: LIFO

# what is Queue?
# A queue is a linear data structure that follows the FIFO (First In First Out) principle. It can store any type of data. It has two main operations: enqueue (to add an element to the end of the queue) and dequeue (to remove the front element from the queue). Other common operations include peek (to view the front element without removing it) and isEmpty (to check if the queue is empty).

# Queue Opertions:
# 1. Enqueue: Add an element to the end of the queue.
# 2. Dequeue: Remove the front element from the queue.
# 3. size
# 4. front
# 5. Rear
# 6. isEmpty


# Program: Implement Queue Using Array (Using Class)
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    # Enqueue Operation
    def enqueue(self, value):
        if len(self.queue) == self.size:
            print("Queue Overflow")
            return
        self.queue.append(value)
        print(value, "Inserted into Queue")

    # Dequeue Operation
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
            return
        print(self.queue.pop(0), "Deleted from Queue")

    # Front Operation
    def front(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
            return
        print("Front Element:", self.queue[0])

    # Rear Operation
    def rear(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
            return
        print("Rear Element:", self.queue[-1])

    # isEmpty Operation
    def isEmpty(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")

    # Size Operation
    def queue_size(self):
        print("Queue Size:", len(self.queue))

    # Display Queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue:", self.queue)

# Driver Code
size = int(input("Enter Queue Size: "))
q = Queue(size)
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
print("Dequeue : O(N)")
print("Front : O(1)")
print("Rear : O(1)")
print("isEmpty : O(1)")
print("Size : O(1)")
print("Display : O(N)")
print("\nSpace Complexity : O(N)")