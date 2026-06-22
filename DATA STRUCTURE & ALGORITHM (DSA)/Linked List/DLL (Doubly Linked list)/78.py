# # Program: Find Pairs With Given Sum in DLL (Brute Force)

class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None


class DLL:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
            return

        curr=self.head
        while curr.next:
            curr=curr.next

        curr.next=new_node
        new_node.prev=curr

    def find_pairs(self,target):
        pairs=[]
        first=self.head

        while first:
            second=first.next

            while second:
                if first.val+second.val==target:
                    pairs.append((first.val,second.val))

                second=second.next
            first=first.next
        return pairs

dll=DLL()

arr=list(map(int,input("Enter sorted DLL elements: ").split()))
for num in arr:
    dll.append(num)

target=int(input("Enter target sum: "))
pairs=dll.find_pairs(target)

print("\nBrute Force Approach")
print("Pairs:",pairs)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# Program: Find Pairs With Given Sum in DLL (Better)
print("\nBetter Solution:")
class DLL1:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
            return

        curr=self.head
        while curr.next:
            curr=curr.next

        curr.next=new_node
        new_node.prev=curr

    def find_pairs(self,target):
        seen=set()
        pairs=[]
        curr=self.head

        while curr:
            complement=target-curr.val
            if complement in seen:
                pairs.append((complement,curr.val))

            seen.add(curr.val)
            curr=curr.next
        return pairs


dll=DLL1()

arr=list(map(int,input("Enter DLL elements: ").split()))
for num in arr:
    dll.append(num)

target=int(input("Enter target sum: "))
pairs=dll.find_pairs(target)

print("\nBetter Approach")
print("Pairs:",pairs)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")



# Program: Find Pairs With Given Sum in Sorted DLL (Optimal)
print("\nOptimal Solution :")
class DLL2:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
            return

        curr=self.head
        while curr.next:
            curr=curr.next

        curr.next=new_node
        new_node.prev=curr

    def find_pairs(self,target):
        pairs=[]
        left=self.head
        right=self.head

        while right.next:
            right=right.next

        while left != right and left.prev != right:
            total=left.val+right.val

            if total==target:
                pairs.append((left.val,right.val))
                left=left.next
                right=right.prev

            elif total<target:
                left=left.next

            else:
                right=right.prev
        return pairs

dll=DLL2()

arr=list(map(int,input("Enter sorted DLL elements: ").split()))
for num in arr:
    dll.append(num)

target=int(input("Enter target sum: "))
pairs=dll.find_pairs(target)

print("\nOptimal Approach")
print("Pairs:",pairs)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")