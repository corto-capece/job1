for number in range(2, 1001):
    prime = True

    for divider in range(2, number):
        if number % divider == 0:
            prime = False
            continue

    if prime:
        print(number)
