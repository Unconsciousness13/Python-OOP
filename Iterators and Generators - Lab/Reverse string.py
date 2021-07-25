def reverse_text(text):
    for ch in text[::-1]:
        yield ch


for char in reverse_text("step"):
    print(char, end='')
