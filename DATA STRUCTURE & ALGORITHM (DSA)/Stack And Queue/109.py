# Deque : Double Ended Queue

# difference between queue and deque is that in queue we can insert and delete elements from one end only but in deque we can insert and delete elements from both ends. and queue take O(n) time for insertion and deletion but deque take O(1) time for insertion and deletion.

# Program: Implement Deque Using Array
from collections import deque

lst=deque([])
lst.append(10)
lst.append(20)
lst.append(30)
lst.appendleft(234)
lst.appendleft(278)

print("Deque:", lst)

lst.pop()
print("Deque:", lst)
lst.popleft()
print("Deque after deletion:", lst)