# In the United Kingdom the currency is made up of pound(£) and pence(p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

coin_types = [200, 100, 50, 20, 10, 5, 2, 1]


def goDeep(remaining, next_index):
    if next_index == len(coin_types):
        if remaining == 0:
            return 1
        else:
            return 0

    coin = coin_types[next_index]
    perms = 0

    for value in range(remaining // coin, -1, -1):
        perms += goDeep(remaining - (value * coin), next_index+1)

    return perms


different_ways = goDeep(200, 0)
print("result:", different_ways)
