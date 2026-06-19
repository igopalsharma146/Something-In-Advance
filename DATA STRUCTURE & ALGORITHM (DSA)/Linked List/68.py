# Program: Find Starting Point of Cycle in Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Input
n = int(input("Enter number of nodes: "))

arr = list(map(int, input("Enter node values: ").split()))

nodes = [Node(x) for x in arr]

for i in range(n - 1):
    nodes[i].next = nodes[i + 1]

pos = int(input("Enter cycle position (-1 for no cycle): "))

if pos != -1:
    nodes[-1].next = nodes[pos]

head = nodes[0]


# Brute Force Approach
visited = set()

curr = head
start_node = None

while curr:

    if curr in visited:
        start_node = curr
        break

    visited.add(curr)
    curr = curr.next

print("\nBrute Force Approach")

if start_node:
    print("Starting Node of Cycle:", start_node.val)
else:
    print("No Cycle")

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Better Approach

print("\nBetter Approach")
print("Optimal Solution is same as Better Solution.")
print("Optimal Solution is not available.")
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
slow = head
fast = head

cycle = False

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle = True
        break

start_node = None

if cycle:

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    start_node = slow

print("\nOptimal Approach")

if start_node:
    print("Starting Node of Cycle:", start_node.val)
else:
    print("No Cycle")

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")