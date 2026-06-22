# Program: Doubly Linked List
# Operations: Append, Insert At Head, Insert In Between

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

    # Insert At Head
    def insert_at_head(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert In Between
    # Insert new_val after target
    def insert_in_between(self, target, new_val):

        curr = self.head

        while curr:

            if curr.val == target:

                new_node = Node(new_val)

                new_node.next = curr.next
                new_node.prev = curr

                if curr.next:
                    curr.next.prev = new_node

                curr.next = new_node

                return

            curr = curr.next

        print("Target node not found!")

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


head_val = int(input("\nEnter value to insert at head: "))
dll.insert_at_head(head_val)

print("\nAfter Insert At Head:")
dll.display()


target = int(input("\nInsert after value: "))
new_val = int(input("Enter new value: "))

dll.insert_in_between(target, new_val)

print("\nAfter Insert In Between:")
dll.display()


print("\nAppend")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

print("\nInsert At Head")
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")

print("\nInsert In Between")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")