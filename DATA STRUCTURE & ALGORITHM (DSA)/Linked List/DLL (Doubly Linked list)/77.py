# Program: Remove Duplicates from Sorted Doubly Linked List

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

    # Remove Duplicates
    def remove_duplicates(self):

        curr = self.head

        while curr and curr.next:

            if curr.val == curr.next.val:

                duplicate = curr.next

                curr.next = duplicate.next

                if duplicate.next:
                    duplicate.next.prev = curr

            else:
                curr = curr.next


dll = DLL()

arr = list(map(int, input("Enter sorted DLL elements: ").split()))

for num in arr:
    dll.append(num)

print("\nOriginal DLL:")
dll.display()

dll.remove_duplicates()

print("\nAfter Removing Duplicates:")
dll.display()

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")