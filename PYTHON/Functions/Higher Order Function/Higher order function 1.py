# higher order function
# create a normal and higher order function that takes list as input and returns the sum of all the even numbers, odd numbers and divisible by 3 in the list.
# normal function to calculate the sum of all elements in the list

def sum_even_odd_div3(lst):
    even_sum = 0
    odd_sum = 0
    div3_sum = 0
    for num in lst:
        if num % 2 == 0:
            even_sum += num
        if num % 2 != 0:
            odd_sum += num
        if num % 3 == 0:
            div3_sum += num
    return even_sum, odd_sum, div3_sum
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum, odd_sum, div3_sum = sum_even_odd_div3(lst)
print("Sum of even numbers:", even_sum)  # This will print 30
print("Sum of odd numbers:", odd_sum)  # This will print 25
print("Sum of numbers divisible by 3:", div3_sum)  # This will print 18
result = sum_even_odd_div3(lst)
print("Result from normal function:", result)  # This will print (30, 25, 18)

print("\nUsing higher order function to calculate the sum of even, odd and divisible by 3 numbers...")
# higher order function that takes another function as an argument
def higher_order_sum(lst, condition):
    return sum(num for num in lst if condition(num))

# Define conditions
is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0
is_divisible_by_3 = lambda x: x % 3 == 0

# Calculate sums using higher order function
even_sum = higher_order_sum(lst, is_even)
odd_sum = higher_order_sum(lst, is_odd)
div3_sum = higher_order_sum(lst, is_divisible_by_3)

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
print("Sum of numbers divisible by 3:", div3_sum)
