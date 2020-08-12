# Euler discovered the remarkable quadratic formula:


# It turns out that the formula will produce 40 primes for the consecutive integer values . However, when  is divisible by 41, and certainly when  is clearly divisible by 41.

# The incredible formula  was discovered, which produces 80 primes for the consecutive values . The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# , where  and

# where  is the modulus/absolute value of
# e.g.  and
# Find the product of the coefficients,  and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .

def is_prime(number):
    if number < 0:
        return False
    if number % 2 == 0:
        return False

    for i in range(3, int(number / 2), 2):
        if number % i == 0:
            return False

    return True


def get_number_of_consecutive_primes(a, b):
    count = 0
    n = 0
    while True:
        value = (n*n) + (a*n) + b
        if not is_prime(value):
            return n

        n += 1


def get_max():
    max_consecutive = -1
    max_a = 0
    max_b = 0
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            consecutive = get_number_of_consecutive_primes(a, b)
            if max_consecutive < consecutive:
                max_consecutive = consecutive
                max_a = a
                max_b = b

    return (max_a, max_b, max_consecutive)


(a, b, m) = get_max()
print(a*b)
