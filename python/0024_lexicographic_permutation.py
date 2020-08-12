# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers = [0, 1, 2, 3]


def perm(prefix, remaining, number, wanted_number):
    if len(remaining) == 0:
        print(prefix)
        if number == wanted_number - 1:
            print("This is it")
        return 1

    for r in remaining:
        if number >= wanted_number:
            return number

        next_generated = math.factorial(len(remaining)-1)
        if len(remaining) > 1 and (number + next_generated < wanted_number):
            number += next_generated
        else:
            new_prefix = prefix.copy()
            new_prefix.append(r)
            new_remaining = remaining.copy()
            new_remaining.remove(r)
            number += perm(new_prefix, new_remaining, number, wanted_number)

    return number


perm([], numbers, 0, 1_000_000)
