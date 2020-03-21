# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


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
        factor = 0
        while number % prime == 0 and number > 1:
            number = number / prime
            factor += 1

        if factor > 0:
            yield prime, factor

        if number == 1:
            break

    if number > 1:
        yield number, 1


def smallest_positive_number(start, stop):
    factors = {}

    for i in range(start, stop):
        for prime, factor in largest_prime_factor(i):
            if factors.get(prime) == None or factors[prime] < factor:
                factors[prime] = factor

    print("hey: ", factors)
    print("aa", factors.get(200) == None)
    n = 1
    for key, value in factors.items():
        print("key", key, value)
        n *= pow(key, value)

    return n


print("Smallest positive is: ", smallest_positive_number(1, 20))
