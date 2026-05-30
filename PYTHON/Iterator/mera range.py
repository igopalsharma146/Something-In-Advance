class MeraRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += 1
            return current
        else:
            raise StopIteration
mera_range = MeraRange(1, 10)
for i in mera_range:
    print(i)