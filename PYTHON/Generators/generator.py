# generators : generators are a simple way of creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example of a generator is shown below:
def my_range(start, end):
    current = start
    while current < end:
        # print(f"Yielding {current}")
        yield current
        # yaha yeh current value return karega aur next() call hone par wapas se yaha se start karega, aur current value ko 1 se increment karega
        current += 1
for i in my_range(1, 10):
    print(i)
    
    
# difference between generator and normal function :
# 1. A normal function returns a single value, while a generator can yield multiple values one at a time, allowing for more efficient memory usage.
# 2. A normal function executes all its code when called, while a generator can pause its execution and resume later, which is useful for handling large datasets or infinite sequences.
# 3. A normal function uses the return statement to return a value, while a generator uses the yield statement to produce a value and pause its execution.
# 4. A normal function is not an iterator, while a generator is an iterator that can be iterated over using a for loop or the next() function.
# 5. A normal function can be called multiple times and will execute its code each time, while a generator can only be iterated over once, as it maintains its state between iterations.