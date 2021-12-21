# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import math


def is_digit_factorial(nr):
    nr2 = nr
    sum = 0
    while nr2 > 0:
        digit = nr2 % 10
        sum += math.factorial(digit)
        nr2 = nr2 // 10

    return sum == nr


sum = 0
for i in range(3, 1000000):
    if is_digit_factorial(i):
        sum += i
        print(i)

print("Sum: ", sum)
