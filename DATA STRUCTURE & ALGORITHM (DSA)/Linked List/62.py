# Bsic program of node

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

node1=Node(5)
node2=Node(6)
node3=Node(10)
node4=Node(11)
node5=Node(15)

print(node1)
print(node1.val)
print(node1.next)

#connecting each other node
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

print(node2)
print(node2.val)
print(node2.next.val)