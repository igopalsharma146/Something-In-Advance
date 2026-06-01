# benifits of using generator :
# 1. Memory Efficiency: Generators produce items one at a time and only when requested, which can save a lot of memory when working with large datasets or infinite sequences.
print("Memory efficiency of generators:")
large_range = [x for x in range(10000)]  
large_generator = (x for x in range(10000))
print("Memory usage of list:", large_range.__sizeof__())
print("Memory usage of generator:", large_generator.__sizeof__())

# 2. easy to implement: Generators can be implemented using simple functions with the yield statement, making them easy to write and understand.
print("Counting up to 5:")
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for number in count_up_to(5):
    print(number)
    
# 3. Represent infinite sequences: Generators can represent infinite sequences, such as the Fibonacci sequence or prime numbers, without consuming infinite memory.
    # print("Fibonacci sequence:")
    # def fibonacci():
    #     a, b = 0, 1
    #     while True:
    #         yield a
    #         a, b = b, a + b
    # fib_gen = fibonacci()
    # for _ in range(10):
    #     print(next(fib_gen))
print("Even numbers:")
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2
even_gen = even_numbers()
for _ in range(10):
    print(next(even_gen))
    
# 4. Chaining operations: Generators can be easily chained together to create complex data processing pipelines, allowing for efficient and readable code.
print("Chaining generators:")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def squares(gen):
    for number in gen:
        yield number ** 2
fib_gen = fibonacci()
squared_fib_gen = squares(fib_gen)
print("Squared Fibonacci numbers:")
for _ in range(10):
    print(next(squared_fib_gen))