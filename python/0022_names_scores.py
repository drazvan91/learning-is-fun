# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

file_object = open("./python/0022_input.txt", "r")
file = file_object.read()
names = file.split(",")
names = list(sorted(map(lambda name: name.strip('"'), names)))


def value(name):
    sum = 0
    for l in name:
        sum += ord(l)-ord('A')+1

    return sum


total = 0
for i in range(len(names)):
    v = value(names[i])
    total += v * (i+1)

print(total)
