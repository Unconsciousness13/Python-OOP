# iterator
class vowels:
    _vowels = {'a', 'e', 'o', 'y', 'u', 'i', 'I', 'A', 'E', 'O', 'Y', 'U'}

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        ch = self.text[self.index]
        self.index += 1
        if ch not in self._vowels:
            return self.__next__()

        return ch


# generator funcion
# def vowels(text):
#
#     vowels = {'a', 'e', 'o', 'y', 'u', 'i', 'I', 'A', 'E', 'O', 'Y', 'U'}
#     for ch in text:
#         if ch in vowels:
#             yield ch

# generator comprehension
# def vowels(text):
#     vowels = {'a', 'e', 'o', 'y', 'u', 'i', 'I', 'A', 'E', 'O', 'Y', 'U'}
#     return (ch for ch in text if ch in vowels)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
