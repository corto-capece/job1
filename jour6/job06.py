L = [1, 2, 3, 4, 5]
print(L)

def intervert(L):
    first_index = L[0]
    last_index = L[-1]
    
    L[0] = last_index
    L[-1] = first_index

intervert(L)
print(L)
        