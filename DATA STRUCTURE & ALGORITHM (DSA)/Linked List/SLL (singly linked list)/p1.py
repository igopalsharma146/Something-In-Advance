# remove the nth element from the end
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    
    #creating linked list
    def creating_linked_list(self,arr):
        
        if len(arr)==0:
            return None
        
        self.head=Node(arr[0])
        curr=self.head
        
        for i in range(1,len(arr)):
            curr.next=Node(arr[i])
            curr=curr.next
        return curr
        
    def display(self):
        curr=self.head
        if curr is None:
            print("Emplty Linked List.")
            return
        while curr is not None:
            print(f"{curr.val} -> ",end="")
            curr=curr.next
            
    def delete_At_The_end(self,n):
        slow,fast=self.head,self.head
        for _ in range(n):
            fast=fast.next
        
        if fast==None:
            self.head=self.head.next
            return self.head
        else:
            while fast.next is not None:
                slow=slow.next
                fast=fast.next
            slow.next=slow.next.next
            return self.head
    
    
l1=SLL()
arr=list(map(int,input("Enter the array elements : ").split()))
r=l1.creating_linked_list(arr)
print(r.val)
l1.display()
l1.delete_At_The_end(5)
print("\n")
l1.display()