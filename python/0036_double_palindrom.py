# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrom(nr, base, extra):
    digit = nr % base
    nr = nr // base
    extra.append(digit)
    if nr > 0:
        return is_palindrom(nr, base, extra)

    for i in range(len(extra)):
        if extra[i] != extra[len(extra)-i-1]:
            return False
    
    return True

count = 0
sum = 0
for i in range(1_000_000):
    if is_palindrom(i, 10, []) and is_palindrom(i, 2, []):
        print(i)
        count += 1
        sum += i


print("Sum: ", sum)