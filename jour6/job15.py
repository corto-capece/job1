L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

length = 0
for number in L:
    length += 1

for index in range(length):
    number = int(L[index])
    float_number = L[index] - number    

    if float_number >= 0.5:
        L[index] = number + 1

    else:
        L[index] = number


def sort_list(L):
    length = 0
    for number in L:
        length += 1

    index1 = 0

    while index1 < length:
        index2 = index1 + 1

        while index2 < length:
            if L[index1] > L[index2]:
                x = L[index1]
                L[index1] = L[index2]
                L[index2] = x

            index2 += 1

        index1 += 1

    return L

print(sort_list(L))