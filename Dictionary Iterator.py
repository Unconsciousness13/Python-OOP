class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary_elements = list(dictionary.items())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.dictionary_elements):
            idx = self.current_index
            self.current_index += 1
            return self.dictionary_elements[idx]
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
