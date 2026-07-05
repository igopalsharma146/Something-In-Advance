# Program: Implement Deque Using Array (Using Class)

class Deque:
    def __init__(self, size):
        self.deque = []
        self.size = size

    # Insert Front
    def insert_front(self, value):
        if len(self.deque) == self.size:
            print("Deque Overflow")
            return
        self.deque.insert(0, value)
        print(value, "Inserted at Front")

    # Insert Rear
    def insert_rear(self, value):
        if len(self.deque) == self.size:
            print("Deque Overflow")
            return

        self.deque.append(value)
        print(value, "Inserted at Rear")

    # Delete Front
    def delete_front(self):
        if len(self.deque) == 0:
            print("Deque Underflow")
            return
        print(self.deque.pop(0), "Deleted from Front")

    # Delete Rear
    def delete_rear(self):
        if len(self.deque) == 0:
            print("Deque Underflow")
            return
        print(self.deque.pop(), "Deleted from Rear")

    # Get Front
    def get_front(self):
        if len(self.deque) == 0:
            print("Deque is Empty")
            return
        print("Front Element:", self.deque[0])

    # Get Rear
    def get_rear(self):
        if len(self.deque) == 0:
            print("Deque is Empty")
            return
        print("Rear Element:", self.deque[-1])

    # isEmpty
    def isEmpty(self):
        if len(self.deque) == 0:
            print("Deque is Empty")
        else:
            print("Deque is Not Empty")

    # Size
    def deque_size(self):
        print("Deque Size:", len(self.deque))

    # Display
    def display(self):
        if len(self.deque) == 0:
            print("Deque is Empty")
        else:
            print("Deque:", self.deque)


# Driver Code
size = int(input("Enter Deque Size: "))
dq = Deque(size)
dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(5)
dq.insert_front(2)

dq.display()

dq.get_front()
dq.get_rear()

dq.delete_front()
dq.delete_rear()

dq.display()

dq.deque_size()

dq.isEmpty()

print("\nTime Complexity")
print("Insert Front : O(N)")
print("Insert Rear  : O(1)")
print("Delete Front : O(N)")
print("Delete Rear  : O(1)")
print("Front        : O(1)")
print("Rear         : O(1)")
print("isEmpty      : O(1)")
print("Size         : O(1)")
print("Display      : O(N)")

print("\nSpace Complexity : O(N)")