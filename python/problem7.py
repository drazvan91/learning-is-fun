# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

found_primes = [3]


def is_prime(number):
    max = math.sqrt(number)
    for i in found_primes:
        if i > max:
            return True

        if number % i == 0:
            return False

    return True


def prime_generator(number_of_primes):
    i = 2
    nr = 5
    while i < number_of_primes:
        if is_prime(nr):
            found_primes.append(nr)
            i += 1

        nr += 2


prime_generator(10001)
print(found_primes)
