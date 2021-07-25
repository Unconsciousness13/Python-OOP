def genrange(start, end):
    for n in range(start, end + 1):
        yield n


print(list(genrange(1, 10)))
