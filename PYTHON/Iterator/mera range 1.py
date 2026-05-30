# iterable
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self)
class MyRangeIterator:
    def __init__(self, my_range):
        self.my_range = my_range
        self.current = my_range.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.my_range.end:
            current_value = self.current
            self.current += 1
            return current_value
        else:
            raise StopIteration
my_range = MyRange(1, 10)
for i in my_range:
    print(i)