def even_parameters(n):
    def wrapper(*args):
        if len(args) == len([el for el in args if isinstance(el, int) and not el % 2 == 1]):
            res = n(*args)
            return res

        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
