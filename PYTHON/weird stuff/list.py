# list
l1=[[2,3],[4,5],8,9]
print(id(l1))

l1.append(10)
print(id(l1))  # Output: Same memory address

l1[0].append(6)
print(id(l1),l1)  # Output: Same memory address

print("\nNow let's check the behavior for a tuple:")
l2=([2,3],[4,5],8,9)
print(id(l2),l2)  # Output: Same memory address
l2[0].append(6)
print(id(l2),l2)  # Output: Same memory address

l2[0].clear()
print(id(l2),l2)  # Output: Same memory address

# l2.__add__([10,11])
# print(id(l2),l2)  # Output: Same memory address, but the content of l2 is not changed because tuples are immutable, so the __add__ method returns a new tuple without modifying the original one.