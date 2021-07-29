def type_check(type_of_argument):
    def dec(t):
        def wrapper(arg):
            if type(arg) != type_of_argument:
                return "Bad Type"
            func = t(arg)
            return func

        return wrapper

    return dec


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
