# Space Complexity बताती है कि किसी algorithm को execution के दौरान कितनी extra memory (RAM) की जरूरत पड़ती है।

# इसे भी Big-O notation में लिखा जाता है।

# Formula
# Space Complexity=Input Space+Auxiliary Space

# लेकिन interview में ज्यादातर Auxiliary Space (extra memory) की बात की जाती है।

a = 10
b = 20
c = a + b

# चाहे input कितना भी बड़ा हो, केवल कुछ variables use हो रहे हैं।

# Space Complexity = O(1)
n=5
arr = []
for i in range(n):
    arr.append(i)

# arr में n elements store होंगे।

# Space Complexity = O(n)

matrix = [[0] * n for _ in range(n)]
print(matrix)

# यह n × n matrix बना रहा है।

# Space Complexity = O(n²)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
# Time Complexity = O(2ⁿ)
# Space Complexity = O(n)

# क्योंकि recursion stack की maximum depth n तक जा सकती है।

# Quick Trick
# Extra variables only → O(1)
# Array of size n → O(n)
# Matrix n × n → O(n²)
# Recursion depth n → O(n)
# Recursion depth log n → O(log n)