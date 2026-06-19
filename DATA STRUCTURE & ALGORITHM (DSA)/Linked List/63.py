# Append And Traverse a LL
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    #Display
    def display(self):
        curr=self.head
        if curr is None:
            print("Empty Linked List")
        else:
            while curr is not None:
                print(f"{curr.val}",end=" -> ")
                curr=curr.next
    
    #Append
    def append(self,val):
        new_node=Node(val) #pahle ham value ko node me convert karenge
        
        if self.head==None:
            self.head=new_node #agar hamara head empty h new node ko hum head banayenge
        else:
            curr=self.head
            while curr is not None and curr.next is not None:
                curr=curr.next
            curr.next=new_node

l1=LinkedList()
l1.display()
l1.append(5)
l1.append(10)
l1.append(32)
l1.display()
