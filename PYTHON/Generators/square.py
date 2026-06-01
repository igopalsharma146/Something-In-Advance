# printing square numbers using generator
def square_numbers(n):
    for i in range(1,n+1):
        yield i ** 2

gen= square_numbers(10)
print(gen) # <generator object square_numbers at 0x7f8b8c8c8c8>
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9

for num in gen:
    print(num) # 16, 25, 36, 49, 64, 81

for num in gen:
    print(num) # nothing will be printed because the generator has already been exhausted

for num in square_numbers(5):
    print(num) # 1, 4, 9, 16, 25