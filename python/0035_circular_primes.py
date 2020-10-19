# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import math

found_primes = [2, 3]


def is_prime(number):
    max = math.sqrt(number)
    for i in found_primes:
        if i > max:
            return True

        if number % i == 0:
            return False

    return True


def prime_generator(below_number):
    nr = 5
    while nr < below_number:
        if is_prime(nr):
            found_primes.append(nr)

        nr += 2

def number_of_digits(number):
    if number < 10:
        return 1
    if number < 100:
        return 2
    if number <1000:
        return 3
    if number < 10000:
        return 4
    if number < 100000:
        return 5
    if number < 1000000:
        return 6
    raise "should not touch this point"

def get_rotations(number):
    nr_digits = number_of_digits(number)
    for i in range(nr_digits-1):
        remainder = number % 10
        number = (number // 10) + (remainder * math.pow(10,nr_digits-1))
        yield number

def was_found(number):
    for i in found_primes:
        if i==number:
            return True
        if i>number:
            return False

def is_circular_prime(number):
    for rotation in get_rotations(number):
        if not was_found(rotation):
            return False
    
    return True

def get_circular_primes():
    for i in found_primes:
        if is_circular_prime(i):
            yield i


prime_generator(1_000_000)
count = 0
for circular_prime in get_circular_primes():
    count+=1

print("Result:", count)

