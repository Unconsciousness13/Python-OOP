def make_bold(name):
    def wrapper(*args):
        res = name(*args)
        outp = f"<b>{res}</b>"
        return outp
    return wrapper


def make_italic(name):
    def wrapper(*args):
        res = name(*args)
        outp = f"<i>{res}</i>"
        return outp
    return wrapper


def make_underline(name):
    def wrapper(*args):
        res = name(*args)
        outp = f"<u>{res}</u>"
        return outp
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
