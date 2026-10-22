L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
total = 0

for number in L:
    if number % 2 == 0:
        total += number

print(total)