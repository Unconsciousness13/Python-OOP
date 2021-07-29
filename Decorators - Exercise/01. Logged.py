def logged(fun):
    def wrapper(*args, **kwargs):
        funct = fun(*args, **kwargs)
        result = f"you called {fun.__name__}{args}\nit returned {funct}"
        return result

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
