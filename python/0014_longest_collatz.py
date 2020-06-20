# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

distances = {}
distances[1] = 1

result = (0, 0)


def process_distance(number):
    global result
    if distances.get(number):
        return distances[number]

    next = 0
    if number % 2 == 0:
        next = process_distance(number/2) + 1
    else:
        next = process_distance(3*number+1) + 1

    distances[number] = next
    if result[0] < next:
        result = (next, number)

    return next


def process_all(up_to):
    for i in range(1, up_to):
        process_distance(i)


process_all(1000000)


print("max len: ", result[0])
print("Result: ", result[1])
print("dist for 13: ", distances[13])
