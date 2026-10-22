L = [1, 2, 3, 4, 5]
print(L)
print(L[1])

def remplacer(L):
    L[3] = L[2] + L[4]

remplacer(L)
print(L)
print(L[-1])