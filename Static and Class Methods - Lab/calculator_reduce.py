from functools import reduce


class Calculator:
    @classmethod
    def add(cls, *args):
        result = reduce(lambda x, y: x + y, args)
        return result

    @classmethod
    def multiply(cls, *args):
        result = reduce(lambda x, y: x * y, args)
        return result

    @classmethod
    def divide(cls, *args):
        result = reduce(lambda x, y: x / y, args)
        return result

    @classmethod
    def subtract(cls, *args):
        result = reduce(lambda x, y: x - y, args)
        return result
