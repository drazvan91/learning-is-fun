# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


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


def prime_generator(max_number):
    i = 2
    nr = 5
    sum = 5
    while nr < max_number:
        if is_prime(nr):
            found_primes.append(nr)
            sum += nr
            i += 1

        nr += 2

    return sum


sum = prime_generator(2_000_000)
print(sum)
