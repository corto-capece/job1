import string

alphabet = string.ascii_lowercase * 10
index = 1

while index <= 29:
    print(alphabet[:index])
    index += 2