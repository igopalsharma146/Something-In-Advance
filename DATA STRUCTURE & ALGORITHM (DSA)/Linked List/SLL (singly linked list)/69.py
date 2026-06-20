# Program: Find Length of Loop in Linked List

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
visited = {}
curr = head
index = 0

loop_length = 0

while curr:

    if curr in visited:
        loop_length = index - visited[curr]
        break

    visited[curr] = index
    index += 1
    curr = curr.next

print("\nBrute Force Approach")
print("Loop Length:", loop_length)

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

loop_length = 0

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

    if slow == fast:

        loop_length = 1
        temp = slow.next

        while temp != slow:
            loop_length += 1
            temp = temp.next

        break

print("\nOptimal Approach")
print("Loop Length:", loop_length)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")