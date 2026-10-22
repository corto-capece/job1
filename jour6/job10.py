L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
total = 1
found = False

for number in L:
    if 25 <= number <= 90:
        total *= number
        found = True

if found is not True:
    total = 0

print(total)