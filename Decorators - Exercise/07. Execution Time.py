from time import time
from functools import wraps


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))
