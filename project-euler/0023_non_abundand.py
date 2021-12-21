# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math


def get_divizors(nr):
    m = math.floor(math.sqrt(nr))
    yield 1
    for i in range(2, m+1):
        if nr % i == 0:
            yield i
            if i != nr // i:
                yield nr // i


def sum_of_divizors(nr):
    sum = 0
    for divizor in get_divizors(nr):
        sum += divizor

    return sum


limit = 28123

numbers = []

for i in range(1, limit):
    if sum_of_divizors(i) > i:
        numbers.append(i)

sums = []
for i in range(0, limit):
    sums.append("")

for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        sum = numbers[i]+numbers[j]
        if sum < limit:
            sums[sum] = str(numbers[i])+"_"+str(numbers[j])

total = 0
for i in range(0, limit):
    if sums[i] == "":
        total += i
    else:
        if i < 200:
            print(str(i)+" - "+sums[i])

print(total)
