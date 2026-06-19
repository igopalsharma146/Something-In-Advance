# Append, Traversal, Insert at an specific position and Delete a Node
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    #Display Or Traverse
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
    
    # Insert
    def insert(self,position,val):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current_node=self.head
            prev_node=None
            count=0
            while current_node is not None and count<position:
                prev_node=current_node
                current_node=current_node.next
                count+=1
            prev_node.next=new_node
            new_node.next=current_node
    
    # DELETE
    def Delete(self, val):
        temp = self.head

        # Empty List
        if temp is None:
            print("Linked List is Empty")
            return

        # Delete Head Node
        if temp.val == val:
            self.head = temp.next
            del temp
            return

        prev = None
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
                del temp
                return

            prev = temp
            temp = temp.next
        print("Node Not Found")

l1=LinkedList()
# Appending More than 1 Value
# n=int(input("Enter the to no. of element in LL :"))
# for i in range(0,n):
#     val=int(input(f"Enter the {i+1} Value :"))
#     l1.append(val)
l1.display()
l1.insert(0,5)
l1.insert(2,8)
l1.insert(1,9)
l1.Delete(8)
l1.display()

