def tags(tag):
    def decorator(fn):
        def wrapper(*args):
            func = fn(*args)
            result = f"<{tag}>{func}</{tag}>"
            return result

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
