# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def get_number_of_digits(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10

    return count


def fibonnaci():
    yield 1
    yield 1

    a = 1
    b = 1

    while True:
        c = a+b
        a = b
        b = c
        yield c


def find_number(number_of_digits):
    nth = 0
    for nr in fibonnaci():
        nth = nth + 1
        if get_number_of_digits(nr) == number_of_digits:
            return (nth, nr)


print(find_number(1000))
