#check if string is a palindrome

#using for loop
print("\nusing for loop :")
s="najarajan"
left=0
n=len(s)
right=n-1
for i in range(1,n//2+1):
    if s[left]!=s[right]:
        print("It is not a palindrome string.")
        break
    left+=1
    right-=1
else:
    print("Palindrome")
    
# using while loop
print("\nusing while loop :")
s="najarajan"
left=0
n=len(s)
right=n-1
while left<right:
    if s[left]!=s[right]:
        print("It is not a palindrome string.")
        break
    left+=1
    right-=1
else:
    print("Palindrome")
    
# using Recursion
print("\nusing Recursion :")
def palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        print("It is not a palindrome string.")
        return False
    return palindrome(s,left+1,right-1)
n=len(s)
left=0
right=n-1
print(palindrome(s,left,right))
