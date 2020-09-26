# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


def is_pandigital(numbers, n):
    digits = {0}
    for number in numbers:
        while number > 0:
            digit = number % 10
            if digit in digits:
                return False
            digits.add(digit)

            number = number // 10

    for i in range(1, n+1):
        if i not in digits:
            return False

    return True


# is_pandigital([39 187 7293])
results = set()
sum = 0
for i in range(1, 100):
    for j in range(i, 100000):
        prod = i*j
        if is_pandigital([i, j, prod], 9):
            print(i, j, prod)
            if prod not in results:
                results.add(prod)
                sum += prod
            else:
                print("Already exists")

print("Result: ", results)
print("Sum: ", sum)
