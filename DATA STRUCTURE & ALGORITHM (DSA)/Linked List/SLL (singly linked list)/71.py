# Program: Delete Nth Node From End of Linked List

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
n = int(input("Enter nth node from end to delete: "))

head = create_linked_list(arr)


# Brute Force Approach
length = 0
curr = head

while curr:
    length += 1
    curr = curr.next

delete_pos = length - n

temp_head = create_linked_list(arr)

if delete_pos == 0:
    temp_head = temp_head.next

else:
    curr = temp_head

    for _ in range(delete_pos - 1):
        curr = curr.next

    curr.next = curr.next.next

print("\nBrute Force Approach")
display(temp_head)

print("Time Complexity: O(n + n)")
print("Space Complexity: O(1)")


# Better Approach
values = arr[:]

delete_index = len(values) - n

if 0 <= delete_index < len(values):
    values.pop(delete_index)

temp_head = create_linked_list(values)

print("\nBetter Approach")
display(temp_head)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


# Optimal Approach
head2 = create_linked_list(arr)

dummy = Node(0)
dummy.next = head2

fast = dummy
slow = dummy

for _ in range(n):
    fast = fast.next

while fast.next:
    fast = fast.next
    slow = slow.next

slow.next = slow.next.next

print("\nOptimal Approach")
display(dummy.next)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")