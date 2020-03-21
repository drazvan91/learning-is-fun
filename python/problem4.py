# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


def generate_products(min, max):
    for i in range(max, min, -1):
        if i % 50 == 0:
            print("Checkpoint: ", i)

        for j in range(i-1, min, -1):
            yield i*j


def find_biggest_palindrom(min, max):
    largest_palindrom = 0
    for n in generate_products(min, max):
        if largest_palindrom < n and isPalindrome(str(n)):
            print("New largest: ", n)
            largest_palindrom = n

    return largest_palindrom


print("largest palindrom is: ", find_biggest_palindrom(100, 999))
