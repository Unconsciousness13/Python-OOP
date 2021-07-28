def even_numbers(function):
    def wrapper(numbers):
        let = function(numbers)
        return [num for num in let if num % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
