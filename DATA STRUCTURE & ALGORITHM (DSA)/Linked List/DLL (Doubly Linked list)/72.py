# Simple Program of Doubly Linked List
class DLL:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
        

node1=DLL(5)
node2=DLL(10)
node3=DLL(15)
node4=DLL(17)
node5=DLL(19)

node1.next=node2
node2.prev=node1
node2.next=node3
node3.prev=node2
node3.next=node4
node4.prev=node3
node4.next=node5
node5.prev=node4

print(node1.next.next.next.val)
print(node5.prev.prev.prev.prev.val)