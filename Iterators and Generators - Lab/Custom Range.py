class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        value = self.value
        self.value += 1
        return value


for x in custom_range(1,10):
    print(x)
