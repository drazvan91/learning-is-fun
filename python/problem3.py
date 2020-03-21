# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

test_number = 13195
input_number = 600851475143


def is_prime(number):
    if number % 2 == 0:
        return False

    for i in range(3, int(number / 2), 2):
        if number % i == 0:
            return False

    return True


def generate_primes(max):
    yield 2
    for i in range(3, max, 2):
        if is_prime(i):
            yield i


def largest_prime_factor(number):
    primes = generate_primes(number)
    for prime in primes:
        print("prime", prime, "number", number)
        while number % prime == 0 and number > 1:
            number = number / prime
            print("number", number)

        if number == 1:
            return prime

    return 0


print("Largest prime factor:", largest_prime_factor(test_number))
print("Largest prime factor:", largest_prime_factor(input_number))
