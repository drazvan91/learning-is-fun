# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import math


def sum_fifth_power(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += math.pow(digit, 5)
        number = number // 10

    return sum


def get_all_numbers(less_than):
    for i in range(2, less_than):
        if sum_fifth_power(i) == i:
            yield i


sum = 0
for nr in get_all_numbers(1000000):
    print("nr: ", nr)
    sum += nr

print("sum: ", sum)
