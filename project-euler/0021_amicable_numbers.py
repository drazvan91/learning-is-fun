# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math


def get_divizors(nr):
    m = math.floor(math.sqrt(nr))
    yield 1
    for i in range(2, m):
        if nr % i == 0:
            yield i
            yield nr // i


def sum_of_divizors(nr):
    sum = 0
    for divizor in get_divizors(nr):
        sum += divizor

    return sum


def get_array(n):
    sums = [0]
    for i in range(1, n):
        sum = sum_of_divizors(i)
        sums.append(sum)

    return sums


m = get_array(30000)
sum_of_sum = 0
for i in range(1, 10000):
    if m[m[i]] == i and m[i] != i:
        sum_of_sum += i
        print(i, m[i])

print(sum_of_sum)
