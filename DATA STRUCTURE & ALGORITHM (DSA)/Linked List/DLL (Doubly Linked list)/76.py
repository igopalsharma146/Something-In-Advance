# Program: Delete All Occurrences of a Key in DLL

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

    # Delete All Occurrences
    def delete_all_occurrences(self, key):

        curr = self.head

        while curr:
            next_node = curr.next

            if curr.val == key:
                # Head Node
                if curr.prev is None:
                    self.head = curr.next

                    if self.head:
                        self.head.prev = None
                        
                # Last Node
                elif curr.next is None:
                    curr.prev.next = None

                # Middle Node
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
            curr = next_node


dll = DLL()

arr = list(map(int, input("Enter DLL elements: ").split()))

for num in arr:
    dll.append(num)

print("\nOriginal DLL:")
dll.display()

key = int(input("\nEnter key to delete: "))

dll.delete_all_occurrences(key)

print("\nAfter Deletion:")
dll.display()

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")