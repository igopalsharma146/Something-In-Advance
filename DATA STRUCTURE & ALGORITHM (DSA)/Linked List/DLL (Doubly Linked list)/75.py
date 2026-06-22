# Program: Reverse a Doubly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    # Append
    def append(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    # Display
    def display(self):

        curr = self.head

        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next

        print("None")

    # Reverse DLL
    def reverse(self):

        curr = self.head
        temp = None

        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp

            curr = curr.prev

        if temp:
            self.head = temp.prev

    # Reverse DLL
    def reverse2(self):
        # Better Approach

        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        curr = self.head
        i = len(values) - 1

        while curr:
            curr.val = values[i]
            i -= 1
            curr = curr.next


dll = DLL()

n = int(input("Enter number of nodes: "))
for _ in range(n):
    val = int(input("Enter value: "))
    dll.append(val)

print("\nOriginal DLL:")
dll.display()


dll.reverse2()
print("\nReversed DLL Better solution:")
dll.display()
print("\nBetter Approach")
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")

dll.reverse()
print("\nReversed DLL Optimal Solution:")
dll.display()
print("\nOptimal Approach")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")