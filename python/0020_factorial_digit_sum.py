# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

factorial = 1
for i in range(1, 100):
    factorial *= i

    while factorial % 10 == 0:
        factorial = factorial // 10


sum = 0
while factorial > 0:
    sum += factorial % 10
    factorial = factorial // 10

print(sum)
