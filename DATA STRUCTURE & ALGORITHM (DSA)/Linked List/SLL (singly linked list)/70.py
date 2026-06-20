# Program: Odd Even Linked List

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

odd = []
even = []

for i in range(len(values)):

    if i % 2 == 0:
        odd.append(values[i])
    else:
        even.append(values[i])

result = odd + even

new_head = create_linked_list(result)

print("\nBrute Force Approach")
display(new_head)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Better Approach
odd_nodes = []
even_nodes = []

curr = head
index = 1

while curr:

    if index % 2:
        odd_nodes.append(curr.val)
    else:
        even_nodes.append(curr.val)

    index += 1
    curr = curr.next

new_head = create_linked_list(odd_nodes + even_nodes)

print("\nBetter Approach")
display(new_head)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
head2 = create_linked_list(arr)

if head2 is None or head2.next is None:

    print("\nOptimal Approach")
    display(head2)

else:

    odd = head2
    even = head2.next
    even_head = even

    while even and even.next:

        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    print("\nOptimal Approach")
    display(head2)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")