class Calculator:
    def add(*args):
        result = 0
        for el in args:
            result += el
        return result

    def multiply(*args):
        result = 1
        for el in args:
            result *= el
        return result

    def divide(*args):
        result = 0
        counter = 0
        for el in args:
            counter += 1
            if counter == 1:
                result = el
            else:
                result /= el
        return result

    def subtract(*args):
        result = 0
        counter = 0
        for el in args:
            counter += 1
            if counter == 1:
                result = el
                continue
            if el >= 0:
                result -= el
            else:
                result += abs(el)
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
