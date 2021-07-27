def read_next(*args):
    for arg in args:
        for ar in arg:
            ar = str(ar)
            for a in ar:
                yield a


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
