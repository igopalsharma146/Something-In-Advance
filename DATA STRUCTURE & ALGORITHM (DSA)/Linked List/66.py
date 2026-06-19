# Program: Reverse a Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    curr = head

    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next

    return head


def display(head):
    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))
head = create_linked_list(arr)


# Brute Force Approach
values = []

curr = head
while curr:
    values.append(curr.val)
    curr = curr.next

curr = head
i = len(values) - 1

while curr:
    curr.val = values[i]
    i -= 1
    curr = curr.next

print("\nBrute Force Approach")
display(head)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Better Approach
head2 = create_linked_list(arr)

stack = []

curr = head2
while curr:
    stack.append(curr.val)
    curr = curr.next

curr = head2
while curr:
    curr.val = stack.pop()
    curr = curr.next

print("\nBetter Approach")
display(head2)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
head3 = create_linked_list(arr)

prev = None
curr = head3

while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
head3 = prev

print("\nOptimal Approach")
display(head3)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")