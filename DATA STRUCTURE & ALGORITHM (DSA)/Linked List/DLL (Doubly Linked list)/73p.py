# Creating a DLL
class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None
    
    # 1. Insert At Head
    def insert_at_head(self,val):
        new_node=Node(val)
        
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            
    # 2. Append At the End
    def Append(self,val):
        new_node=Node(val)
        
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr
            
    # 3. Insert In Between
    def insert_in_between(self,val,position):
        new_node=Node(val)
        
        if position==0:
            self.insert_at_head(val)
            return
        else:
            curr=self.head
            count=1
            while count<position and curr is not None:
                curr=curr.next
                count+=1
            
            if curr is None:
                print("Position out of Bounds.")
                return
            new_node.prev=curr.prev
            curr.prev.next=new_node
            curr.prev=new_node
            new_node.next=curr
    
    # def insert_in_between(self,val,position):
    #     new_node=Node(val)

    #     if position==0:
    #         self.insert_at_head(val)
    #         return

    #     curr=self.head
    #     count=1

    #     while count<position and curr is not None:
    #         curr=curr.next
    #         count+=1

    #     if curr is None:
    #         print("Position out of Bounds.")
    #         return

    #     new_node.next=curr.next
    #     new_node.prev=curr

    #     if curr.next is not None:
    #         curr.next.prev=new_node

    #     curr.next=new_node
    
    # 4. Display
    def Display(self):
        curr=self.head
        if curr is None:
            print("Elements Not Present Please Add First")
        else:
            while curr is not None:
                print(f"{curr.val} -> ",end="")
                curr=curr.next
            print("None")

n1=DLL()
n1.Display()

n1.insert_at_head(5)
n1.insert_at_head(10)
n1.insert_at_head(15)
n1.insert_at_head(20)
n1.Display()

n1.insert_in_between(12,3)
n1.Display()
n1.insert_in_between(17,5)
n1.Display()
n1.insert_in_between(25,7)
n1.Display()
n1.insert_in_between(30,6)
n1.Display()
