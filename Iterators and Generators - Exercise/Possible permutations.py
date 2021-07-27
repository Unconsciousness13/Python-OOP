from itertools import permutations


def possible_permutations(li):
    return (list(p) for p in permutations(li))


[print(n) for n in possible_permutations([1, 2, 3])]
