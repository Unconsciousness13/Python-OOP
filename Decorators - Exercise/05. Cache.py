def cache(func):
    def wrapper(n):
        res = func(n)

        if n not in wrapper.log:
            wrapper.log[n] = res

        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
