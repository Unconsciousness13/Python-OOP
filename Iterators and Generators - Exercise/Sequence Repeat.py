class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx < self.number:
            idx = self.current_idx
            self.current_idx += 1
            return self.sequence[idx % len(self.sequence)]
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
