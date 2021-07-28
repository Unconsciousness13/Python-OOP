def vowel_filter(function):
    def wrapper():
        out = function()
        letters = "aeouyi"
        return [let for let in out if let.lower() in letters]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
