# Program: Doubly Linked List
# Operations: Delete Head, Delete Last, Delete In Between

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

    # Delete Head
    def delete_head(self):

        if self.head is None:
            print("DLL is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    # Delete Last
    def delete_last(self):

        if self.head is None:
            print("DLL is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.prev.next = None

    # Delete In Between
    # Delete node having target value
    def delete_in_between(self, target):

        if self.head is None:
            print("DLL is Empty")
            return

        curr = self.head

        while curr:

            if curr.val == target:

                # Head node
                if curr.prev is None:
                    self.delete_head()
                    return

                # Last node
                if curr.next is None:
                    curr.prev.next = None
                    return

                curr.prev.next = curr.next
                curr.next.prev = curr.prev

                return

            curr = curr.next

        print("Value not found")

    # Display
    def display(self):

        curr = self.head

        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next

        print("None")


dll = DLL()

n = int(input("Enter number of nodes: "))

for _ in range(n):
    val = int(input("Enter value: "))
    dll.append(val)

print("\nOriginal DLL:")
dll.display()


dll.delete_head()

print("\nAfter Delete Head:")
dll.display()


dll.delete_last()

print("\nAfter Delete Last:")
dll.display()


target = int(input("\nEnter value to delete: "))
dll.delete_in_between(target)

print("\nAfter Delete In Between:")
dll.display()


print("\nDelete Head")
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")

print("\nDelete Last")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

print("\nDelete In Between")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")