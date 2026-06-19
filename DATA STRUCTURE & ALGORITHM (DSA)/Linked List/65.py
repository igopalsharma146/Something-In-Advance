# Program: Find Middle of Linked List

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


# Input
arr = list(map(int, input("Enter linked list elements: ").split()))
head = create_linked_list(arr)


# Brute Force Approach
count = 0
curr = head

while curr:
    count += 1
    curr = curr.next

middle = count // 2

curr = head

for _ in range(middle):
    curr = curr.next

print("\nBrute Force Approach")
print("Middle Node:", curr.val)

print("Time Complexity: O(n + n/2)")
print("Space Complexity: O(1)")


# Better Approach
nodes = []

curr = head

while curr:
    nodes.append(curr)
    curr = curr.next

middle = len(nodes) // 2

print("\nBetter Approach")
print("Middle Node:", nodes[middle].val)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print("\nOptimal Approach")
print("Middle Node:", slow.val)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")