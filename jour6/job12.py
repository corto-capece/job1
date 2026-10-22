L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

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